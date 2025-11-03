# 📋 INSTRUÇÕES PARA ATUALIZAR GITHUB
# ====================================

## 🚀 MÉTODO 1: Script Automatizado (RECOMENDADO)

### PowerShell (Completo):
```powershell
# Abra PowerShell como Administrador na pasta do projeto
.\atualizar_github.ps1
```

### Batch (Simples):
```cmd
# Clique duplo ou execute no CMD
atualizar_github_simples.bat
```

---

## 🔐 IMPORTANTE: Credenciais GitHub

Quando solicitado, use:
- **Email:** cristiano.s.santos@ba.estudante.senai.br
- **Senha:** Sua senha do GitHub OU Token de Acesso

### 🛡️ Recomendação: Use Token em vez de Senha
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Selecione: `repo` (Full control of private repositories)
4. Use o token gerado no lugar da senha

---

## 📱 MÉTODO 2: GitHub Desktop (Interface Gráfica)

1. **Baixar:** https://desktop.github.com/
2. **Instalar** e fazer login
3. **File → Clone repository**
4. **URL:** `https://github.com/cristiano-superacao/aula_combustivel`
5. **Copiar** todos os arquivos novos para a pasta local
6. **Commit** e **Push** via interface

---

## 🌐 MÉTODO 3: GitHub Web (Upload Manual)

1. **Acesse:** https://github.com/cristiano-superacao/aula_combustivel
2. **Add file → Upload files**
3. **Arrastar pastas:** `frontend/`, `api/`
4. **Arrastar arquivos:** `requirements.txt`, `iniciar_sistema.*`, README.md atualizado
5. **Commit changes**

---

## 🔍 VERIFICAR SUCESSO

Após atualizar, acesse:
- **Repositório:** https://github.com/cristiano-superacao/aula_combustivel
- **Verificar** se as pastas `frontend` e `api` estão lá
- **README.md** deve mostrar a nova documentação

---

## ⚡ EXECUÇÃO RÁPIDA

```powershell
# 1. Abra PowerShell na pasta do projeto
cd "c:\Users\aluno.den\Downloads\Posto_de_Combustivel\Posto_de_Combustivel"

# 2. Execute o script (escolha um):
.\atualizar_github.ps1        # Versão completa
.\atualizar_github_simples.bat # Versão simples
```

---

## 🐛 PROBLEMAS COMUNS

### Erro: "Git não encontrado"
- **Solução:** Instalar Git: https://git-scm.com/download/win

### Erro: "Authentication failed" 
- **Solução:** Use token de acesso em vez de senha

### Erro: "Remote already exists"
- **Solução:** Normal, o script já trata isso

### Erro: "Branch main não existe"
- **Solução:** Script tenta automaticamente branch `master`

---

## 📞 SUPORTE

Se houver problemas:
1. Verifique se Git está instalado
2. Confirme credenciais do GitHub
3. Tente o método manual (GitHub Web)
4. Execute um script por vez (não os dois)

---

## 🎯 RESULTADO ESPERADO

Seu repositório terá:
```
aula_combustivel/
├── frontend/          # ← Interface web
├── api/              # ← Servidor Flask  
├── menu.py           # ← Sistema original
├── combustivel.py
├── pagamento.py
├── abastecimento.py
├── requirements.txt  # ← Dependências
├── iniciar_sistema.* # ← Scripts execução
└── README.md         # ← Documentação atualizada
```

🎉 **Frontend profissional integrado com sistema Python original!**