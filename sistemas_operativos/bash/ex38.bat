@echo off
setlocal enabledelayedexpansion

set "tamanho=10"

for /L %%i in (0,1,10) do (
    cls
    set /a perc=%%i*10
    set "barra="
    
    for /L %%j in (1,1,%%i) do set "barra=!barra!#"
    for /L %%j in (1,1,%tamanho%-%%i) do set "barra=!barra!-"
    
    echo [!barra!] !perc!%%
    timeout /t 1 >nul
)

cls
echo [##########] 100%
echo Concluido!
pause