@echo off
echo.
echo ========================================
echo  INSTALLAZIONE DIPENDENZE CASINO PROJECT
echo ========================================
echo.

REM Controlla se pip è disponibile
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo ERRORE: Python non è installato o pip non è disponibile!
    echo Installa Python da https://www.python.org
    pause
    exit /b 1
)

echo Installazione di matplotlib in corso...
echo.

python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERRORE: Installazione fallita!
    pause
    exit /b 1
)

echo.
echo ========================================
echo  INSTALLAZIONE COMPLETATA CON SUCCESSO!
echo ========================================
echo.
echo Puoi ora avviare il programma con:
echo   python main.py
echo.
pause
