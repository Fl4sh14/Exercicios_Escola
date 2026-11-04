@echo off
set contador=0

for /f "delims=" %%a in (ficheiro.txt) do (
    set /a contador+=1
    echo Linha !contador!: %%a
)

echo.
echo Total de linhas: %contador%
pause
