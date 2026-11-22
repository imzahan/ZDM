@echo off
cd /d "%~dp0"
if exist "dist\ZDM-3.0.0-portable\zdm.exe" (
    cd dist\ZDM-3.0.0-portable
    start "" zdm.exe %*
) else (
    cargo run --release -p mdm-app -- %*
)
