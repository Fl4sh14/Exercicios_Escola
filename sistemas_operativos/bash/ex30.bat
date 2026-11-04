@echo off

set /p n=Introduza o numero de copias: 

for /l %%i in (1,1,%n%) do (
    copy dados.txt dados_%%i.txt >nul
)

echo Copias criadas com sucesso!
pause
