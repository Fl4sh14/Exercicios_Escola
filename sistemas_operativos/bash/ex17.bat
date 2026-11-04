@echo off
:menu

echo 1 - Listar ficheiros
echo 2 - Criar pasta
echo 3 - Sair
set /p opcao=Escolhe: 

if %opcao%==1 dir
if %opcao%==2 mkdir nova_pasta
if %opcao%==3 exit

goto menu