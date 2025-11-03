"""
MÓDULO COMBUSTÍVEL
==================
Este módulo é responsável pelo gerenciamento dos tipos de combustível disponíveis no posto.
Contém funções para cadastrar, listar, atualizar preços e validar combustíveis.

Funcionalidades principais:
- Cadastro de novos combustíveis
- Listagem de combustíveis disponíveis 
- Atualização de preços
- Validação de combustíveis
"""

# BANCO DE DADOS SIMPLES - Dicionário que simula uma base de dados
# Estrutura: {"nome_combustivel": preço_por_litro}
# Em um sistema real, isso seria substituído por um banco de dados
combustiveis_cadastrados = {
    "Gasolina": 5.79,              # Gasolina comum - preço padrão
    "Etanol": 3.89,                # Álcool etílico - mais barato
    "Diesel": 4.95,                # Diesel para caminhões/ônibus
    "Gasolina Aditivada": 6.15     # Gasolina premium - mais cara
}

def listar_combustiveis():
    """
    FUNÇÃO: Listar todos os combustíveis disponíveis
    ================================================
    Esta função retorna o dicionário completo com todos os combustíveis
    cadastrados e seus respectivos preços por litro.
    
    Utilizada em:
    - Exibição do menu de combustíveis para o cliente
    - Relatórios gerenciais
    - Validações internas do sistema
    
    Returns:
        dict: Dicionário com os combustíveis e seus preços
              Exemplo: {"Gasolina": 5.79, "Etanol": 3.89}
    """
    return combustiveis_cadastrados  # Retorna o dicionário completo

def obter_preco_combustivel(nome_combustivel):
    """
    Obtém o preço por litro de um combustível específico
    
    Args:
        nome_combustivel (str): Nome do combustível
    
    Returns:
        float: Preço por litro ou None se não encontrado
    """
    return combustiveis_cadastrados.get(nome_combustivel)

def cadastrar_combustivel(nome, preco_por_litro):
    """
    Cadastra um novo tipo de combustível
    
    Args:
        nome (str): Nome do combustível
        preco_por_litro (float): Preço por litro
    
    Returns:
        bool: True se cadastrado com sucesso
    """
    try:
        combustiveis_cadastrados[nome] = float(preco_por_litro)
        return True
    except (ValueError, TypeError):
        return False

def atualizar_preco_combustivel(nome, novo_preco):
    """
    Atualiza o preço de um combustível existente
    
    Args:
        nome (str): Nome do combustível
        novo_preco (float): Novo preço por litro
    
    Returns:
        bool: True se atualizado com sucesso
    """
    if nome in combustiveis_cadastrados:
        try:
            combustiveis_cadastrados[nome] = float(novo_preco)
            return True
        except (ValueError, TypeError):
            return False
    return False

def exibir_menu_combustiveis():
    """
    FUNÇÃO: Exibir menu interativo de combustíveis
    ==============================================
    Mostra todos os combustíveis disponíveis em formato de menu numerado
    e permite que o usuário faça uma seleção através de números.
    
    Fluxo da função:
    1. Busca todos os combustíveis cadastrados
    2. Exibe em formato numerado com preços
    3. Captura a escolha do usuário
    4. Valida a entrada
    5. Retorna o nome do combustível escolhido
    
    Returns:
        str: Nome do combustível selecionado ou None se entrada inválida
    """
    # PASSO 1: Buscar combustíveis cadastrados
    combustiveis = listar_combustiveis()
    
    # PASSO 2: Exibir cabeçalho do menu
    print("\n=== TIPOS DE COMBUSTÍVEL ===")
    
    # PASSO 3: Converter dicionário para lista para indexação numérica
    opcoes = list(combustiveis.keys())
    
    # PASSO 4: Exibir opções numeradas com preços formatados
    for i, combustivel in enumerate(opcoes, 1):  # enumerate começa do 1
        preco = combustiveis[combustivel]
        print(f"{i}. {combustivel} - R$ {preco:.2f}/L")  # Formatar com 2 casas decimais
    
    # PASSO 5: Capturar e validar entrada do usuário
    try:
        # Solicitar entrada numérica
        escolha = int(input(f"\nEscolha o tipo de combustível (1-{len(opcoes)}): "))
        
        # Validar se a escolha está dentro do range válido
        if 1 <= escolha <= len(opcoes):
            return opcoes[escolha - 1]  # Converter de 1-indexado para 0-indexado
        else:
            print("Opção inválida!")
            return None
            
    except ValueError:  # Captura erro se usuário digitar texto em vez de número
        print("Por favor, digite um número válido!")
        return None

def validar_combustivel(nome_combustivel):
    """
    Valida se o combustível existe no sistema
    
    Args:
        nome_combustivel (str): Nome do combustível
    
    Returns:
        bool: True se o combustível existe
    """
    return nome_combustivel in combustiveis_cadastrados