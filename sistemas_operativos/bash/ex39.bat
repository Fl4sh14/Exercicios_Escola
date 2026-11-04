@echo off
:menu
cls
echo =========================
echo     FERRAMENTAS DO SISTEMA
echo =========================
echo 1 - Abrir Gestor de Tarefas
echo 2 - Abrir Painel de Controlo
echo 3 - Abrir Explorador
echo 4 - Abrir CMD
echo 5 - Sair
echo =========================
set /p opcao=Escolhe uma opcao: 

if "%opcao%"=="1" start taskmgr
if "%opcao%"=="2" start control
if "%opcao%"=="3" start explorer
if "%opcao%"=="4" start cmd
if "%opcao%"=="5" goto fim

goto menu

:fim
echo Ate logo!
pause
exit