@echo off
REM ====================================================================
REM SCRIPT DE INICIALIZAÇÃO - SISTEMA DE POSTO DE COMBUSTÍVEL
REM ====================================================================
REM Script para Windows que instala dependências e inicia o sistema
REM Desenvolvido para: SENAI 2025

echo.
echo ====================================================================
echo  🚗 SISTEMA DE POSTO DE COMBUSTÍVEL - INICIALIZAÇÃO
echo ====================================================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado! Por favor, instale Python 3.8+ antes de continuar.
    echo 📥 Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.

REM Verificar se pip está disponível
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip não encontrado! Instalando pip...
    python -m ensurepip --upgrade
)

echo ✅ pip disponível
echo.

REM Instalar dependências
echo 📦 Instalando dependências...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ❌ Erro ao instalar dependências!
    echo 💡 Tente executar como administrador ou verificar sua conexão de internet.
    pause
    exit /b 1
)

echo.
echo ✅ Dependências instaladas com sucesso!
echo.

REM Iniciar o servidor
echo 🚀 Iniciando servidor web...
echo.
echo 📋 Sistema disponível em: http://localhost:5000
echo 🛑 Para parar o sistema, pressione Ctrl+C
echo.

cd /d "%~dp0api"
python app.py

pause