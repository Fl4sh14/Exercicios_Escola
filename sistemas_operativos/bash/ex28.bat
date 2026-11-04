@echo off
echo A juntar ficheiros...

del Agregado.txt 2>nul

for %%f in (*) do (
    if not "%%f"=="Agregado.txt" (
        type "%%f" >> Agregado.txt
        echo. >> Agregado.txt
    )
)

echo Concluído! Todos os ficheiros foram agregados em Agregado.txt
pause
