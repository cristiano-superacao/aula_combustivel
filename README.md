# Sistema de Controle de Abastecimento

## Descrição
Sistema desenvolvido em Python para controle de abastecimento em postos de combustíveis, utilizando módulos separados para cada entidade e aplicação de funções para cálculo e desconto.

**Desenvolvido para:** Curso de Lógica de Programação - SENAI 2025

## Estrutura do Projeto

```
Posto_de_Combustivel/
├── menu.py              # Menu principal e fluxo do sistema
├── combustivel.py       # Cadastro e manipulação de tipos de combustível  
├── pagamento.py         # Formas de pagamento e verificação de desconto
├── abastecimento.py     # Cálculo do total e aplicação de desconto
├── teste_sistema.py     # Demonstração automatizada das funcionalidades
├── analise_conformidade.py # Verificação de conformidade com requisitos
└── README.md           # Documentação do projeto
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

## Como Executar

1. **Navegue até a pasta do projeto:**
   ```bash
   cd "D:\Senai 2025\exercicios\Modulo_1\Posto_de_Combustivel"
   ```

2. **Execute o sistema:**
   ```bash
   python menu.py
   ```

3. **Navegue pelo menu:**
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

## Desenvolvido por
**Curso de Lógica de Programação - SENAI 2025**

Sistema modular para demonstração de conceitos de:
- Modularização em Python
- Funções e procedimentos
- Estruturas de dados
- Programação orientada a objetos
- Tratamento de erros
- Interface de usuário em console