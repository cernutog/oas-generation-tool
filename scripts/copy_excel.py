import shutil
import os

src = "API Templates/$index_reconstructed.xlsm"
dst = "API Templates/$index.xlsm"

if os.path.exists(src):
    shutil.copy(src, dst)
    print(f"Copied {src} to {dst}")
else:
    print(f"Source file not found: {src}")
