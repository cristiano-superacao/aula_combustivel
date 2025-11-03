# ====================================================================
# SCRIPT POWERSHELL - ATUALIZAR GITHUB AUTOMATICAMENTE
# ====================================================================
# Script automatizado para enviar o frontend para o GitHub
# Desenvolvido para: SENAI 2025

param(
    [string]$Email = "cristiano.s.santos@ba.estudante.senai.br",
    [string]$Nome = "Cristiano Santos",
    [string]$Repo = "https://github.com/cristiano-superacao/aula_combustivel.git"
)

# Cores para output
$ErrorActionPreference = "Continue"

function Write-ColorOutput($ForegroundColor) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    if ($args) {
        Write-Output $args
    }
    $host.UI.RawUI.ForegroundColor = $fc
}

function Write-Success { Write-ColorOutput Green $args }
function Write-Info { Write-ColorOutput Cyan $args }
function Write-Warning { Write-ColorOutput Yellow $args }
function Write-Error { Write-ColorOutput Red $args }

Clear-Host
Write-Host ""
Write-Host "====================================================================" -ForegroundColor Blue
Write-Host " 🚀 ATUALIZADOR AUTOMÁTICO DO GITHUB - SISTEMA POSTO COMBUSTÍVEL" -ForegroundColor Blue
Write-Host "====================================================================" -ForegroundColor Blue
Write-Host ""

# Verificar se estamos na pasta correta
if (!(Test-Path "menu.py")) {
    Write-Error "❌ ERRO: Execute este script na pasta do projeto (onde está o menu.py)"
    Write-Info "💡 Navegue para a pasta correta e execute novamente"
    Read-Host "Pressione ENTER para sair"
    exit 1
}

Write-Success "✅ Pasta do projeto encontrada"

# Verificar se git está instalado
try {
    $gitVersion = git --version 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Success "✅ Git encontrado: $gitVersion"
    } else {
        throw "Git não encontrado"
    }
} catch {
    Write-Error "❌ Git não está instalado!"
    Write-Info "📥 Instale o Git: https://git-scm.com/download/win"
    Read-Host "Pressione ENTER para sair"
    exit 1
}

Write-Info "🔧 Configurando Git..."

# Configurar usuário Git
try {
    git config --global user.email $Email
    git config --global user.name $Nome
    Write-Success "✅ Usuário Git configurado: $Nome <$Email>"
} catch {
    Write-Error "❌ Erro ao configurar usuário Git"
    exit 1
}

# Verificar se já é um repositório Git
if (!(Test-Path ".git")) {
    Write-Info "📁 Inicializando repositório Git..."
    git init
    if ($LASTEXITCODE -eq 0) {
        Write-Success "✅ Repositório inicializado"
    } else {
        Write-Error "❌ Erro ao inicializar repositório"
        exit 1
    }
} else {
    Write-Success "✅ Repositório Git já existe"
}

# Verificar/adicionar remote origin
$currentRemote = git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Info "🔗 Adicionando remote origin..."
    git remote add origin $Repo
    if ($LASTEXITCODE -eq 0) {
        Write-Success "✅ Remote adicionado: $Repo"
    } else {
        Write-Error "❌ Erro ao adicionar remote"
        exit 1
    }
} else {
    Write-Success "✅ Remote já configurado: $currentRemote"
    
    # Atualizar remote se diferente
    if ($currentRemote -ne $Repo) {
        Write-Info "🔄 Atualizando remote..."
        git remote set-url origin $Repo
    }
}

# Criar arquivo .gitignore se não existir
if (!(Test-Path ".gitignore")) {
    Write-Info "📝 Criando .gitignore..."
    @"
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
desktop.ini

# Logs
*.log
logs/

# Temporary files
*.tmp
*.temp
"@ | Out-File -FilePath ".gitignore" -Encoding UTF8
    Write-Success "✅ .gitignore criado"
}

