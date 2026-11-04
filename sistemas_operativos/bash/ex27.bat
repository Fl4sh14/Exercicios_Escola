set /p pasta = Indique a pasta
mkdir texto
mkdir fotos
mkdir relatórios

for /f %%file in (pasta\ *.txt) do (
    mv %%file texto
)
