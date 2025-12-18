import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import threading
import os
import sys

# Ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import main as main_script

# Set Theme
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class OASGenApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("OAS Generation Tool")
        self.geometry("700x550")

        # Set Window Icon
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
        if not os.path.exists(icon_path):
            # Try looking one level up (dev mode)
            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icon.ico")
        
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass # Icon loading might fail on some systems/formats, ignore
        
        # Grid Layout Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)  # Log area expands

        # --- Header ---
        self.frame_header = ctk.CTkFrame(self, corner_radius=0)
        self.frame_header.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        
        self.lbl_title = ctk.CTkLabel(self.frame_header, text="OAS Generator", font=ctk.CTkFont(size=20, weight="bold"))
        self.lbl_title.pack(padx=10, pady=10, side="left")
        
        self.lbl_version = ctk.CTkLabel(self.frame_header, text="v1.0", font=ctk.CTkFont(size=12))
        self.lbl_version.pack(padx=10, pady=15, side="right")

        # --- Controls Area ---
        self.frame_controls = ctk.CTkFrame(self)
        self.frame_controls.grid(row=1, column=0, sticky="ew", padx=20, pady=10)
        self.frame_controls.grid_columnconfigure(1, weight=1) # Entry expands

        # Directory Selection
        self.lbl_dir = ctk.CTkLabel(self.frame_controls, text="Template Directory:")
        self.lbl_dir.grid(row=0, column=0, padx=15, pady=15, sticky="w")

        self.entry_dir = ctk.CTkEntry(self.frame_controls, placeholder_text="Path to API Templates...")
        self.entry_dir.grid(row=0, column=1, padx=(0, 10), pady=15, sticky="ew")
        
        # Default Path Logic
        default_path = os.path.join(os.getcwd(), "..", "API Templates")
        if os.path.exists(default_path):
             self.entry_dir.insert(0, os.path.abspath(default_path))
        else:
             self.entry_dir.insert(0, os.getcwd())

        self.btn_browse = ctk.CTkButton(self.frame_controls, text="Browse", width=100, command=self.browse_dir)
        self.btn_browse.grid(row=0, column=2, padx=15, pady=15)

        # Options
        self.lbl_opts = ctk.CTkLabel(self.frame_controls, text="Options:")
        self.lbl_opts.grid(row=1, column=0, padx=15, pady=(0, 15), sticky="w")
        
        self.frame_opts = ctk.CTkFrame(self.frame_controls, fg_color="transparent")
        self.frame_opts.grid(row=1, column=1, columnspan=2, sticky="w", padx=0, pady=(0, 15))

        self.var_30 = ctk.BooleanVar(value=True)
        self.chk_30 = ctk.CTkCheckBox(self.frame_opts, text="Generate OAS 3.0", variable=self.var_30)
        self.chk_30.pack(side="left", padx=(0, 20))
        
        self.var_31 = ctk.BooleanVar(value=True)
        self.chk_31 = ctk.CTkCheckBox(self.frame_opts, text="Generate OAS 3.1", variable=self.var_31)
        self.chk_31.pack(side="left")

        # Generate Button
        self.btn_gen = ctk.CTkButton(self, text="GENERATE SPECIFICATIONS", font=ctk.CTkFont(size=14, weight="bold"), height=40, command=self.start_generation)
        self.btn_gen.grid(row=3, column=0, padx=20, pady=(10, 20), sticky="ew")

        # --- Log Area ---
        self.frame_log = ctk.CTkFrame(self)
        self.frame_log.grid(row=2, column=0, sticky="nsew", padx=20, pady=0)
        self.frame_log.grid_rowconfigure(0, weight=1)
        self.frame_log.grid_columnconfigure(0, weight=1)

        self.log_area = ctk.CTkTextbox(self.frame_log)
        self.log_area.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.log_area.insert("0.0", "Ready.\n")
        self.log_area.configure(state="disabled") # Read-only primarily

    def browse_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.entry_dir.delete(0, 'end')
            self.entry_dir.insert(0, directory)
            
    def log(self, message):
        self.log_area.configure(state="normal")
        self.log_area.insert("end", message + "\n")
        self.log_area.see("end")
        self.log_area.configure(state="disabled")
        
    def start_generation(self):
        base_dir = self.entry_dir.get()
        gen_30 = self.var_30.get()
        gen_31 = self.var_31.get()
        
        if not base_dir:
            self.log("ERROR: Please select a directory.")
            return

        self.btn_gen.configure(state="disabled", text="GENERATING...")
        self.log_area.configure(state="normal")
        self.log_area.delete("1.0", "end")
        self.log_area.configure(state="disabled")
        self.log("Starting generation process...")
        
        # Run in thread
        t = threading.Thread(target=self.run_process, args=(base_dir, gen_30, gen_31))
        t.start()
        
    def run_process(self, base_dir, gen_30, gen_31):
        try:
            # Use log_callback adapter to push to GUI
            def gui_logger(msg):
                self.after(0, self.log, msg)
                
            main_script.generate_oas(base_dir, gen_30=gen_30, gen_31=gen_31, log_callback=gui_logger)
            
        except Exception as e:
            self.after(0, self.log, f"CRITICAL ERROR: {e}")
        finally:
            def reset_btn():
                self.btn_gen.configure(state="normal", text="GENERATE SPECIFICATIONS")
            self.after(0, reset_btn)

if __name__ == "__main__":
    app = OASGenApp()
    app.mainloop()

