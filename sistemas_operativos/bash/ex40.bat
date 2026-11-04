@echo off 

:inicio

if exist ficheiro.txt (
    echo o ficheiro existe
    exit 
)

timeout /t 3 > nul
goto inicio
