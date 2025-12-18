import subprocess
import json
import os
import tempfile

class SpectralRunner:
    def __init__(self, spectral_cmd="spectral"):
        self.cmd = spectral_cmd

    def run_lint(self, file_path, log_callback=None):
        """
        Runs spectral lint on the given file.
        """
        def log(msg):
            if log_callback: log_callback(msg)

        if not os.path.exists(file_path):
            log(f"Error: File not found: {file_path}")
            return {'success': False, 'error_msg': f"File not found", 'summary': {}, 'details': []}

        fd, temp_out = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        
        # Determine command - rely on shell=True to pick up .cmd/.exe from PATH
        # Explicitly use the local .spectral.yaml to avoid "No ruleset found"
        ruleset_path = os.path.abspath(".spectral.yaml")
        if not os.path.exists(ruleset_path):
             # Fallback if file missing (though we just created it)
             command = f'{self.cmd} lint "{file_path}" -f json --output "{temp_out}"' 
        else:
             command = f'{self.cmd} lint "{file_path}" --ruleset "{ruleset_path}" -f json --output "{temp_out}"'
             
        log(f"Executing: {command}")
        
        try:
            # use stdin=DEVNULL to ensure it never waits for input
            process = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=20,
                stdin=subprocess.DEVNULL
            )
            
            log(f"Process ended. Return Code: {process.returncode}")
            if process.stderr:
                log(f"STDERR: {process.stderr[:200]}...") # Log first 200 chars of error
            
            if not os.path.exists(temp_out) or os.path.getsize(temp_out) == 0:
                 log("Error: Output file empty or missing.")
                 return {'success': False, 'error_msg': "Spectral output missing.", 'summary': {}, 'details': []}

            log("Parsing JSON output...")
            with open(temp_out, 'r', encoding='utf-8') as f:
                results = json.load(f)
            
            log(f"Found {len(results)} issues.")
            
            # Analyze results
            summary = {'error': 0, 'warning': 0, 'info': 0, 'hint': 0}
            simplified_details = []

            for item in results:
                severity_map = {0: 'error', 1: 'warning', 2: 'info', 3: 'hint'}
                severity_code = item.get('severity', 0)
                severity_str = severity_map.get(severity_code, 'error')
                
                summary[severity_str] = summary.get(severity_str, 0) + 1
                
                simplified_details.append({
                    'code': item.get('code'),
                    'message': item.get('message'),
                    'path': item.get('path', []),
                    'line': item.get('range', {}).get('start', {}).get('line', 0) + 1,
                    'severity': severity_str
                })

            return {
                'success': True,
                'summary': summary,
                'details': simplified_details,
                'raw_count': len(results)
            }

        except subprocess.TimeoutExpired:
             log("Error: Timeout Expired!")
             return {'success': False, 'error_msg': "Timeout (20s)", 'summary': {}, 'details': []}
        except Exception as e:
            log(f"Exception: {str(e)}")
            return {'success': False, 'error_msg': str(e), 'summary': {}, 'details': []}
        finally:
            if os.path.exists(temp_out):
                try:
                    os.remove(temp_out)
                except:
                    pass
