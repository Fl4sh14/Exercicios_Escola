#!/bin/bash
echo 'Ola, Mundo!'

read -p "Nome: " nome
echo "Bem-vindo, $nome!"

#!/bin/bash
read -p "Numero 1: " a
read -p "Numero 2: " b
echo "Soma: $(( a + b ))"

#!/bin/bash
read -p "Numero: " n
(( n % 2 == 0 )) && echo "Par" || echo "Impar"

#!/bin/bash
read -p "Numero 1: " a
read -p "Numero 2: " b
read -p "Numero 3: " c
maior=$a
(( b > maior )) && maior=$b
(( c > maior )) && maior=$c
echo "Maior: $maior"

#!/bin/bash
read -p "N: " n
for (( i=n; i>=0; i-- )); do echo $i; done
echo "Lancamento!"

#!/bin/bash
read -p "Numero: " n
for (( i=1; i<=10; i++ )); do echo "$n x $i = $(( n * i ))"; done

#!/bin/bash
[ -f "$1" ] && echo "Ficheiro existe" || echo "Ficheiro nao existe"

#!/bin/bash
for f in *.txt; do mv "$f" "old_$f"; done

#!/bin/bash
echo "Data: $(date +"%d/%m/%Y")"
echo "Hora: $(date +"%H:%M:%S")"
echo "Utilizador: $USER"

#!/bin/bash

read -p 'Numero 1: ' a
read -p 'Numero 2: ' b
read -p 'Operacao (+,-,*,/): ' op

case $op in
  + echo 'Resultado: $(( a + b ))' ;;
  - echo 'Resultado: $(( a - b ))' ;;
  \* echo 'Resultado: $(( a * b ))' ;;
  /
    [ $b -eq 0 ] && echo 'Erro: divisao por zero' || echo 'Resultado: $(echo 'scale=2; $a / $b' | bc)'
    ;;
  * echo 'Operacao invalida' ;;
esac

#!/bin/bash
read -p "Numero: " n
[ $n -lt 0 ] && echo "Erro: numero negativo" && exit 1
fat=1
for (( i=2; i<=n; i++ )); do fat=$(( fat * i )); done
echo "Fatorial: $fat"

#!/bin/bash
read -p "Termos: " n
a=0; b=1
for (( i=0; i<n; i++ )); do printf "$a "; temp=$(( a + b )); a=$b; b=$temp; done
echo

#!/bin/bash
read -p "Palavra: " p
[ "$p" == "$(echo "$p" | rev)" ] && echo "E palindromo" || echo "Nao e palindromo"

#!/bin/bash
pasta="$1"
tar -czf "${pasta}_$(date +%F).tar.gz" "$pasta"
echo "Backup criado: ${pasta}_$(date +%F).tar.gz"

#!/bin/bash
while true; do echo "1) Ver data  2) Listar ficheiros  3) Ver utilizador  4) Sair"; read -p "Opcao: " op; case $op in 1) date ;; 2) ls ;; 3) echo $USER ;; 4) break ;; *) echo "Opcao invalida" ;; esac; done

#!/bin/bash
echo "Linhas: $(wc -l < "$1")"
echo "Palavras: $(wc -w < "$1")"
echo "Caracteres: $(wc -c < "$1")"

#!/bin/bash
echo "Ocorrencias: $(grep -o "$1" "$2" | wc -l)"

#!/bin/bash
if systemctl is-active --quiet "$1"; then echo "Servico '$1' esta ativo"; else echo "Servico '$1' esta inativo. Para iniciar: sudo systemctl start $1"; fi

#!/bin/bash
echo "$(date '+%d/%m/%Y %H:%M:%S') - $USER" >> log.txt
tail -5 log.txt

#!/bin/bash
rsync -av "$1/" "$2/"

#!/bin/bash
ficheiro="$1"
while IFS=',' read -r col1 col2 col3; do echo "Campo1: $col1 | Campo2: $col2 | Campo3: $col3"; done < "$ficheiro"

#!/bin/bash
while true; do echo "1) Criar utilizador  2) Eliminar utilizador  3) Listar utilizadores  4) Sair"; read -p "Opcao: " op; case $op in 1) read -p "Nome: " u; sudo useradd -m "$u" && echo "Criado" ;; 2) read -p "Nome: " u; sudo userdel -r "$u" && echo "Eliminado" ;; 3) grep '/bin/bash' /etc/passwd | cut -d: -f1 ;; 4) break ;; *) echo "Opcao invalida" ;; esac; done

#!/bin/bash
mkdir -p entrada processados
while true; do for f in entrada/*.txt; do [ -f "$f" ] || continue; mv "$f" processados/; echo "$(date '+%d/%m/%Y %H:%M:%S') - Movido: $(basename "$f")" >> log.txt; done; sleep 5; done

