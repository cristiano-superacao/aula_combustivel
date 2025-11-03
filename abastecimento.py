"""
MÓDULO ABASTECIMENTO
====================
Este é o módulo central do sistema que processa e calcula os abastecimentos.
Integra os módulos de combustível e pagamento para realizar os cálculos finais.

Responsabilidades:
- Processar dados de abastecimento
- Calcular valores (bruto, desconto, final)
- Validar informações inseridas
- Gerar registros detalhados
- Exibir resumos formatados

Classes:
- RegistroAbastecimento: Representa um abastecimento completo

Funções principais:
- processar_abastecimento(): Processa um abastecimento completo
- calcular_valor_total(): Fórmula básica (litros × preço)
- exibir_resumo_abastecimento(): Mostra resultado formatado
"""

# IMPORTAÇÕES DOS MÓDULOS DO SISTEMA
import combustivel  # Para buscar preços e validar combustíveis
import pagamento    # Para calcular descontos e validar formas de pagamento
from datetime import datetime  # Para registrar data/hora do abastecimento

class RegistroAbastecimento:
    """
    CLASSE: Registro de Abastecimento
    =================================
    Esta classe representa um abastecimento completo no sistema.
    Ela encapsula todos os dados e cálculos relacionados a uma operação.
    
    Conceitos de POO (Programação Orientada a Objetos):
    - Encapsulamento: dados e métodos ficam juntos
    - Abstração: esconde a complexidade dos cálculos
    - Métodos privados: começam com _ (underscore)
    
    Atributos armazenados:
    - Dados de entrada (combustível, litros, pagamento)
    - Dados calculados (valores bruto, desconto, final)
    - Metadados (data/hora, preço por litro)
    """
    def __init__(self, tipo_combustivel, quantidade_litros, forma_pagamento):
        """
        CONSTRUTOR DA CLASSE
        ====================
        Inicializa um novo registro de abastecimento com todos os cálculos.
        Este método é chamado automaticamente quando criamos um objeto.
        """
        # DADOS BÁSICOS DO ABASTECIMENTO
        self.tipo_combustivel = tipo_combustivel      # Ex: "Gasolina"
        self.quantidade_litros = quantidade_litros    # Ex: 30.0
        self.forma_pagamento = forma_pagamento        # Ex: "PIX"
        
        # BUSCAR PREÇO ATUAL DO COMBUSTÍVEL NO MÓDULO COMBUSTÍVEL
        self.valor_por_litro = combustivel.obter_preco_combustivel(tipo_combustivel)
        
        # REGISTRAR TIMESTAMP DO ABASTECIMENTO
        self.data_abastecimento = datetime.now()
        
        # EXECUTAR TODOS OS CÁLCULOS AUTOMATICAMENTE
        self.valor_bruto = self._calcular_valor_bruto()      # Litros × Preço
        self.valor_desconto = self._calcular_desconto()      # Desconto aplicado
        self.valor_final = self._calcular_valor_final()      # Valor bruto - desconto
    
    def _calcular_valor_bruto(self):
        """
        MÉTODO PRIVADO: Calcular valor bruto
        ====================================
        Implementa a fórmula básica: Quantidade × Preço por litro
        
        Exemplo: 30 litros × R$ 5,79 = R$ 173,70
        
        Returns:
            float: Valor bruto antes de qualquer desconto
        """
        # VALIDAÇÃO: verificar se o preço foi encontrado
        if self.valor_por_litro is None:
            return 0.0
        
        # FÓRMULA PRINCIPAL: Quantidade × Preço unitário
        return self.quantidade_litros * self.valor_por_litro
    
    def _calcular_desconto(self):
        """
        MÉTODO PRIVADO: Calcular desconto
        =================================
        Utiliza o módulo de pagamento para calcular o desconto baseado
        na forma de pagamento escolhida.
        
        Integração entre módulos: abastecimento → pagamento
        
        Returns:
            float: Valor do desconto em reais
        """
        # DELEGAÇÃO: passar responsabilidade para o módulo pagamento
        return pagamento.calcular_desconto(self.valor_bruto, self.forma_pagamento)
    
    def _calcular_valor_final(self):
        """
        MÉTODO PRIVADO: Calcular valor final
        ====================================
        Aplica o desconto ao valor bruto para obter o valor que
        o cliente efetivamente pagará.
        
        Fórmula: Valor bruto - Desconto = Valor final
        
        Returns:
            float: Valor final que o cliente deve pagar
        """
        # SUBTRAÇÃO SIMPLES: valor bruto menos desconto
        return self.valor_bruto - self.valor_desconto

