"""
MÓDULO PAGAMENTO
================
Este módulo gerencia as formas de pagamento disponíveis no posto e 
implementa a lógica de aplicação de descontos automáticos.

Regras de negócio implementadas:
- 4 formas de pagamento disponíveis
- Desconto de 10% para: Dinheiro, PIX e Cartão de Débito
- Cartão de Crédito não recebe desconto (taxas da operadora)
"""

# CONSTANTES DO SISTEMA - Configurações das formas de pagamento
# Dicionário que mapeia códigos numéricos para nomes das formas de pagamento
# Facilita a criação de menus numerados para o usuário
FORMAS_PAGAMENTO = {
    1: "Dinheiro",           # Pagamento em espécie - recebe desconto
    2: "PIX",                # Transferência instantânea - recebe desconto  
    3: "Cartão de Crédito",  # Pagamento parcelado - SEM desconto
    4: "Cartão de Débito"    # Débito em conta - recebe desconto
}

# REGRA DE NEGÓCIO - Formas que recebem desconto
# Lista com as formas de pagamento que têm direito ao desconto promocional
# Critério: formas que não geram taxa para o posto
PAGAMENTO_COM_DESCONTO = ["Dinheiro", "PIX", "Cartão de Débito"]

# CONFIGURAÇÃO DE DESCONTO - Percentual aplicado
PERCENTUAL_DESCONTO = 0.10  # 10% de desconto (0.10 = 10/100)

def listar_formas_pagamento():
    """
    Lista todas as formas de pagamento disponíveis
    
    Returns:
        dict: Dicionário com as opções de pagamento
    """
    return FORMAS_PAGAMENTO

def tem_desconto(forma_pagamento):
    """
    Verifica se a forma de pagamento tem direito a desconto
    
    Args:
        forma_pagamento (str): Nome da forma de pagamento
    
    Returns:
        bool: True se tem desconto, False caso contrário
    """
    return forma_pagamento in PAGAMENTO_COM_DESCONTO

def calcular_desconto(valor_total, forma_pagamento):
    """
    FUNÇÃO PRINCIPAL: Calcular valor do desconto
    ===========================================
    Esta é a função central do módulo de pagamento. Ela implementa
    a lógica de negócio para calcular descontos automáticos.
    
    Lógica implementada:
    1. Verifica se a forma de pagamento tem direito a desconto
    2. Se sim: calcula 10% do valor total
    3. Se não: retorna 0 (zero desconto)
    
    Fórmula do desconto: valor_total × 0.10
    Exemplo: R$ 100,00 × 0.10 = R$ 10,00 de desconto
    
    Args:
        valor_total (float): Valor total antes do desconto (ex: 100.00)
        forma_pagamento (str): Nome da forma de pagamento (ex: "PIX")
    
    Returns:
        float: Valor em reais do desconto (ex: 10.00) ou 0.0 se sem desconto
    """
    # PASSO 1: Verificar se tem direito ao desconto
    if tem_desconto(forma_pagamento):
        # PASSO 2: Calcular 10% do valor total
        return valor_total * PERCENTUAL_DESCONTO
    
    # PASSO 3: Se não tem desconto, retorna zero
    return 0.0

def obter_percentual_desconto():
    """
    Obtém o percentual de desconto aplicado
    
    Returns:
        float: Percentual de desconto (0.10 para 10%)
    """
    return PERCENTUAL_DESCONTO

def exibir_menu_pagamento():
    """
    Exibe o menu de formas de pagamento e retorna a escolha do usuário
    
    Returns:
        str: Nome da forma de pagamento escolhida ou None se inválida
    """
    print("\n=== FORMAS DE PAGAMENTO ===")
    
    for codigo, nome in FORMAS_PAGAMENTO.items():
        desconto_info = " (10% de desconto)" if tem_desconto(nome) else ""
        print(f"{codigo}. {nome}{desconto_info}")
    
    try:
        escolha = int(input(f"\nEscolha a forma de pagamento (1-{len(FORMAS_PAGAMENTO)}): "))
        
        if escolha in FORMAS_PAGAMENTO:
            forma_escolhida = FORMAS_PAGAMENTO[escolha]
            return forma_escolhida
        else:
            print("Opção inválida!")
            return None
            
    except ValueError:
        print("Por favor, digite um número válido!")
        return None

def validar_forma_pagamento(forma_pagamento):
    """
    Valida se a forma de pagamento é válida
    
    Args:
        forma_pagamento (str): Nome da forma de pagamento
    
    Returns:
        bool: True se é válida, False caso contrário
    """
    return forma_pagamento in FORMAS_PAGAMENTO.values()

def obter_info_desconto(forma_pagamento):
    """
    Obtém informações sobre o desconto para uma forma de pagamento
    
    Args:
        forma_pagamento (str): Nome da forma de pagamento
    
    Returns:
        dict: Informações sobre desconto (tem_desconto, percentual)
    """
    return {
        "tem_desconto": tem_desconto(forma_pagamento),
        "percentual": PERCENTUAL_DESCONTO if tem_desconto(forma_pagamento) else 0.0,
        "percentual_exibicao": f"{int(PERCENTUAL_DESCONTO * 100)}%" if tem_desconto(forma_pagamento) else "0%"
    }