# 🚗 Sistema de Controle de Abastecimento

## Descrição
Sistema completo para controle de abastecimento em postos de combustíveis, desenvolvido em Python com **frontend web responsivo e profissional**. O sistema possui:

- **Backend Python** com módulos separados para cada funcionalidade
- **Frontend Web** moderno e responsivo
- **API REST** para integração frontend/backend
- **PWA (Progressive Web App)** para uso mobile
- **Tema claro/escuro** e interface profissional

**Desenvolvido para:** Curso de Lógica de Programação - SENAI 2025

## 🏗️ Estrutura do Projeto

```
Posto_de_Combustivel/
├── 🐍 BACKEND PYTHON
│   ├── menu.py                 # Menu principal (console)
│   ├── combustivel.py          # Gestão de combustíveis
│   ├── pagamento.py           # Formas de pagamento e descontos
│   ├── abastecimento.py       # Processamento de abastecimentos
│   ├── teste_sistema.py       # Testes automatizados
│   └── analise_conformidade.py # Verificação de requisitos
│
├── 🌐 FRONTEND WEB
│   ├── frontend/
│   │   ├── templates/
│   │   │   └── index.html      # Interface principal
│   │   └── static/
│   │       ├── css/
│   │       │   └── style.css   # Estilos responsivos
│   │       ├── js/
│   │       │   └── app.js      # Aplicação JavaScript
│   │       ├── images/         # Ícones e imagens
│   │       ├── manifest.json   # PWA Manifest
│   │       └── sw.js          # Service Worker
│   │
├── 🔌 API REST
│   └── api/
│       └── app.py             # Servidor Flask
│
├── 📋 CONFIGURAÇÃO
│   ├── requirements.txt        # Dependências Python
│   ├── iniciar_sistema.bat    # Script Windows
│   ├── iniciar_sistema.sh     # Script Linux/macOS
│   └── README.md              # Esta documentação
```

## Módulos

### 📄 `combustivel.py`
- **Função:** Cadastro e manipulação de tipos de combustível
- **Recursos:**
  - Lista combustíveis cadastrados (Gasolina, Etanol, Diesel, etc.)
  - Cadastro de novos combustíveis
  - Atualização de preços
  - Validação de combustíveis

### 💳 `pagamento.py`
- **Função:** Formas de pagamento e verificação de desconto
- **Recursos:**
  - 4 formas de pagamento: Dinheiro, PIX, Cartão de Crédito, Cartão de Débito
  - Desconto automático de 10% para: Dinheiro, PIX e Cartão de Débito
  - Validação de formas de pagamento

### ⛽ `abastecimento.py`
- **Função:** Cálculo do total e aplicação de desconto
- **Recursos:**
  - Classe `RegistroAbastecimento` para controle completo
  - Cálculo automático: `valor_total = litros × valor_por_litro`
  - Aplicação automática de desconto quando aplicável
  - Validação completa dos dados

### 🖥️ `menu.py`
- **Função:** Menu principal e fluxo do sistema
- **Recursos:**
  - Interface intuitiva com menus organizados
  - Gerenciamento completo de combustíveis
  - Processamento de abastecimentos
  - Informações detalhadas sobre pagamentos

## Requisitos Atendidos

✅ **Cadastro de tipos de combustível:**
- Nome (Ex: Gasolina, Etanol, Diesel)
- Valor por litro (float)

✅ **Formas de pagamento:**
- Dinheiro (10% desconto)
- PIX (10% desconto)
- Cartão de Crédito
- Cartão de Débito (10% desconto)

✅ **Entrada de dados:**
- Tipo de combustível
- Quantidade em litros  
- Forma de pagamento

✅ **Cálculo do valor total:**
- `valor_total = litros × valor_por_litro`

✅ **Desconto automático de 10%** para:
- Dinheiro
- PIX
- Cartão de Débito

## 🚀 Como Executar

### 💻 Frontend Web (Recomendado)

**Windows:**
```cmd
# Clique duplo no arquivo ou execute no terminal:
iniciar_sistema.bat
```

**Linux/macOS:**
```bash
# Dar permissão de execução (primeira vez):
chmod +x iniciar_sistema.sh

# Executar:
./iniciar_sistema.sh
```

