import os
import sys
import unittest
import shutil

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import main

GOLDEN_FILE = "Expected results/EBACL_FPAD_20251110_OpenApi3.1_FPAD_API_Participant_4.1_v20251212.yaml"
OUTPUT_FILE = "API Templates/generated/generated_oas_3.1.yaml"
BASE_DIR = "API Templates"

class TestRegressionOAS31(unittest.TestCase):
    def test_regression_oas_31(self):
        """
        Runs the generation and compares output against the last known good file.
        """
        print(f"\n[INFO] Starting Regression Test...")
        
        # 1. Clean output
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)
        
        # 2. Run Generation
        # Use a list to capture logs instead of print
        logs = []
        def log_capture(msg):
            logs.append(msg)
            
        print("[INFO] Running Generator...")
        try:
            main.generate_oas(BASE_DIR, gen_30=False, gen_31=True, log_callback=log_capture)
        except Exception as e:
            self.fail(f"Generator crashed: {e}")
        
        # 3. Verify Output Exists
        self.assertTrue(os.path.exists(OUTPUT_FILE), "Output file was not generated")
        
        # 4. Compare with Golden
        if not os.path.exists(GOLDEN_FILE):
            print(f"[WARN] Golden file {GOLDEN_FILE} not found. Skipping comparison.")
            return

        with open(GOLDEN_FILE, 'r', encoding='utf-8') as f:
            golden_content = f.read()
            
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            generated_content = f.read()
            
        # Check size first
        len_golden = len(golden_content)
        len_gen = len(generated_content)
        size_diff = abs(len_golden - len_gen)
        print(f"[INFO] Size Diff: {size_diff} bytes (Golden: {len_golden}, Generated: {len_gen})")
        
        # Detailed diff if failed
        if golden_content != generated_content:
             self.fail(f"Content mismatch! Size diff: {size_diff} bytes.")

if __name__ == '__main__':
    unittest.main()
