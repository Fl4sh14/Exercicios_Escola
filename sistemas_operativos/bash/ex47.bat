@echo off
setlocal enabledelayedexpansion

set "ficheiro=numeros.txt"

set /a soma=0

for /f "usebackq tokens=*" %%L in ("%ficheiro%") do (
    set /a soma+=%%L
)

echo A soma total dos numeros e: !soma!
pause
