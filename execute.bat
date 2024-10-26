@echo off

:: Path to the virtual environment
set VENV_PATH=C:\ExamplePath\my_project\venv

:: Activate the virtual environment
call %VENV_PATH%\Scripts\activate

:: Full path to the Python script
set SCRIPT_PATH=C:\ExamplePath\my_project\backup_script.py

:: Run the Python script
python %SCRIPT_PATH%

:: Check if the script executed successfully
if %errorlevel%==0 (
    echo Backup completed.
    msg * "Backup completed successfully!"
) else (
    echo An error occurred while performing the backup.
    msg * "Error: backup failed."
)

:: Automatically close the terminal
exit
