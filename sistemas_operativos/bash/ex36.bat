@echo off
:menu
cls
echo =====================
echo        MENU
echo =====================
echo 1 - Abrir Notepad
echo 2 - Abrir Paint
echo 3 - Abrir Calculadora
echo 0 - Sair
echo =====================
set /p opcao=Escolhe uma opcao: 

if "%opcao%"=="1" goto notepad
if "%opcao%"=="2" goto paint
if "%opcao%"=="3" goto calc
if "%opcao%"=="0" goto fim

echo Opcao invalida!
pause
goto menu

:notepad
start notepad.exe
goto menu

:paint
start mspaint.exe
goto menu

:calc
start calc.exe
goto menu

:fim
echo Ate logo!
pause
exit