import os
import sys
import multiprocessing

# Required for PyInstaller to properly handle multiprocessing
if __name__ == "__main__":
    multiprocessing.freeze_support()

# Ensure project root is in sys.path
if getattr(sys, 'frozen', False):
    # Running in a bundle (PyInstaller)
    base_path = sys._MEIPASS
else:
    # Running in normal Python environment
    base_path = os.path.dirname(os.path.abspath(__file__))

if base_path not in sys.path:
    sys.path.insert(0, base_path)


if __name__ == "__main__":
    # Show splash screen and load app
    try:
        from src.splash_screen import show_splash_and_load_app
        app = show_splash_and_load_app()
    except ImportError:
        # Fallback: direct import without splash
        import customtkinter as ctk
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        try:
            from src.gui import OASGenApp
        except ImportError:
            from gui import OASGenApp
        
        app = OASGenApp()
    
    app.mainloop()