**Manual:**
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar servidor
cd api
python app.py
```

**Acesso:**
- 🌐 **Interface Web:** http://localhost:5000
- 📱 **Mobile:** Funciona perfeitamente em dispositivos móveis
- 💾 **PWA:** Pode ser instalado como app no celular/desktop

---

### 🖥️ Terminal/Console (Sistema Original)

```bash
python menu.py
```

**Navegação:**
- Use as opções numéricas para navegar
- Siga as instruções na tela  
- Digite `0` para sair de qualquer menu

## Exemplo de Uso

### Saída Esperada para um Abastecimento:

```
==================================================
--- REGISTRO DE ABASTECIMENTO ---
==================================================
Data/Hora: 24/10/2025 14:30:15
Tipo de Combustível: Gasolina
Valor por litro: R$ 5.79
Quantidade: 30.00 litros
Valor bruto: R$ 173.70
Forma de pagamento: PIX
Desconto aplicado (10%): R$ 17.37
--------------------------------------------------
TOTAL A PAGAR: R$ 156.33
==================================================
```

## Funcionalidades do Sistema

### Menu Principal
1. **Realizar Abastecimento** - Processa um novo abastecimento
2. **Gerenciar Combustíveis** - Cadastra, lista e atualiza combustíveis
3. **Informações de Pagamento** - Mostra formas de pagamento e descontos
4. **Sobre o Sistema** - Informações sobre o projeto
0. **Sair** - Encerra o sistema

### Validações Implementadas
- ✅ Combustível deve existir no sistema
- ✅ Quantidade de litros deve ser maior que zero
- ✅ Forma de pagamento deve ser válida
- ✅ Preços devem ser números válidos e positivos
- ✅ Tratamento de erros de entrada do usuário

## Características Técnicas

### Organização em Módulos
- **Separação de responsabilidades:** Cada módulo tem uma função específica
- **Reutilização de código:** Funções podem ser importadas e reutilizadas
- **Manutenibilidade:** Fácil de manter e expandir
- **Legibilidade:** Código bem documentado e organizado

### Programação Orientada a Objetos
- Classe `RegistroAbastecimento` para encapsular dados do abastecimento
- Métodos privados para cálculos internos
- Propriedades calculadas automaticamente

### Tratamento de Erros
- Validação de entrada do usuário
- Tratamento de exceções
- Mensagens de erro claras e específicas

## 🌟 Funcionalidades do Frontend Web

### 📊 Dashboard Interativo
- **Estatísticas em tempo real** dos combustíveis e formas de pagamento
- **Atividade recente** dos abastecimentos
- **Cards informativos** com design moderno
- **Ações rápidas** para navegação eficiente

### ⛽ Sistema de Abastecimento
- **Formulário intuitivo** com validação em tempo real
- **Cálculo automático** de valores conforme digitação
- **Preview dos valores** (bruto, desconto, total)
- **Comprovante digital** formatado para impressão
- **Histórico local** salvo no navegador

### 🛠️ Gestão de Combustíveis
- **Listagem visual** de todos os combustíveis
- **Cadastro simplificado** de novos tipos
- **Edição de preços** em tempo real
- **Integração total** com o sistema Python original

### 🎨 Interface Profissional
- **Design responsivo** (desktop, tablet, mobile)
- **Tema claro/escuro** com alternância automática
- **Animações suaves** e feedback visual
- **Ícones modernos** (Font Awesome)
- **Tipografia profissional** (Inter Font)

### 📱 PWA (Progressive Web App)
- **Instalação como app** no celular/desktop
- **Funcionamento offline** com Service Worker
- **Cache inteligente** de recursos
- **Notificações push** (preparado para futuro)
- **Atalhos rápidos** no menu do sistema

### 🔧 Recursos Técnicos
- **API REST** completa com endpoints documentados
- **SPA (Single Page Application)** sem recarregamentos
- **Local Storage** para persistência de dados
- **Validações client-side** e server-side
- **Tratamento de erros** robusto
- **Feedback visual** com toasts/notificações

---

## 🏭 Arquitetura do Sistema

### Backend (Python)
```
Módulos Originais → API Flask → Frontend Web
     ↓                 ↓           ↓
