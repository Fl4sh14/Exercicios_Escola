@echo off

for /l %%i in (10,-1,0) do (
    echo %%i
    timeout /t 1 >nul
)

echo Tempo terminado
pause