import subprocess
import json
import os
import tempfile

class SpectralRunner:
    def __init__(self, spectral_cmd="spectral"):
        self.cmd = spectral_cmd

    def run_lint(self, file_path):
        """
        Runs spectral lint on the given file and returns the parsed results.
        Returns:
            dict: {
                'success': bool,
                'summary': {'error': 0, 'warning': 0, 'info': 0, 'hint': 0},
                'details': [list of result objects],
                'error_msg': str (if execution failed)
            }
        """
        if not os.path.exists(file_path):
            return {'success': False, 'error_msg': f"File not found: {file_path}", 'summary': {}, 'details': []}

        # Create a temp file for JSON output
        fd, temp_out = tempfile.mkstemp(suffix='.json')
        os.close(fd)

        # Build command
        # remove cmd /c prefix, rely on shell=True to find executable in path
        command = f'{self.cmd} lint "{file_path}" -f json --output "{temp_out}"'
        
        try:
            # We don't check return code because Spectral returns 1 if issues are found.
            # Added timeout to prevent hanging
            subprocess.run(command, check=False, shell=True, capture_output=True, timeout=30)
            
            if not os.path.exists(temp_out) or os.path.getsize(temp_out) == 0:
                 return {'success': False, 'error_msg': "Spectral failed to generate output (or timed out). check console/path.", 'summary': {}, 'details': []}

            with open(temp_out, 'r', encoding='utf-8') as f:
                results = json.load(f)
            
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

        except Exception as e:
            return {'success': False, 'error_msg': str(e), 'summary': {}, 'details': []}
        finally:
            if os.path.exists(temp_out):
                try:
                    os.remove(temp_out)
                except:
                    pass