- combustivel.py   /api/combustiveis   Dashboard
- pagamento.py  →  /api/pagamentos  →  Formulários
- abastecimento.py /api/abastecimentos Gestão
```

### Frontend (Web)
```
HTML5 + CSS3 + JavaScript ES6+
         ↓
   Bootstrap-free Design
         ↓
   Progressive Web App
```

### Integração
- **Sem modificação** do código Python original
- **API wrapper** que expõe funcionalidades via HTTP
- **Frontend independente** que consome a API
- **Compatibilidade total** com sistema console

---

## 🎯 Tecnologias Utilizadas

### Backend
- **Python 3.8+**
- **Flask** (framework web)
- **Flask-CORS** (compartilhamento de recursos)

### Frontend
- **HTML5** semântico e acessível
- **CSS3** com Grid, Flexbox e Custom Properties
- **JavaScript ES6+** com classes e async/await
- **PWA** com Service Worker e Manifest
- **Font Awesome** para ícones
- **Inter Font** para tipografia

### Recursos Modernos
- **Responsive Design** mobile-first
- **Dark Mode** com preferência do sistema
- **Local Storage** para persistência
- **Fetch API** para requisições
- **CSS Animations** para transições suaves

---

## 📋 Requisitos do Sistema

### Mínimos
- **Python 3.8+** 
- **Navegador moderno** (Chrome 80+, Firefox 75+, Safari 13+, Edge 80+)
- **4 MB** de espaço em disco
- **Conexão de internet** (apenas para instalação inicial)

### Recomendados
- **Python 3.10+**
- **8 GB RAM**
- **Navegador atualizado**
- **SSD** para melhor performance

---

## 🚀 Desenvolvimento e Contribuição

### Estrutura para Desenvolvedores
```bash
# 1. Clonar/baixar projeto
git clone <repo> ou baixar ZIP

# 2. Instalar ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar em modo desenvolvimento
cd api
python app.py
# Servidor reinicia automaticamente ao modificar código
```

### APIs Disponíveis
```
GET  /api/status              # Status do sistema
GET  /api/combustiveis        # Listar combustíveis
POST /api/combustiveis        # Cadastrar combustível
PUT  /api/combustiveis/{nome} # Atualizar preço
GET  /api/pagamentos          # Listar formas pagamento
POST /api/abastecimentos      # Processar abastecimento
POST /api/calcular            # Calcular valores (preview)
```

### Personalização
- **CSS:** Modificar `/frontend/static/css/style.css`
- **JavaScript:** Editar `/frontend/static/js/app.js`
- **Cores:** Alterar CSS Custom Properties em `:root`
- **Logo:** Substituir ícones em `/frontend/static/images/`

---

## 🔒 Segurança e Produção

### Para Uso em Produção
```python
# api/app.py - Modificar para produção:
app.config['DEBUG'] = False
app.config['SECRET_KEY'] = 'sua-chave-secreta'

# Usar servidor WSGI (Gunicorn, uWSGI)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Melhorias de Segurança
- Adicionar **autenticação** (login/senha)
- Implementar **HTTPS** em produção  
- Configurar **CORS** específico
- Adicionar **rate limiting**
- Validar **inputs** mais rigorosamente

---

## 📚 Conceitos Demonstrados

### Programação Backend
- **Modularização** em Python
- **Programação Orientada a Objetos**
- **API REST** e arquitetura web
- **Tratamento de exceções**
- **Separação de responsabilidades**

### Desenvolvimento Frontend
- **Design responsivo** mobile-first
- **Progressive Web Apps (PWA)**
- **Single Page Applications (SPA)**
- **Integração API** com JavaScript
- **UX/UI** moderno e acessível

### Engenharia de Software  
- **Arquitetura limpa** (não modificar código original)
- **Versionamento** e documentação
- **Scripts de automação**
- **Cross-platform** (Windows, Linux, macOS)

---

## 🎓 Desenvolvido por
**Curso de Lógica de Programação - SENAI 2025**

Sistema completo demonstrando evolução de:
- Console → Web Interface
- Monolito → API + Frontend  
- Local → PWA Instalável
- Básico → Profissional