#!/bin/bash

# ==============================================================================
# MENSAGEM DE BOAS-VINDAS
# ==============================================================================
echo '=================================================='
echo '   Bem-vindo ao Organizador Automático de Pastas  '
echo '=================================================='
echo 'Este script vai organizar os ficheiros desta pasta por categorias.'
echo ''

# ==============================================================================
# DEFINIÇÃO DE VARIÁVEIS
# ==============================================================================
# Criamos uma lista com os tipos de extensões que queremos organizar
extensoes_texto=('txt' 'pdf' 'docx')
extensoes_imagem=('jpg' 'png' 'gif')

# Contadores para o relatório final
total_texto=0
total_imagem=0

# ==============================================================================
# CRIAÇÃO DAS SUBPASTAS (Se não existirem)
# ==============================================================================
# O operador '-d' verifica se a pasta já existe. Se não existir (!), cria-se com 'mkdir'.
if [ ! -d 'Documentos' ]; then
    mkdir 'Documentos'
    echo '[INFO] Pasta 'Documentos' criada com sucesso.'
fi

if [ ! -d 'Imagens' ]; then
    mkdir 'Imagens'
    echo '[INFO] Pasta 'Imagens' criada com sucesso.'
fi

# ==============================================================================
# PROCESSAMENTO E ORGANIZAÇÃO DOS FICHEIROS
# ==============================================================================
# Iniciamos um ciclo 'for' que vai ler todos os ficheiros da pasta atual (*)
for ficheiro in *; do

    # Verificamos se é um ficheiro real (e não uma pasta) para evitar mover diretorias
    if [ -f '$ficheiro' ]; then
        
        # Extraímos a extensão do ficheiro (ex: 'relatorio.txt' passa a 'txt')
        extensao='${ficheiro##*.}'

        # --- Bloco para Documentos de Texto ---
        # Verificamos se a extensão do ficheiro está na nossa lista de texto
        for ext in '${extensoes_texto[@]}'; do
            if [ '$extensao' == '$ext' ]; then
                mv '$ficheiro' 'Documentos/'
                echo '[SUCESSO] Movido: $ficheiro -> Documentos/'
                total_texto=$((total_texto + 1))
                break # Sai do ciclo interno pois o ficheiro já foi movido
            fi
        done

        # --- Bloco para Imagens ---
        # Verificamos se a extensão do ficheiro está na nossa lista de imagens
        for ext in '${extensoes_imagem[@]}'; do
            if [ '$extensao' == '$ext' ]; then
                mv '$ficheiro' 'Imagens/'
                echo '[SUCESSO] Movido: $ficheiro -> Imagens/'
                total_imagem=$((total_imagem + 1))
                break
            fi
        done

    fi
done

# ==============================================================================
# MENSAGEM DE SAÍDA E RESUMO
# ==============================================================================
echo ''
echo '=================================================='
echo '               Organização Concluída!             '
echo '=================================================='
echo 'Resumo das operações:'
echo '-> Ficheiros de texto movidos: $total_texto'
echo '-> Imagens movidas: $total_imagem'
echo 'Obrigado por usar o Organizador. Até à próxima!'
echo '=================================================='\
