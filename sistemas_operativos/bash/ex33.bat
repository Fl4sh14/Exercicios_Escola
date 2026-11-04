@echo off
set /p tempo=Introduz o tempo para o contador regressivo: 

:loop
echo Tempo restante: %tempo% segundos
timeout /t 1 >nul
set /a tempo=%tempo%-1

if %tempo% GEQ 0 goto loop

echo Contagem terminada!
pause
