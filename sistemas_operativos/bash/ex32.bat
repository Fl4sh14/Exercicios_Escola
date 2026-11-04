@echo off
set soma=0

:loop
set /p num=Introduz um numero (ou escreve fim para terminar): 

if /i "%num%"=="fim" goto resultado

set /a soma=soma+num
goto loop

:resultado
echo.
echo A soma total e %soma%
pause
