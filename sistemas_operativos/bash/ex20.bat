@echo off
SETLOCAL ENABLEDELAYEDEXPANSION 
set i=1

for %%f in (*.txt) do (
    ren "%%f" ficheiro_!i!.txt
    set /a i+=1
)

pause
