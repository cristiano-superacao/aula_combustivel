#!/bin/bash

# ====================================================================
# SCRIPT DE INICIALIZAÇÃO - SISTEMA DE POSTO DE COMBUSTÍVEL
# ====================================================================
# Script para Linux/macOS que instala dependências e inicia o sistema
# Desenvolvido para: SENAI 2025

echo ""
echo "===================================================================="
echo " 🚗 SISTEMA DE POSTO DE COMBUSTÍVEL - INICIALIZAÇÃO"
echo "===================================================================="
echo ""

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python não encontrado! Por favor, instale Python 3.8+ antes de continuar."
        echo "📥 Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip"
        echo "📥 macOS: brew install python3"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "✅ Python encontrado ($PYTHON_CMD)"
echo ""

# Verificar se pip está disponível
if ! command -v pip3 &> /dev/null; then
    if ! command -v pip &> /dev/null; then
        echo "❌ pip não encontrado! Instalando pip..."
        $PYTHON_CMD -m ensurepip --upgrade
    else
        PIP_CMD="pip"
    fi
else
    PIP_CMD="pip3"
fi

echo "✅ pip disponível ($PIP_CMD)"
echo ""

# Instalar dependências
echo "📦 Instalando dependências..."
$PIP_CMD install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Erro ao instalar dependências!"
    echo "💡 Tente executar: sudo $PIP_CMD install -r requirements.txt"
    exit 1
fi

echo ""
echo "✅ Dependências instaladas com sucesso!"
echo ""

# Iniciar o servidor
echo "🚀 Iniciando servidor web..."
echo ""
echo "📋 Sistema disponível em: http://localhost:5000"
echo "🛑 Para parar o sistema, pressione Ctrl+C"
echo ""

cd "$(dirname "$0")/api"
$PYTHON_CMD app.py