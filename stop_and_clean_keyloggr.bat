@echo off
:: Find and kill the pythonw.exe process running keylogger.pyw
for /f "tokens=2 delims=," %%I in ('tasklist /FI "IMAGENAME eq pythonw.exe" /FO CSV /NH') do (
    taskkill /F /PID %%I
)

:: Wait for the process to terminate
timeout /t 2 /nobreak > nul

:: Delete the keylog.txt file
del "keylog.txt"
echo Keylogger stopped and log file deleted.
pause
exit
