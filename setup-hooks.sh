#!/bin/bash

# Copia os hooks para o repositório

if [ ! -d ".git/hooks" ]; then
    echo "Erro: diretório .git/hooks não encontrado. Criando..."
    mkdir -p .git/hooks
fi

if [ ! -f "scripts/pre-push" ]; then
    echo "Erro: arquivo scripts/pre-push não encontrado."
    exit 1
fi

# Copia os hooks para o repositório
install -m 755 scripts/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push