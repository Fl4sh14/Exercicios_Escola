@echo off
set /p ficheiro=Nome do ficheiro: 
set /p destino=Pasta destino: 

copy "%ficheiro%" "%destino%"
echo Ficheiro copiado.
pause