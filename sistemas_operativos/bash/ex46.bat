@echo off
set /p ficheiro="Introduz o nome do ficheiro (com extensao): "

if exist "%cd%\%ficheiro%" (
    echo O ficheiro "%ficheiro%" existe na pasta atual.
) else (
    echo O ficheiro "%ficheiro%" NAO existe na pasta atual.
)

pause
