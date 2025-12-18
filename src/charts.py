import customtkinter as ctk
import tkinter as tk
import math

class PieChart(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.canvas = tk.Canvas(self, bg=self._apply_appearance_mode(self._fg_color), highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Curated Palette (Material Design 500/600 level)
        self.palette = [
            '#F44336', # Red
            '#E91E63', # Pink
            '#9C27B0', # Purple
            '#673AB7', # Deep Purple
            '#3F51B5', # Indigo
            '#2196F3', # Blue
            '#03A9F4', # Light Blue
            '#00BCD4', # Cyan
            '#009688', # Teal
            '#4CAF50', # Green
            '#8BC34A', # Light Green
            '#CDDC39', # Lime
            '#FFEB3B', # Yellow
            '#FFC107', # Amber
            '#FF9800', # Orange
            '#FF5722', # Deep Orange
            '#795548', # Brown
            '#607D8B', # Blue Grey
        ]
        
        self.data = {}
        self.bind("<Configure>", self.draw)

    def _get_color(self, index):
        return self.palette[index % len(self.palette)]

    def set_data(self, data):
        self.data = data
        self.draw()

    def draw(self, event=None):
        self.canvas.delete("all")
        
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        
        if w < 50 or h < 50: return

        # Layout: Pie on Left (60%), Legend on Right (40%)
        pie_area_w = w * 0.6
        legend_start_x = w * 0.65
        
        # Pie Dimensions
        cx = pie_area_w / 2
        cy = h / 2
        radius = min(pie_area_w, h) / 2 - 20
        
        total = sum(self.data.values())
        
        if total == 0:
            self.canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, fill=self.colors['empty'], outline="")
            self.canvas.create_text(cx, cy, text="No Data", fill="gray")
            return

        start_angle = 90
        sorted_items = sorted(self.data.items(), key=lambda x: x[1], reverse=True)
        
        # Draw Pie
        for i, (key, value) in enumerate(sorted_items):
            if value == 0: continue
            
            extent = (value / total) * 360
            color = self._get_color(i)
            
            self.canvas.create_arc(
                cx - radius, cy - radius, cx + radius, cy + radius,
                start=start_angle, extent=extent,
                fill=color, outline="white", width=2
            )
            
            # Label on Pie (if large enough)
            if extent > 20:
                mid = math.radians(start_angle + extent / 2)
                lbl_r = radius * 0.7
                lx = cx + lbl_r * math.cos(mid)
                ly = cy - lbl_r * math.sin(mid)
                self.canvas.create_text(lx, ly, text=str(value), fill="white", font=("Arial", 10, "bold"))
                
            start_angle += extent

        # Draw Legend
        legend_y = 20
        for i, (key, value) in enumerate(sorted_items):
            if value == 0: continue
            color = self._get_color(i)
            
            # Color Box
            self.canvas.create_rectangle(legend_start_x, legend_y, legend_start_x + 15, legend_y + 15, fill=color, outline="")
            
            # Text (Code + Count) - Truncate if too long
            label_text = f"{key} ({value})"
            if len(label_text) > 30: label_text = label_text[:27] + "..."
            
            self.canvas.create_text(
                legend_start_x + 25, legend_y + 8, 
                text=label_text, 
                anchor="w", 
                fill=self._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"]),
                font=("Arial", 10)
            )
            
            legend_y += 20
            if legend_y > h - 20: # Stop if running out of space
                self.canvas.create_text(legend_start_x, legend_y + 5, text="...", anchor="w", fill="gray")
                break
