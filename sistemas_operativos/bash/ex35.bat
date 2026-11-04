@echo off
set txt=0
set jpg=0
set exe=0

for %%f in (*.txt) do set /a txt+=1
for %%f in (*.jpg) do set /a jpg+=1
for %%f in (*.exe) do set /a exe+=1

echo Ficheiros .txt: %txt%
echo Ficheiros .jpg: %jpg%
echo Ficheiros .exe: %exe%

pause
