@echo off

set "pastaA=C:\Caminho\Para\PastaA"
set "pastaB=C:\Caminho\Para\PastaB"

echo Ficheiros em A mas nao em B:
for %%F in ("%pastaA%\*") do (
    if not exist "%pastaB%\%%~nxF" echo %%~nxF
)

pause