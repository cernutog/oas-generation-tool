import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import threading
import os
import sys
import json
import tempfile

# from . import main as main_script # Avoid circular import if possible, or use lazy import inside function
# But main.py imports gui.py? No, main.py imports gui.py logic. gui.py imports main.py for generate_oas? 
# Let's check logic. gui.py calls main_script.generate_oas.
# AND main.py imports gui to run app?
# Yes, circular dependency if top-level import.
# But inside run_gui.py, we import src.gui.
# If src.gui imports src.main, and src.main imports src.gui...
# src.main imports src.gui inside main() function (lazy import), so it's fine.

from . import main as main_script
from .linter import SpectralRunner
from .charts import SemanticPieChart
from .redoc_gen import RedocGenerator
from .preferences import PreferencesManager
from .preferences_dialog import PreferencesDialog
from chlorophyll import CodeView
import pygments.lexers

# Set Theme
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Module-level function for multiprocessing (must be picklable)
def _run_webview_process(html_file, window_title):
    """Target function for multiprocessing - runs pywebview in separate process."""
    try:
        import webview
        webview.create_window(window_title, html_file, width=1200, height=800)
        webview.start()
    except Exception as e:
        print(f"WebView error: {e}")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

class OASGenApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("OAS Generation Tool")
        self.geometry("1100x700")

        # Icon Setup
        try:
            icon_file = resource_path("icon.ico")
            if os.path.exists(icon_file):
                self.iconbitmap(icon_file)
        except Exception:
            pass 
        
        # Initialize Preferences Manager
        self.prefs_manager = PreferencesManager()
        
        # Apply saved window geometry if available
        if self.prefs_manager.get("remember_window_pos") and self.prefs_manager.get("window_geometry"):
            try:
                self.geometry(self.prefs_manager.get("window_geometry"))
            except:
                pass
        
        # Bind window close to save geometry
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        
        # Grid Layout Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1) # Tabview expands

        # --- Header ---
        self.frame_header = ctk.CTkFrame(self, corner_radius=0)
        self.frame_header.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        
        self.lbl_title = ctk.CTkLabel(self.frame_header, text="OAS Generator", font=ctk.CTkFont(size=20, weight="bold"))
        self.lbl_title.pack(padx=20, pady=15, side="left")
        
        self.lbl_version = ctk.CTkLabel(self.frame_header, text="v1.2.2", font=ctk.CTkFont(size=12))
        self.lbl_version.pack(padx=20, pady=15, side="right")
        
        # Settings button - use text for clarity
        self.btn_settings = ctk.CTkButton(
            self.frame_header, 
            text="⛭",  # Gear without hub, cleaner look
            width=35, 
            height=35,
            font=ctk.CTkFont(size=20),
            command=self.open_preferences
        )
        self.btn_settings.pack(padx=(0, 5), pady=10, side="right")
        
        # Add tooltip on hover
        self._tooltip = None
        self.btn_settings.bind("<Enter>", self._show_settings_tooltip)
        self.btn_settings.bind("<Leave>", self._hide_settings_tooltip)

        # --- Tab View ---
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        
        self.tab_gen = self.tabview.add("Generation")
        self.tab_val = self.tabview.add("Validation")

        # ==========================
        # TAB 1: GENERATION
        # ==========================
        self.tab_gen.grid_columnconfigure(0, weight=1)
        self.tab_gen.grid_rowconfigure(2, weight=1) # Log expands

        # Controls
        self.frame_controls = ctk.CTkFrame(self.tab_gen, fg_color="transparent")
        self.frame_controls.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        self.frame_controls.grid_columnconfigure(1, weight=1)

        self.lbl_dir = ctk.CTkLabel(self.frame_controls, text="Template Directory:", font=ctk.CTkFont(weight="bold"))
        self.lbl_dir.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_dir = ctk.CTkEntry(self.frame_controls, placeholder_text="Path to API Templates...")
        self.entry_dir.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ew")
        
        # Use saved preference or default path
        saved_template_dir = self.prefs_manager.get("template_directory", "")
        if saved_template_dir and os.path.exists(saved_template_dir):
            self.entry_dir.insert(0, saved_template_dir)
        else:
            default_path = os.path.join(os.getcwd(), "..", "API Templates")
            if os.path.exists(default_path):
                self.entry_dir.insert(0, os.path.abspath(default_path))
            else:
                self.entry_dir.insert(0, os.getcwd())

        self.btn_browse = ctk.CTkButton(self.frame_controls, text="Browse", width=100, command=self.browse_dir)
        self.btn_browse.grid(row=0, column=2, padx=10, pady=10)

        # OAS Output Folder (shared across all tabs)
        self.lbl_oas_folder = ctk.CTkLabel(self.frame_controls, text="OAS Output Folder:", font=ctk.CTkFont(weight="bold"))
        self.lbl_oas_folder.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_oas_folder = ctk.CTkEntry(self.frame_controls, placeholder_text="Path to OAS output folder...")
        self.entry_oas_folder.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="ew")
        
        # Use saved preference or default OAS folder
        saved_oas_folder = self.prefs_manager.get("oas_folder", "")
        if saved_oas_folder and os.path.exists(saved_oas_folder):
            self.entry_oas_folder.insert(0, saved_oas_folder)
        else:
            default_oas_folder = os.path.join(os.getcwd(), "OAS Generated")
            self.entry_oas_folder.insert(0, os.path.abspath(default_oas_folder))
        
        self.btn_browse_oas = ctk.CTkButton(self.frame_controls, text="Browse", width=100, command=self.browse_oas_folder)
        self.btn_browse_oas.grid(row=1, column=2, padx=10, pady=10)

        # Options
        self.frame_opts = ctk.CTkFrame(self.tab_gen, fg_color="transparent")
        self.frame_opts.grid(row=1, column=0, sticky="w", padx=20, pady=(0, 10))

        self.var_31 = ctk.BooleanVar(value=self.prefs_manager.get("gen_oas_31", True))
        self.chk_31 = ctk.CTkCheckBox(self.frame_opts, text="OAS 3.1", variable=self.var_31)
        self.chk_31.pack(side="left", padx=(0, 20))

        self.var_30 = ctk.BooleanVar(value=self.prefs_manager.get("gen_oas_30", True))
        self.chk_30 = ctk.CTkCheckBox(self.frame_opts, text="OAS 3.0", variable=self.var_30)
        self.chk_30.pack(side="left", padx=(0, 20))

        self.var_swift = ctk.BooleanVar(value=self.prefs_manager.get("gen_oas_swift", False))
        self.chk_swift = ctk.CTkCheckBox(self.frame_opts, text="OAS SWIFT", variable=self.var_swift)
        self.chk_swift.pack(side="left")

        # Generate Button layout on the right of opts? Or below? Below logs? 
        # Let's keep it prominent.
        self.btn_gen = ctk.CTkButton(self.frame_opts, text="GENERATE", font=ctk.CTkFont(weight="bold"), width=150, command=self.start_generation)
        self.btn_gen.pack(side="left", padx=40)

        # Log Area with theme from preferences
        gen_log_theme = self.prefs_manager.get("gen_log_theme", "Light")
        if gen_log_theme == "Dark":
            self.log_area = ctk.CTkTextbox(self.tab_gen, fg_color="#1e1e1e", text_color="#d4d4d4")
        else:
            self.log_area = ctk.CTkTextbox(self.tab_gen, fg_color="#ffffff", text_color="#333333")
        self.log_area.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.log_area.insert("0.0", "Ready to generate.\n")
        self.log_area.configure(state="disabled")

        # ==========================
        # TAB 2: VALIDATION
        # ==========================
        self.linter = SpectralRunner() 
        self.last_lint_result = None
        self.last_generated_files = []  # Track files from generation
        
        self.tab_val.grid_columnconfigure(0, weight=1) # List
        self.tab_val.grid_columnconfigure(1, weight=1) # Chart
        self.tab_val.grid_rowconfigure(2, weight=1)  # Content pane expands
        self.tab_val.grid_rowconfigure(3, weight=0)  # Footer row

        # Top Bar - OAS Folder
        self.frame_val_folder = ctk.CTkFrame(self.tab_val, fg_color="transparent")
        self.frame_val_folder.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 0))
        self.frame_val_folder.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(self.frame_val_folder, text="OAS Folder:", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=(0, 10), sticky="w")
        self.entry_val_oas_folder = ctk.CTkEntry(self.frame_val_folder, placeholder_text="Path to OAS folder...")
        self.entry_val_oas_folder.grid(row=0, column=1, padx=(0, 10), sticky="ew")
        # Sync with Generation tab (which uses preferences)
        self.entry_val_oas_folder.insert(0, self.entry_oas_folder.get())
        self.btn_browse_val_oas = ctk.CTkButton(self.frame_val_folder, text="Browse", width=80, command=self.browse_oas_folder_validation)
        self.btn_browse_val_oas.grid(row=0, column=2)

        # Top Bar - File Selector
        self.frame_val_top = ctk.CTkFrame(self.tab_val, fg_color="transparent")
        self.frame_val_top.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        
        # File Selector - use grid with weight for expansion
        self.frame_val_top.grid_columnconfigure(1, weight=1)  # Make combo column expand
        
        self.lbl_sel = ctk.CTkLabel(self.frame_val_top, text="Select File:", font=ctk.CTkFont(weight="bold"))
        self.lbl_sel.grid(row=0, column=0, padx=(0, 10))

        self.file_map = {} 
        self.cbo_files = ctk.CTkComboBox(self.frame_val_top, width=300, values=["No OAS files found"], command=self.on_file_select)
        self.cbo_files.grid(row=0, column=1, sticky="ew")  # Changed from 'w' to 'ew' for expansion
        
        # Refresh Button (reload file list)
        self.btn_refresh_val = ctk.CTkButton(self.frame_val_top, text="↻ Refresh", width=80, command=self.update_file_list)
        self.btn_refresh_val.grid(row=0, column=2, padx=(10, 0))

        # Filter Checkbox
        self.chk_ignore_br = ctk.CTkCheckBox(self.frame_val_top, text="Ignore 'Bad Request' Examples", command=self.on_filter_change)
        self.chk_ignore_br.grid(row=0, column=3, padx=(20, 0), sticky="w")
        self.chk_ignore_br.select() # Default Checked

        # Progress Bar (Indeterminate)
        # Progress Bar Removed as per user request


        # Main Layout: List vs Chart

        
        # Use PanedWindow for resizable Log Console
        self.paned_val = tk.PanedWindow(self.tab_val, orient="vertical", sashrelief="raised", bg="#d0d0d0")
        self.paned_val.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        # TOP PANE: Content (List + Chart)
        self.frame_val_content = ctk.CTkFrame(self.paned_val)
        self.paned_val.add(self.frame_val_content, minsize=200, sticky="nsew", stretch="always")
        
        self.frame_val_content.grid_columnconfigure(0, weight=1)
        self.frame_val_content.grid_columnconfigure(1, weight=1)
        self.frame_val_content.grid_rowconfigure(0, weight=1)

        self.frame_list = ctk.CTkScrollableFrame(self.frame_val_content, label_text="Issues List")
        self.frame_list.grid(row=0, column=0, sticky="nsew", padx=(0, 5), pady=5)
        
        self.frame_chart_container = ctk.CTkFrame(self.frame_val_content)
        self.frame_chart_container.grid(row=0, column=1, sticky="nsew", padx=(5, 0), pady=5)
        self.chart = SemanticPieChart(self.frame_chart_container)
        self.chart.pack(fill="both", expand=True, padx=10, pady=10)

        # Log Pane (Created but added dynamically)
        self.val_log_frame = ctk.CTkFrame(self.paned_val) # Container
        
        # Internal Log Header (Visible when expanded)
        self.log_internal_header = ctk.CTkFrame(self.val_log_frame, height=28, corner_radius=0, fg_color=("gray85", "gray20"))
        self.log_internal_header.pack(fill="x", side="top")
        
        self.btn_toggle_log_h = ctk.CTkButton(
            self.log_internal_header, text="▼ Logs", width=60, height=20, fg_color="transparent", 
            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.toggle_log
        )
        self.btn_toggle_log_h.pack(side="left", padx=5, pady=2)

        self.tab_logs = ctk.CTkTabview(self.val_log_frame, height=150)
        self.tab_logs.pack(fill="both", expand=True, padx=2, pady=0) # reduced top padding
        
        self.tab_logs.add("Analysis Logs")
        self.tab_logs.add("Spectral Output")
        
        # Tab 1: Analysis Logs with theme from preferences
        analysis_log_theme = self.prefs_manager.get("analysis_log_theme", "Light")
        if analysis_log_theme == "Dark":
            self.val_log = ctk.CTkTextbox(self.tab_logs.tab("Analysis Logs"), font=("Consolas", 11), state="disabled", fg_color="#1e1e1e", text_color="#d4d4d4")
        else:
            self.val_log = ctk.CTkTextbox(self.tab_logs.tab("Analysis Logs"), font=("Consolas", 11), state="disabled", fg_color="#ffffff", text_color="#333333")
        self.val_log.pack(fill="both", expand=True)

        # Tab 2: Spectral Output with theme from preferences
        spectral_log_theme = self.prefs_manager.get("spectral_log_theme", "Light")
        if spectral_log_theme == "Dark":
            self.val_json_log = ctk.CTkTextbox(self.tab_logs.tab("Spectral Output"), font=("Consolas", 11), state="disabled", wrap="none", fg_color="#1e1e1e", text_color="#d4d4d4")
        else:
            self.val_json_log = ctk.CTkTextbox(self.tab_logs.tab("Spectral Output"), font=("Consolas", 11), state="disabled", wrap="none", fg_color="#ffffff", text_color="#333333")
        self.val_json_log.pack(fill="both", expand=True)

        # Persistent Footer (Status Bar + Log Toggle) -> For Collapsed State
        self.footer_frame = ctk.CTkFrame(self.tab_val, height=30, corner_radius=0, fg_color=("gray85", "gray20"))
        self.footer_frame.grid(row=3, column=0, columnspan=2, sticky="ew")
        
        self.btn_toggle_log_f = ctk.CTkButton(
            self.footer_frame, text="▶ Logs", width=60, height=24, fg_color="transparent", 
            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.toggle_log
        )
        self.btn_toggle_log_f.pack(side="left", padx=5, pady=2)
        # ==========================
        # TAB 3: VIEW (REDOC)
        # ==========================
        self.tab_view_oas = self.tabview.add("View")
        self.tab_view_oas.grid_columnconfigure(0, weight=1)
        self.tab_view_oas.grid_rowconfigure(2, weight=1)  # Content at row 2

        # Top Bar - OAS Folder
        self.frame_view_folder = ctk.CTkFrame(self.tab_view_oas, fg_color="transparent")
        self.frame_view_folder.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
        self.frame_view_folder.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(self.frame_view_folder, text="OAS Folder:", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=(0, 10), sticky="w")
        self.entry_view_oas_folder = ctk.CTkEntry(self.frame_view_folder, placeholder_text="Path to OAS folder...")
        self.entry_view_oas_folder.grid(row=0, column=1, padx=(0, 10), sticky="ew")
        # Sync with Generation tab (which uses preferences)
        self.entry_view_oas_folder.insert(0, self.entry_oas_folder.get())
        self.btn_browse_view_oas = ctk.CTkButton(self.frame_view_folder, text="Browse", width=80, command=self.browse_oas_folder_view)
        self.btn_browse_view_oas.grid(row=0, column=2)

        # Top Bar - File Selector (row 1)
        self.frame_view_top = ctk.CTkFrame(self.tab_view_oas, fg_color="transparent")
        self.frame_view_top.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        ctk.CTkLabel(self.frame_view_top, text="Select File:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=(0, 10))
        
        # Combobox expands to fill available space
        self.cbo_view_files = ctk.CTkComboBox(self.frame_view_top, width=400, values=["No OAS files found"], command=self.on_view_file_select)
        self.cbo_view_files.pack(side="left", fill="x", expand=True)

        self.btn_refresh_view = ctk.CTkButton(self.frame_view_top, text="↻ Refresh", width=80, command=self.refresh_view_files)
        self.btn_refresh_view.pack(side="left", padx=(10, 0))
        
        # View Documentation button (no emoji, standard text)
        self.btn_open_viewer = ctk.CTkButton(
            self.frame_view_top, 
            text="View Documentation",
            width=150,
            command=self.open_documentation_viewer
        )
        self.btn_open_viewer.pack(side="left", padx=(10, 0))

        # Content Area - YAML Viewer with syntax highlighting (full width) - row 2
        self.frame_yaml = ctk.CTkFrame(self.tab_view_oas)
        self.frame_yaml.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        
        # Header bar with title and theme selector
        self.yaml_header = ctk.CTkFrame(self.frame_yaml, fg_color="transparent")
        self.yaml_header.pack(fill="x", padx=5, pady=2)
        
        ctk.CTkLabel(self.yaml_header, text="YAML Source", font=ctk.CTkFont(weight="bold")).pack(side="left")
        
        # Custom colorschemes directory
        if getattr(sys, 'frozen', False):
            self.colorschemes_dir = os.path.join(sys._MEIPASS, 'src', 'colorschemes')
        else:
            self.colorschemes_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'colorschemes')
        
        # Theme selector on the right (custom + bundled themes)
        self.available_themes = [
            "oas-dark", "oas-light",  # Custom app themes
            "github-dark", "nord", "one-dark", "vs-dark",  # Custom popular themes
            "monokai", "dracula", "ayu-dark", "ayu-light"  # Bundled chlorophyll themes
        ]
        self.cbo_yaml_theme = ctk.CTkComboBox(
            self.yaml_header, 
            width=140, 
            values=self.available_themes,
            command=self.on_theme_change
        )
        self.cbo_yaml_theme.set(self.prefs_manager.get("yaml_theme", "oas-dark"))
        self.cbo_yaml_theme.pack(side="right")
        ctk.CTkLabel(self.yaml_header, text="Theme:", font=ctk.CTkFont(size=12)).pack(side="right", padx=(0, 5))
        
        # Font size slider (before theme)
        self.lbl_font_val = ctk.CTkLabel(self.yaml_header, text=str(self.prefs_manager.get("yaml_font_size", 12)), width=25)
        self.lbl_font_val.pack(side="right", padx=(0, 10))
        self.slider_font_size = ctk.CTkSlider(
            self.yaml_header, from_=8, to=20, number_of_steps=12, width=100,
            command=self._on_font_size_change
        )
        self.slider_font_size.set(self.prefs_manager.get("yaml_font_size", 12))
        self.slider_font_size.pack(side="right")
        ctk.CTkLabel(self.yaml_header, text="Font:", font=ctk.CTkFont(size=12)).pack(side="right", padx=(0, 5))
        
        # CodeView with YAML lexer and line numbers
        yaml_font_size = self.prefs_manager.get("yaml_font_size", 12)
        yaml_font_family = self.prefs_manager.get("yaml_font", "Consolas")
        self.txt_yaml = CodeView(
            self.frame_yaml, 
            lexer=pygments.lexers.YamlLexer,
            color_scheme="monokai",  # Use built-in initially
            font=(yaml_font_family, yaml_font_size)
        )
        self.txt_yaml.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Apply saved theme after initialization
        saved_theme = self.prefs_manager.get("yaml_theme", "oas-dark")
        self.after(100, lambda: self.on_theme_change(saved_theme))

        # Redoc Generator initialization
        self.redoc_gen = RedocGenerator()

        self.val_log_print("Ready.")
        self.log_visible = False 
        
        # Load file lists on startup (after widgets are ready)
        self.after(200, self._load_files_on_startup)
    
    def _load_files_on_startup(self):
        """Load file lists in Validation and View tabs on startup."""
        oas_dir = self.entry_oas_folder.get()
        if os.path.exists(oas_dir):
            self.update_file_list()
        else:
            self.val_log_print(f"OAS folder not found: {oas_dir}")
    
    def _load_custom_theme(self, theme_name):
        """Load a custom TOML theme file and return as dict."""
        import toml
        custom_path = os.path.join(self.colorschemes_dir, f"{theme_name}.toml")
        if os.path.exists(custom_path):
            return toml.load(custom_path)
        return None
    
    def on_theme_change(self, theme_name):
        """Change the color scheme of the YAML viewer."""
        try:
            # Check if it's a custom theme (in our colorschemes folder)
            theme_dict = self._load_custom_theme(theme_name)
            if theme_dict:
                self.txt_yaml._set_color_scheme(theme_dict)
            else:
                # Use bundled chlorophyll theme
                self.txt_yaml._set_color_scheme(theme_name)
        except Exception as e:
            self.val_log_print(f"Error changing theme: {e}")
    
    def _show_settings_tooltip(self, event):
        """Show tooltip for settings button."""
        if self._tooltip is None:
            x = self.btn_settings.winfo_rootx() + self.btn_settings.winfo_width() // 2
            y = self.btn_settings.winfo_rooty() + self.btn_settings.winfo_height() + 5
            self._tooltip = tk.Toplevel(self)
            self._tooltip.wm_overrideredirect(True)
            self._tooltip.wm_geometry(f"+{x - 40}+{y}")
            label = tk.Label(self._tooltip, text="Preferences", bg="#333", fg="white", 
                           font=("Segoe UI", 9), padx=8, pady=4)
            label.pack()
    
    def _hide_settings_tooltip(self, event):
        """Hide tooltip for settings button."""
        if self._tooltip:
            self._tooltip.destroy()
            self._tooltip = None
    
    def _on_font_size_change(self, value):
        """Handle font size slider change in View tab."""
        font_size = int(value)
        self.lbl_font_val.configure(text=str(font_size))
        try:
            self.txt_yaml.configure(font=("Consolas", font_size))
            # Save to preferences
            self.prefs_manager.set("yaml_font_size", font_size)
            self.prefs_manager.save()
        except Exception:
            pass
    
    def _on_close(self):
        """Handle window close - save geometry and exit."""
        if self.prefs_manager.get("remember_window_pos"):
            geometry = self.geometry()
            self.prefs_manager.set("window_geometry", geometry)
            self.prefs_manager.save()
        self.destroy()
    
    def open_preferences(self):
        """Open the preferences dialog."""
        dialog = PreferencesDialog(self, self.prefs_manager, on_save_callback=self._apply_preferences)
        self.wait_window(dialog)
    
    def _apply_preferences(self, new_prefs: dict):
        """Apply new preferences to the UI."""
        # Apply YAML theme
        if "yaml_theme" in new_prefs:
            self.on_theme_change(new_prefs["yaml_theme"])
            self.cbo_yaml_theme.set(new_prefs["yaml_theme"])
        
        # Apply font size (if CodeView supports it)
        if "yaml_font_size" in new_prefs:
            try:
                font_size = new_prefs["yaml_font_size"]
                current_font = self.txt_yaml.cget("font")
                if isinstance(current_font, tuple):
                    self.txt_yaml.configure(font=(current_font[0], font_size))
                else:
                    self.txt_yaml.configure(font=("Consolas", font_size))
            except:
                pass
        
        # Apply generation checkboxes
        if new_prefs.get("gen_oas_30", True):
            self.var_30.set(True)
        else:
            self.var_30.set(False)
        
        if new_prefs.get("gen_oas_31", True):
            self.var_31.set(True)
        else:
            self.var_31.set(False)
        
        if new_prefs.get("gen_oas_swift", False):
            self.var_swift.set(True)
        else:
            self.var_swift.set(False)
        
        # Apply validation checkbox
        if new_prefs.get("ignore_bad_request", True):
            self.chk_ignore_br.select()
        else:
            self.chk_ignore_br.deselect()
        
        # Apply log themes immediately
        if "gen_log_theme" in new_prefs:
            theme = new_prefs["gen_log_theme"]
            if theme == "Dark":
                self.log_area.configure(fg_color="#1e1e1e", text_color="#d4d4d4")
            else:
                self.log_area.configure(fg_color="#ffffff", text_color="#333333")
        
        if "analysis_log_theme" in new_prefs:
            theme = new_prefs["analysis_log_theme"]
            if theme == "Dark":
                self.val_log.configure(fg_color="#1e1e1e", text_color="#d4d4d4")
            else:
                self.val_log.configure(fg_color="#ffffff", text_color="#333333")
        
        if "spectral_log_theme" in new_prefs:
            theme = new_prefs["spectral_log_theme"]
            if theme == "Dark":
                self.val_json_log.configure(fg_color="#1e1e1e", text_color="#d4d4d4")
            else:
                self.val_json_log.configure(fg_color="#ffffff", text_color="#333333")
        
        # Refresh file list with new sort order
        self.update_file_list()
        
    def toggle_log(self):
        if self.log_visible:
            # COLLAPSE
            self.paned_val.forget(self.val_log_frame) # Hide Pane 2
            self.footer_frame.grid() # Show Footer
            self.log_visible = False
        else:
            # EXPAND
            self.footer_frame.grid_remove() # Hide Footer
            self.paned_val.add(self.val_log_frame, minsize=100, sticky="nsew", stretch="always") # Show Pane 2
            self.log_visible = True

    def val_log_print(self, msg):
        self.val_log.configure(state="normal")
        self.val_log.insert("end", f"> {msg}\n")
        self.val_log.see("end")
        self.val_log.configure(state="disabled")

    def browse_dir(self):
        current_path = self.entry_dir.get()
        initial_dir = current_path if os.path.exists(current_path) else os.getcwd()
        directory = filedialog.askdirectory(initialdir=initial_dir)
        if directory:
            self.entry_dir.delete(0, 'end')
            self.entry_dir.insert(0, directory)
    
    def _sync_oas_folders(self, new_path):
        """Sync OAS folder value across all tabs."""
        # Update Generation tab
        self.entry_oas_folder.delete(0, 'end')
        self.entry_oas_folder.insert(0, new_path)
        # Update Validation tab
        self.entry_val_oas_folder.delete(0, 'end')
        self.entry_val_oas_folder.insert(0, new_path)
        # Update View tab
        self.entry_view_oas_folder.delete(0, 'end')
        self.entry_view_oas_folder.insert(0, new_path)
        # Clear last generated files so update_file_list reads from folder
        self.last_generated_files = []
        # Refresh file lists
        self.update_file_list()
        self.refresh_view_files()
    
    def browse_oas_folder(self):
        """Browse for OAS folder (Generation tab)."""
        current_path = self.entry_oas_folder.get()
        initial_dir = current_path if os.path.exists(current_path) else os.getcwd()
        directory = filedialog.askdirectory(initialdir=initial_dir)
        if directory:
            self._sync_oas_folders(directory)
    
    def browse_oas_folder_validation(self):
        """Browse for OAS folder (Validation tab)."""
        current_path = self.entry_val_oas_folder.get()
        initial_dir = current_path if os.path.exists(current_path) else os.getcwd()
        directory = filedialog.askdirectory(initialdir=initial_dir)
        if directory:
            self._sync_oas_folders(directory)
    
    def browse_oas_folder_view(self):
        """Browse for OAS folder (View tab)."""
        current_path = self.entry_view_oas_folder.get()
        initial_dir = current_path if os.path.exists(current_path) else os.getcwd()
        directory = filedialog.askdirectory(initialdir=initial_dir)
        if directory:
            self._sync_oas_folders(directory)
            
    def log(self, message):
        self.log_area.configure(state="normal")
        self.log_area.insert("end", message + "\n")
        self.log_area.see("end")
        self.log_area.configure(state="disabled")
        
    def start_generation(self):
        base_dir = self.entry_dir.get()
        gen_30 = self.var_30.get()
        gen_31 = self.var_31.get()
        gen_swift = self.var_swift.get()
        
        if not base_dir:
            self.log("ERROR: Please select a directory.")
            return

        self.btn_gen.configure(state="disabled", text="GENERATING...")
        self.log("Starting generation process...")
        
        t = threading.Thread(target=self.run_process, args=(base_dir, gen_30, gen_31, gen_swift))
        t.start()
        
    def run_process(self, base_dir, gen_30, gen_31, gen_swift):
        try:
            self.last_generated_files = [] 
            output_dir = self.entry_oas_folder.get()  # Get OAS output folder
            
            def gui_logger(msg):
                self.after(0, self.log, msg)
                if "Writing OAS" in msg:
                    parts = msg.split(": ")
                    if len(parts) > 1:
                         self.last_generated_files.append(parts[1].strip())
                         self.after(0, self.update_file_list)
                         
            main_script.generate_oas(base_dir, gen_30=gen_30, gen_31=gen_31, gen_swift=gen_swift, output_dir=output_dir, log_callback=gui_logger)
            
        except Exception as e:
            self.after(0, self.log, f"CRITICAL ERROR: {e}")
        finally:
            def reset_btn():
                self.btn_gen.configure(state="normal", text="GENERATE")
                self.after(0, self.update_file_list) # Final refresh
            self.after(0, reset_btn)

    def update_file_list(self):
        files_to_show = []
        candidates = set()  # Use set to avoid duplicates
        
        # Always read from OAS folder
        oas_dir = self.entry_oas_folder.get()
        if os.path.exists(oas_dir):
            for f in os.listdir(oas_dir):
                if f.endswith(".yaml") or f.endswith(".json"):
                    candidates.add(os.path.join(oas_dir, f))
        
        # Also add last generated files (in case they're in a different folder)
        for f in self.last_generated_files:
            if os.path.exists(f):
                candidates.add(f)
        
        # Sort based on preference
        sort_order = self.prefs_manager.get("file_sort_order", "alphabetical")
        if sort_order == "newest_first":
            sorted_candidates = sorted(candidates, key=lambda f: os.path.getmtime(f), reverse=True)
        elif sort_order == "oldest_first":
            sorted_candidates = sorted(candidates, key=lambda f: os.path.getmtime(f))
        else:  # alphabetical
            sorted_candidates = sorted(candidates)
        
        self.file_map = {}
        display_names = []
        for path in sorted_candidates:
            name = os.path.basename(path)
            self.file_map[name] = path
            display_names.append(name)
            
        if display_names:
            self.cbo_files.configure(values=display_names)
            self.cbo_files.set(display_names[0])
            # Always run validation on file selection
            self.run_validation()
        else:
            self.cbo_files.configure(values=["No OAS files found"])
            self.cbo_files.set("No OAS files found")
            
        # Refresh View Tab
        self.refresh_view_files()
            
    def on_file_select(self, value):
        # Sync with View tab combo and load YAML
        if value in self.view_file_map:
            self.cbo_view_files.set(value)
            self.on_view_file_select(value)  # Load YAML content in View tab
        self.run_validation()

    def run_validation(self):
        selected_name = self.cbo_files.get()
        selected_file = self.file_map.get(selected_name)
        
        if not selected_file or not os.path.exists(selected_file):
            self.val_log_print("File not found or not selected.")
            return
            
        self.val_log_print(f"Starting validation for: {selected_name}")
        # self.progress_val.start() 
        
        for widget in self.frame_list.winfo_children():
            widget.destroy()

        def validate_thread():
            try:
                # Capture logs from linter
                def thread_logger(msg):
                    self.after(0, lambda: self.val_log_print(msg))
                    
                result = self.linter.run_lint(selected_file, log_callback=thread_logger)
                self.after(0, lambda: self.show_results(result))
            except Exception as e:
                 self.after(0, lambda: self.val_log_print(f"THREAD CRASH: {e}"))
            finally:
                pass 
                # self.after(0, self.progress_val.stop)

        t = threading.Thread(target=validate_thread)
        t.start()

    def on_filter_change(self):
        if self.last_lint_result:
            self.show_results(self.last_lint_result)

    def show_results(self, result):
        self.last_lint_result = result # Store for filtering
        
        if not result['success']:
            self.val_log_print(f"Error: {result.get('error_msg', 'Unknown Error')}")
            self.frame_list.configure(label_text="Error")
            # Clear previous
            for widget in self.frame_list.winfo_children(): widget.destroy()
            
            err_lbl = ctk.CTkLabel(self.frame_list, text=result.get('error_msg', 'Unknown Error'), text_color="red")
            err_lbl.pack()
            return

        summary = result['summary']
        code_summary = result.get('code_summary', summary) # Fallback if missing
        details = result['details']
        
        # Apply Filters
        if self.chk_ignore_br.get() == 1:
            filtered_details = []
            # Recalculate code_summary from filtered details
            filtered_code_summary = {}
            filtered_summary = {'error': 0, 'warning': 0, 'info': 0, 'hint': 0}
            
            for item in details:
                path_str = item.get('path', '')
                # Filter Condition: Path contains 'examples' AND 'Bad Request' (case insensitive match if needed, but usually strict)
                # Adding some flexibility: "examples" > ... "Bad Request"
                if "examples" in path_str and "Bad Request" in path_str:
                    continue # Skip this issue
                    
                filtered_details.append(item)
                
                # Rebuild stats
                code = item['code']
                sev = item['severity']
                filtered_summary[sev] = filtered_summary.get(sev, 0) + 1
                
                if code not in filtered_code_summary:
                    filtered_code_summary[code] = {'count': 0, 'severity': sev}
                filtered_code_summary[code]['count'] += 1
                
            details = filtered_details
            summary = filtered_summary
            code_summary = filtered_code_summary
            
        total_issues = len(details)
        
        self.val_log_print(f"Check Complete: {total_issues} issues found.")
        self.frame_list.configure(label_text=f"Issues ({total_issues})")
        
        # Update Chart - Use code_summary for detailed breakdown
        self.chart.set_data(code_summary)

        # Populate Raw JSON Tab
        raw_data = result.get('raw_data', [])
        formatted_json = json.dumps(raw_data, indent=2)
        
        self.val_json_log.configure(state="normal")
        self.val_json_log.delete("0.0", "end")
        self.val_json_log.insert("0.0", formatted_json)
        self.val_json_log.configure(state="disabled")

        # Populate List
        for widget in self.frame_list.winfo_children(): widget.destroy()

        if total_issues == 0:
             ctk.CTkLabel(self.frame_list, text="No issues found! Great job!", text_color="green", font=("Arial", 16)).pack(pady=20)
        else:
            for item in details:
                # Severity Color
                color = "gray"
                if item['severity'] == "error": color = "#FF4444"
                elif item['severity'] == "warning": color = "#FFBB33"
                elif item['severity'] == "info": color = "#33B5E5"
                
                # Card Frame
                card = ctk.CTkFrame(self.frame_list, border_width=1, border_color="gray")
                card.pack(fill="x", pady=2, padx=2)
                
                # Row 1: Code + Severity
                r1 = ctk.CTkFrame(card, fg_color="transparent")
                r1.pack(fill="x", padx=5, pady=2)
                ctk.CTkLabel(r1, text=f"[{item['severity'].upper()}]", text_color=color, font=("Arial", 11, "bold")).pack(side="left")
                ctk.CTkLabel(r1, text=item['code'], font=("Arial", 11, "bold")).pack(side="left", padx=5)
                ctk.CTkLabel(r1, text=f"Line: {item['line']}", text_color="gray", font=("Arial", 10)).pack(side="right")
                
                # Row 2: Path
                if item['path'] and item['path'] != "Root":
                     # High contrast for path
                     path_color = ("#333333", "#CCCCCC") # Dark in light mode, Light in dark mode
                     ctk.CTkLabel(card, text=f"Path: {item['path']}", text_color=path_color, font=("Consolas", 10, "bold"), anchor="w", justify="left", wraplength=350).pack(fill="x", padx=5)

                # Row 3: Message
                ctk.CTkLabel(card, text=item['message'], anchor="w", justify="left", wraplength=350).pack(fill="x", padx=5, pady=(0, 5))

    
    def refresh_view_files(self):
        # Use OAS folder from View tab entry
        oas_dir = self.entry_view_oas_folder.get()
        candidates = []
        if os.path.exists(oas_dir):
            for f in os.listdir(oas_dir):
                if f.endswith(".yaml") or f.endswith(".json"):
                    candidates.append(os.path.join(oas_dir, f))
        
        # Sort based on preference (same as Validation tab)
        sort_order = self.prefs_manager.get("file_sort_order", "alphabetical")
        if sort_order == "newest_first":
            sorted_candidates = sorted(candidates, key=lambda f: os.path.getmtime(f), reverse=True)
        elif sort_order == "oldest_first":
            sorted_candidates = sorted(candidates, key=lambda f: os.path.getmtime(f))
        else:  # alphabetical
            sorted_candidates = sorted(candidates)
        
        self.view_file_map = {}
        display_names = []
        for path in sorted_candidates:
            name = os.path.basename(path)
            self.view_file_map[name] = path
            display_names.append(name)
        
        if display_names:
            self.cbo_view_files.configure(values=display_names)
            self.cbo_view_files.set(display_names[0])
            self.on_view_file_select(display_names[0])
        else:
             self.cbo_view_files.configure(values=["No OAS files found"])
             self.cbo_view_files.set("No OAS files found")

    def on_view_file_select(self, value):
        # Sync with Validation tab combo
        if value in self.file_map:
            self.cbo_files.set(value)
        
        filepath = self.view_file_map.get(value)
        if not filepath or not os.path.exists(filepath):
            return

        # Load YAML into viewer
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # CodeView uses standard tk.Text API
            self.txt_yaml.config(state="normal")
            self.txt_yaml.delete("1.0", "end")
            self.txt_yaml.insert("1.0", content)
            self.txt_yaml.config(state="disabled")
            
            # Store the current content for browser opening
            self._current_yaml_content = content
            self._current_file_name = os.path.basename(filepath)
            
        except Exception as e:
            self.val_log_print(f"Error loading view: {e}")

    def open_in_browser(self):
        """Generate Redoc HTML and open it in the system's default browser."""
        import webbrowser
        
        if not hasattr(self, '_current_yaml_content') or not self._current_yaml_content:
            return
        
        try:
            # Generate HTML
            html_content = self.redoc_gen.get_html_content(self._current_yaml_content)
            
            # Save to file in the generated folder
            base_dir = self.entry_dir.get()
            gen_dir = os.path.join(base_dir, "generated")
            if not os.path.exists(gen_dir):
                os.makedirs(gen_dir)
            
            # Create a nice filename
            html_filename = self._current_file_name.replace('.yaml', '_redoc.html').replace('.json', '_redoc.html')
            html_path = os.path.join(gen_dir, html_filename)
            
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Open in browser
            webbrowser.open(f"file:///{html_path.replace(os.sep, '/')}")
            
            self.val_log_print(f"Opened documentation in browser: {html_path}")
            
        except Exception as e:
            self.val_log_print(f"Error opening browser: {e}")

    def open_documentation_viewer(self):
        """Open documentation in a native pywebview window via multiprocessing."""
        if not hasattr(self, '_current_yaml_content') or not self._current_yaml_content:
            return
        
        try:
            # Generate HTML
            html_content = self.redoc_gen.get_html_content(self._current_yaml_content)
            
            # Save to file
            base_dir = self.entry_dir.get()
            gen_dir = os.path.join(base_dir, "generated")
            if not os.path.exists(gen_dir):
                os.makedirs(gen_dir)
            
            html_filename = self._current_file_name.replace('.yaml', '_redoc.html').replace('.json', '_redoc.html')
            html_path = os.path.join(gen_dir, html_filename)
            
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.val_log_print(f"Generated documentation: {html_path}")
            
            title = f"API Documentation - {self._current_file_name}"
            
            # Launch webview in a separate process (avoids COM conflicts)
            import multiprocessing
            
            # Start as a separate process using module-level function
            p = multiprocessing.Process(target=_run_webview_process, args=(html_path, title))
            p.start()
            
        except Exception as e:
            self.val_log_print(f"Error opening viewer: {e}")

if __name__ == "__main__":
    app = OASGenApp()
    app.mainloop()

