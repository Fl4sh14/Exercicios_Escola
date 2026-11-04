@echo off

set /p origem=Pasta origem: 
set /p destino=Pasta destino: 

copy "%origem%\*.txt" "%destino%"

echo Backup concluido.
pause