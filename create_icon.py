from PIL import Image
import os

# Source path (Concept 19 - Manual Separator)
src_path = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\concept_19_manual.png"
dest_path = r"C:\Users\giuse\.gemini\antigravity\scratch\OAS_Generation_Tool\icon.ico"

try:
    img = Image.open(src_path)
    # Ensure high quality resampling
    img = img.resize((256, 256), Image.Resampling.LANCZOS)
    
    # Save as ICO with all standard sizes to cover all Windows views
    icon_sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    img.save(dest_path, format='ICO', sizes=icon_sizes)
    print(f"Successfully created icon at: {dest_path}")
except Exception as e:
    print(f"Error creating icon: {e}")
