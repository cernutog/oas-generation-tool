@echo off
echo Building OAS Generator Executable...
python -m PyInstaller OAS_Gen_Tool.spec
if %errorlevel% neq 0 (
    echo Build failed!
    exit /b %errorlevel%
)
echo Build successful! Executable is in dist/
