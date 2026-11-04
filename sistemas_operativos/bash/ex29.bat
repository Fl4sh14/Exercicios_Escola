@echo off

set /p num=Quantas copias quer criar? 

for /l %%i in (1,1,%num%) do (
    copy dados.txt dados_%%i.txt
)

echo Copias criadas!
pause
