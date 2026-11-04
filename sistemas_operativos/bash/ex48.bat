@echo off
setlocal enabledelayedexpansion

set soma=0

for /f "tokens=*" %%a in (numeros.txt) do (
    set /a soma=!soma! + %%a
)

echo A soma total é: %soma%
pause
