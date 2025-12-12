import tkinter as tk
from tkinter import filedialog, scrolledtext
import threading
import os
import sys

# Ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import main as main_script

class OASGenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OAS Generation Tool")
        self.root.geometry("600x450")
        
        # Directory Selection
        self.lbl_dir = tk.Label(root, text="Template Directory:")
        self.lbl_dir.pack(pady=5)
        
        frame_dir = tk.Frame(root)
        frame_dir.pack(pady=5)
        
        self.entry_dir = tk.Entry(frame_dir, width=50)
        self.entry_dir.pack(side=tk.LEFT, padx=5)
        
        # Default to API Templates if exists
        default_path = os.path.join(os.getcwd(), "..", "API Templates")
        if os.path.exists(default_path):
             self.entry_dir.insert(0, os.path.abspath(default_path))
        else:
             self.entry_dir.insert(0, os.getcwd())

        self.btn_browse = tk.Button(frame_dir, text="Browse", command=self.browse_dir)
        self.btn_browse.pack(side=tk.LEFT)
        
        # Options
        frame_opts = tk.Frame(root)
        frame_opts.pack(pady=10)
        
        self.var_30 = tk.BooleanVar(value=True)
        self.chk_30 = tk.Checkbutton(frame_opts, text="Generate OAS 3.0", variable=self.var_30)
        self.chk_30.pack(side=tk.LEFT, padx=10)
        
        self.var_31 = tk.BooleanVar(value=True)
        self.chk_31 = tk.Checkbutton(frame_opts, text="Generate OAS 3.1", variable=self.var_31)
        self.chk_31.pack(side=tk.LEFT, padx=10)
        
        # Generate Button
        self.btn_gen = tk.Button(root, text="Generate", command=self.start_generation, bg="#dddddd", height=2, width=20)
        self.btn_gen.pack(pady=10)
        
        # Log Area
        self.log_area = scrolledtext.ScrolledText(root, height=15)
        self.log_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
    def browse_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.entry_dir.delete(0, tk.END)
            self.entry_dir.insert(0, directory)
            
    def log(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
        
    def start_generation(self):
        base_dir = self.entry_dir.get()
        gen_30 = self.var_30.get()
        gen_31 = self.var_31.get()
        
        if not base_dir:
            self.log("Please select a directory.")
            return

        self.btn_gen.config(state=tk.DISABLED)
        self.log_area.delete(1.0, tk.END)
        self.log("Starting generation...")
        
        # Run in thread
        t = threading.Thread(target=self.run_process, args=(base_dir, gen_30, gen_31))
        t.start()
        
    def run_process(self, base_dir, gen_30, gen_31):
        try:
            # Use log_callback adapter to push to GUI
            def gui_logger(msg):
                self.root.after(0, self.log, msg)
                
            main_script.generate_oas(base_dir, gen_30=gen_30, gen_31=gen_31, log_callback=gui_logger)
            
        except Exception as e:
            self.root.after(0, self.log, f"Error: {e}")
        finally:
            self.root.after(0, lambda: self.btn_gen.config(state=tk.NORMAL))

if __name__ == "__main__":
    root = tk.Tk()
    app = OASGenApp(root)
    root.mainloop()