# Verificar status atual
Write-Info "📊 Verificando status do repositório..."
$status = git status --porcelain
if ($status) {
    Write-Info "📝 Arquivos modificados detectados:"
    git status --short
} else {
    Write-Warning "⚠️  Nenhuma modificação detectada"
}

Write-Host ""
Write-Info "🤔 Deseja continuar com o commit e push? (S/n)"
$resposta = Read-Host
if ($resposta -eq 'n' -or $resposta -eq 'N') {
    Write-Warning "⏹️  Operação cancelada pelo usuário"
    exit 0
}

# Adicionar todos os arquivos
Write-Info "📦 Adicionando arquivos..."
git add .
if ($LASTEXITCODE -eq 0) {
    Write-Success "✅ Arquivos adicionados ao stage"
} else {
    Write-Error "❌ Erro ao adicionar arquivos"
    exit 1
}

# Fazer commit
Write-Info "💾 Fazendo commit..."
$commitMessage = @"
✨ Frontend web responsivo e profissional - SENAI 2025

🌟 Principais funcionalidades:
• Interface web moderna e responsiva (HTML5 + CSS3 + JS)
• API REST Flask integrada com código Python original
• PWA (Progressive Web App) instalável
• Dashboard com estatísticas em tempo real
• Formulários com validação e cálculo automático
• Gestão completa de combustíveis via web
• Tema claro/escuro com alternância automática
• Design mobile-first totalmente responsivo
• Sistema offline com Service Worker
• Histórico local com Local Storage

🔧 Recursos técnicos:
• API REST com 7 endpoints
• SPA (Single Page Application) 
• Cache inteligente offline
• Comprovantes digitais para impressão
• Notificações toast para feedback
• Scripts de execução automatizados
• Documentação completa atualizada

🚀 Como executar:
Windows: iniciar_sistema.bat
Linux/macOS: iniciar_sistema.sh
Web: http://localhost:5000

✅ Sistema completo mantendo código Python original intacto
📱 Funciona perfeitamente em desktop, tablet e mobile
💾 Instalável como aplicativo (PWA)

Desenvolvido para: Curso de Lógica de Programação - SENAI 2025
"@

git commit -m $commitMessage
if ($LASTEXITCODE -eq 0) {
    Write-Success "✅ Commit realizado com sucesso"
} else {
    Write-Error "❌ Erro ao fazer commit"
    exit 1
}

# Verificar branch atual
$currentBranch = git branch --show-current
Write-Info "🌿 Branch atual: $currentBranch"

# Fazer push
Write-Info "🚀 Enviando para GitHub..."
Write-Warning "⚠️  Você precisará inserir suas credenciais do GitHub"
Write-Info "📧 Email: $Email"
Write-Info "🔑 Use sua senha ou token de acesso pessoal"
Write-Host ""

git push -u origin $currentBranch
if ($LASTEXITCODE -eq 0) {
    Write-Success "🎉 SUCESSO! Projeto enviado para GitHub!"
    Write-Host ""
    Write-Info "🔗 Acesse: https://github.com/cristiano-superacao/aula_combustivel"
    Write-Info "📱 Seu frontend estará disponível em: GitHub Pages (se configurado)"
} else {
    Write-Error "❌ Erro ao fazer push"
    Write-Host ""
    Write-Info "💡 Possíveis soluções:"
    Write-Info "   • Verifique suas credenciais"
    Write-Info "   • Use token de acesso em vez de senha"
    Write-Info "   • Configure autenticação SSH"
    Write-Info "   • Verifique se o repositório existe no GitHub"
}

Write-Host ""
Write-Host "====================================================================" -ForegroundColor Blue
Write-Info "📚 Próximos passos recomendados:"
Write-Info "   1. Configure GitHub Pages para hospedar o frontend"
Write-Info "   2. Habilite 2FA (Two-Factor Authentication) no GitHub"
Write-Info "   3. Considere usar SSH para futuras atualizações"
Write-Info "   4. Documente o processo para sua equipe"
Write-Host "====================================================================" -ForegroundColor Blue

Write-Host ""
Read-Host "Pressione ENTER para finalizar"