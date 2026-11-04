@echo off

echo 1 - Mostrar data
echo 2 - Sair
set /p opcao=Escolhe: 

if %opcao%==1 date /t
if %opcao%==2 exit

pause