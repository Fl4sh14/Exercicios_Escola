@echo off

set /p numero=Escreve um numero: 

if %numero% GTR 100 (
    echo Maior que 100
) else (
    echo 100 ou menos
)

pause