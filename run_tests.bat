@echo off
REM ===============================================
REM Run all pytest tests with Allure reporting
REM ===============================================

REM --- Activate Python virtual environment ---
IF EXIST ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
) ELSE (
    echo ERROR: Virtual environment not found! Make sure .venv exists.
    pause
    exit /b 1
)

REM --- Create reports folder if it doesn't exist ---
IF NOT EXIST "reports" mkdir reports

REM --- Run pytest with Allure ---
pytest --alluredir=reports

REM --- Serve Allure report ---
IF %ERRORLEVEL% EQU 0 (
    echo Launching Allure report...
    allure serve reports
) ELSE (
    echo Pytest failed. Check the errors above.
)

REM --- Pause at the end so window doesn't close ---
pause
