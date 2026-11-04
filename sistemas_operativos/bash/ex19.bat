@echo off

set count=0

for %%f in (*) do (
    set /a count+=1
)

echo Total de ficheiros: %count%
pause