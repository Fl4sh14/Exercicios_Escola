@echo off

set pasta=backup_%date%_%time%
set pasta=%pasta:/=-%
set pasta=%pasta::=-%

mkdir "%pasta%"
copy *.txt "%pasta%"

echo Backup feito!
pause