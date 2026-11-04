@echo off
setlocal enabledelayedexpansion

:: Pasta a percorrer
set "pasta=C:\Caminho\Da\Pasta"
set "relatorio=relatorio.txt"

> "%relatorio%" echo Relatorio de extensoes em %pasta%
>> "%relatorio%" echo ================================

set /a total=0

:: Percorrer ficheiros
for %%F in ("%pasta%\*.*") do (
    set "ext=%%~xF"
    if defined count_!ext! (
        set /a count_!ext!+=1
    ) else (
        set /a count_!ext!=1
    )
    set /a total+=1
)

:: Escrever relatorio
for /f "tokens=2 delims==" %%E in ('set count_') do (
    set "ext=%%E"
    set "val=!count_!ext!!"
    echo !ext! : !val! >> "%relatorio%"
)

echo ---------------- >> "%relatorio%"
echo Total de ficheiros: %total% >> "%relatorio%"

echo Relatorio gerado em %relatorio%
pause