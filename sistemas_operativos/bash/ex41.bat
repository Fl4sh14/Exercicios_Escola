@echo off

for /L %%i in (1,1,20) do (
    echo %time%
    timeout /t 1 >nul
)
