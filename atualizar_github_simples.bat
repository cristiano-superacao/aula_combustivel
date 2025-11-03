@echo off
REM ====================================================================
REM SCRIPT SIMPLES PARA ATUALIZAR GITHUB
REM ====================================================================
REM Versão simplificada para Windows

echo.
echo ====================================================================
echo  🚀 ATUALIZANDO GITHUB - SISTEMA POSTO DE COMBUSTÍVEL
echo ====================================================================
echo.

REM Verificar se estamos na pasta correta
if not exist "menu.py" (
    echo ❌ ERRO: Execute este script na pasta do projeto
    pause
    exit /b 1
)

echo ✅ Pasta do projeto encontrada
echo.

REM Configurar Git
echo 🔧 Configurando Git...
git config --global user.email "cristiano.s.santos@ba.estudante.senai.br"
git config --global user.name "Cristiano Santos"

REM Inicializar repositório se necessário
if not exist ".git" (
    echo 📁 Inicializando repositório...
    git init
)

REM Adicionar remote
git remote remove origin 2>nul
git remote add origin https://github.com/cristiano-superacao/aula_combustivel.git

echo.
echo 📦 Adicionando arquivos...
git add .

echo.
echo 💾 Fazendo commit...
git commit -m "✨ Adicionar frontend web responsivo e profissional - SENAI 2025"

echo.
echo 🚀 Enviando para GitHub...
echo ⚠️  ATENÇÃO: Você precisará inserir suas credenciais
echo.
git push -u origin main

if %errorlevel% neq 0 (
    echo.
    echo 🔄 Tentando branch master...
    git push -u origin master
)

echo.
echo 🎉 CONCLUÍDO!
echo 🔗 Acesse: https://github.com/cristiano-superacao/aula_combustivel
echo.
pause