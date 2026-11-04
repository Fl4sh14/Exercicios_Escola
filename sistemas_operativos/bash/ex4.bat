@echo off
set /p idade=introduza a sua idade: 
if %idade% GEQ 18 (
    echo maior de idade
) else (
    echo menor de idade
)
pause
