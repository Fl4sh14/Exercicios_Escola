@echo off

for /L %%i in (1,1,100) do (
    if exist ficheiro%%i.txt echo ficheiro%%i.txt
)

pause
