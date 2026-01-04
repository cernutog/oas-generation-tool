"""
Splash Screen for OASIS - OAS Integration Suite.
Shows animated loading screen while the main application initializes.
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sys
import threading
import time


class SplashScreen:
    """Animated splash screen with progress bar."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # No window decorations
        self.root.attributes('-topmost', True)
        
        # Get screen dimensions for centering
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Splash dimensions
        splash_width = 400
        splash_height = 350
        
        # Center the splash
        x = (screen_width - splash_width) // 2
        y = (screen_height - splash_height) // 2
        self.root.geometry(f"{splash_width}x{splash_height}+{x}+{y}")
        
        # Background color
        self.root.configure(bg='#0D1B2A')
        
        # Main frame
        self.frame = tk.Frame(self.root, bg='#0D1B2A')
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Load and display logo
        self._load_logo()
        
        # Title
        self.title_label = tk.Label(
            self.frame,
            text="OASIS",
            font=('Segoe UI', 32, 'bold'),
            fg='#00BCD4',
            bg='#0D1B2A'
        )
        self.title_label.pack(pady=(10, 0))
        
        # Subtitle
        self.subtitle_label = tk.Label(
            self.frame,
            text="OAS Integration Suite",
            font=('Segoe UI', 12),
            fg='#78909C',
            bg='#0D1B2A'
        )
        self.subtitle_label.pack(pady=(0, 20))
        
        # Status label
        self.status_label = tk.Label(
            self.frame,
            text="Initializing...",
            font=('Segoe UI', 9),
            fg='#546E7A',
            bg='#0D1B2A'
        )
        self.status_label.pack(pady=(10, 5))
        
        # Progress bar style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Splash.Horizontal.TProgressbar",
            troughcolor='#1B3A4B',
            background='#00BCD4',
            lightcolor='#00BCD4',
            darkcolor='#0097A7',
            bordercolor='#0D1B2A',
            thickness=8
        )
        
        # Progress bar
        self.progress = ttk.Progressbar(
            self.frame,
            style="Splash.Horizontal.TProgressbar",
            orient='horizontal',
            length=300,
            mode='determinate'
        )
        self.progress.pack(pady=(0, 10))
        
        # Version label
        self.version_label = tk.Label(
            self.frame,
            text="v2.0",
            font=('Segoe UI', 8),
            fg='#37474F',
            bg='#0D1B2A'
        )
        self.version_label.pack(side='bottom')
        
        self.root.update()
    
    def _load_logo(self):
        """Load the OASIS logo image."""
        try:
            # Determine base path
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            
            logo_path = os.path.join(base_path, 'src', 'resources', 'oasis_splash.png')
            
            if os.path.exists(logo_path):
                img = Image.open(logo_path)
                img = img.resize((150, 150), Image.Resampling.LANCZOS)
                self.logo_image = ImageTk.PhotoImage(img)
                
                logo_label = tk.Label(
                    self.frame,
                    image=self.logo_image,
                    bg='#0D1B2A'
                )
                logo_label.pack(pady=(10, 0))
            else:
                # Fallback: show text logo
                self._show_text_logo()
        except Exception as e:
            print(f"Could not load splash logo: {e}")
            self._show_text_logo()
    
    def _show_text_logo(self):
        """Show text-based logo as fallback."""
        logo_frame = tk.Frame(self.frame, bg='#0D1B2A')
        logo_frame.pack(pady=(20, 0))
        
        # ASCII-style palm tree
        palm_text = """
    <>  <>  <>
      \\ | /
       \\|/
        {}
        {}
        {}
        """
        palm_label = tk.Label(
            logo_frame,
            text=palm_text,
            font=('Consolas', 14),
            fg='#00BCD4',
            bg='#0D1B2A',
            justify='center'
        )
        palm_label.pack()
    
    def update_progress(self, value, status_text=None):
        """Update progress bar and status text."""
        self.progress['value'] = value
        if status_text:
            self.status_label.config(text=status_text)
        self.root.update()
    
    def close(self):
        """Close the splash screen."""
        self.root.destroy()


def show_splash_and_load_app():
    """
    Show splash screen, load the main app in background, then switch.
    Returns the main app instance.
    """
    # Create splash
    splash = SplashScreen()
    
    # Simulate loading stages
    loading_stages = [
        (10, "Loading core modules..."),
        (25, "Initializing UI framework..."),
        (40, "Loading parsers..."),
        (55, "Loading generators..."),
        (70, "Loading validators..."),
        (85, "Preparing workspace..."),
        (95, "Almost ready..."),
    ]
    
    # Import heavy modules with progress updates
    for progress, status in loading_stages:
        splash.update_progress(progress, status)
        time.sleep(0.15)  # Small delay for visual effect
    
    # Import the main app (the heavy part)
    import customtkinter as ctk
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    splash.update_progress(100, "Starting OASIS...")
    time.sleep(0.3)
    
    # Import and create main app
    try:
        from src.gui import OASGenApp
    except ImportError:
        from gui import OASGenApp
    
    # Close splash
    splash.close()
    
    # Create and return main app
    return OASGenApp()


if __name__ == "__main__":
    # Test the splash screen
    splash = SplashScreen()
    for i in range(0, 101, 10):
        splash.update_progress(i, f"Loading... {i}%")
        time.sleep(0.2)
    splash.close()