def calcular_valor_total(quantidade_litros, valor_por_litro):
    """
    FUNÇÃO UTILITÁRIA: Calcular valor total básico
    =============================================
    Esta é a fórmula fundamental de um posto: Litros × Preço
    
    Implementa tratamento de erro para entradas inválidas:
    - Converte strings para números
    - Retorna 0 se houver erro na conversão
    
    Exemplo de uso:
    calcular_valor_total(25.5, 5.79) = 147.645
    
    Args:
        quantidade_litros (float): Quantidade abastecida (ex: 25.5)
        valor_por_litro (float): Preço unitário (ex: 5.79)
    
    Returns:
        float: Valor total calculado ou 0.0 se erro
    """
    try:
        # CONVERSÃO SEGURA: garante que são números
        litros = float(quantidade_litros)
        preco = float(valor_por_litro)
        
        # FÓRMULA BÁSICA DE MULTIPLICAÇÃO
        return litros * preco
        
    except (ValueError, TypeError):
        # TRATAMENTO DE ERRO: retorna 0 se conversão falhar
        return 0.0

def processar_abastecimento(tipo_combustivel, quantidade_litros, forma_pagamento):
    """
    Processa um abastecimento completo
    
    Args:
        tipo_combustivel (str): Tipo do combustível
        quantidade_litros (float): Quantidade de litros
        forma_pagamento (str): Forma de pagamento
    
    Returns:
        RegistroAbastecimento: Objeto com todos os dados do abastecimento
    """
    # Validações
    if not combustivel.validar_combustivel(tipo_combustivel):
        raise ValueError(f"Combustível '{tipo_combustivel}' não encontrado!")
    
    if not pagamento.validar_forma_pagamento(forma_pagamento):
        raise ValueError(f"Forma de pagamento '{forma_pagamento}' inválida!")
    
    try:
        quantidade_litros = float(quantidade_litros)
        if quantidade_litros <= 0:
            raise ValueError("Quantidade de litros deve ser maior que zero!")
    except (ValueError, TypeError):
        raise ValueError("Quantidade de litros inválida!")
    
    # Criar e retornar o registro
    return RegistroAbastecimento(tipo_combustivel, quantidade_litros, forma_pagamento)

def exibir_resumo_abastecimento(registro):
    """
    Exibe o resumo detalhado do abastecimento
    
    Args:
        registro (RegistroAbastecimento): Registro do abastecimento
    """
    print("\n" + "="*50)
    print("--- REGISTRO DE ABASTECIMENTO ---")
    print("="*50)
    
    print(f"Data/Hora: {registro.data_abastecimento.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Tipo de Combustível: {registro.tipo_combustivel}")
    print(f"Valor por litro: R$ {registro.valor_por_litro:.2f}")
    print(f"Quantidade: {registro.quantidade_litros:.2f} litros")
    print(f"Valor bruto: R$ {registro.valor_bruto:.2f}")
    print(f"Forma de pagamento: {registro.forma_pagamento}")
    
    if registro.valor_desconto > 0:
        percentual = pagamento.obter_percentual_desconto() * 100
        print(f"Desconto aplicado ({percentual:.0f}%): R$ {registro.valor_desconto:.2f}")
    else:
        print("Desconto aplicado: R$ 0.00")
    
    print("-" * 50)
    print(f"TOTAL A PAGAR: R$ {registro.valor_final:.2f}")
    print("="*50)

def obter_dados_abastecimento():
    """
    Coleta os dados necessários para o abastecimento via input do usuário
    
    Returns:
        tuple: (tipo_combustivel, quantidade_litros, forma_pagamento) ou (None, None, None) se cancelado
    """
    print("\n=== NOVO ABASTECIMENTO ===")
    
    # Selecionar combustível
    tipo_combustivel = combustivel.exibir_menu_combustiveis()
    if not tipo_combustivel:
        return None, None, None
    
    # Obter quantidade de litros
    try:
        quantidade_litros = float(input("\nDigite a quantidade de litros: "))
        if quantidade_litros <= 0:
            print("A quantidade deve ser maior que zero!")
            return None, None, None
    except ValueError:
        print("Quantidade inválida! Digite um número válido.")
        return None, None, None
    
    # Selecionar forma de pagamento
    forma_pagamento = pagamento.exibir_menu_pagamento()
    if not forma_pagamento:
        return None, None, None
    
    return tipo_combustivel, quantidade_litros, forma_pagamento

def validar_dados_abastecimento(tipo_combustivel, quantidade_litros, forma_pagamento):
    """
    Valida os dados do abastecimento
    
    Args:
        tipo_combustivel (str): Tipo do combustível
        quantidade_litros (float): Quantidade de litros
        forma_pagamento (str): Forma de pagamento
    
    Returns:
        tuple: (bool, str) - (é_válido, mensagem_erro)
    """
    # Validar combustível
    if not combustivel.validar_combustivel(tipo_combustivel):
        return False, f"Combustível '{tipo_combustivel}' não está cadastrado!"
    
    # Validar quantidade
    try:
        quantidade = float(quantidade_litros)
        if quantidade <= 0:
            return False, "A quantidade de litros deve ser maior que zero!"
    except (ValueError, TypeError):
        return False, "Quantidade de litros inválida!"
    
    # Validar forma de pagamento
    if not pagamento.validar_forma_pagamento(forma_pagamento):
        return False, f"Forma de pagamento '{forma_pagamento}' não é válida!"
    
    return True, "Dados válidos"