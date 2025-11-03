"""
SISTEMA DE CONTROLE DE ABASTECIMENTO
====================================
MENU PRINCIPAL E INTERFACE DO USUÁRIO

Este arquivo contém o menu principal do sistema e coordena
a interação entre todos os módulos, apresentando uma
interface amigável e intuitiva para o usuário final.

Desenvolvido para: Curso de Lógica de Programação - SENAI 2025
Arquitetura: Sistema modular com separação de responsabilidades

MÓDULOS INTEGRADOS:
- combustivel.py: Gerencia tipos e preços de combustível  
- pagamento.py: Controla formas de pagamento e descontos
- abastecimento.py: Processa cálculos e gera registros

FUNCIONALIDADES PRINCIPAIS:
- Menu interativo com navegação numérica
- Gestão completa de abastecimentos
- Administração de combustíveis e preços
- Informações sobre descontos e pagamentos
"""

# IMPORTAÇÕES DO SISTEMA OPERACIONAL
import os   # Para limpar tela (cls no Windows, clear no Linux)

# IMPORTAÇÕES DOS MÓDULOS CUSTOMIZADOS
import combustivel   # Módulo para gerenciar combustíveis
import pagamento     # Módulo para formas de pagamento
import abastecimento  # Módulo principal de processamento


def limpar_tela():
    """
    Limpa a tela do terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """
    Exibe o cabeçalho do sistema
    """
    print("="*60)
    print(" " * 15 + "POSTO DE COMBUSTÍVEL")
    print(" " * 10 + "Sistema de Controle de Abastecimento")
    print("="*60)

def exibir_menu_principal():
    """
    Exibe o menu principal do sistema
    """
    print("\n" + "="*40)
    print("           MENU PRINCIPAL")
    print("="*40)
    print("1. Realizar Abastecimento")
    print("2. Gerenciar Combustíveis")
    print("3. Informações de Pagamento")
    print("4. Sobre o Sistema")
    print("0. Sair")
    print("="*40)

def menu_gerenciar_combustiveis():
    """
    Menu para gerenciar combustíveis
    """
    while True:
        print("\n" + "="*40)
        print("      GERENCIAR COMBUSTÍVEIS")
        print("="*40)
        print("1. Listar Combustíveis")
        print("2. Cadastrar Novo Combustível")
        print("3. Atualizar Preço")
        print("0. Voltar ao Menu Principal")
        print("="*40)
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 0:
                break
            elif opcao == 1:
                listar_combustiveis()
            elif opcao == 2:
                cadastrar_novo_combustivel()
            elif opcao == 3:
                atualizar_preco_combustivel()
            else:
                print("Opção inválida!")
                
        except ValueError:
            print("Por favor, digite um número válido!")
        
        input("\nPressione ENTER para continuar...")

def listar_combustiveis():
    """
    Lista todos os combustíveis cadastrados
    """
    combustiveis_list = combustivel.listar_combustiveis()
    
    print("\n" + "="*50)
    print("        COMBUSTÍVEIS CADASTRADOS")
    print("="*50)
    
    if combustiveis_list:
        for nome, preco in combustiveis_list.items():
            print(f"{nome:<25} R$ {preco:>8.2f}/L")
    else:
        print("Nenhum combustível cadastrado.")
    
    print("="*50)

def cadastrar_novo_combustivel():
    """
    Cadastra um novo tipo de combustível
    """
    print("\n=== CADASTRAR NOVO COMBUSTÍVEL ===")
    
    nome = input("Nome do combustível: ").strip()
    if not nome:
        print("Nome não pode estar vazio!")
        return
    
    try:
        preco = float(input("Preço por litro (R$): "))
        if preco <= 0:
            print("O preço deve ser maior que zero!")
            return
        
        if combustivel.cadastrar_combustivel(nome, preco):
            print(f"Combustível '{nome}' cadastrado com sucesso!")
        else:
            print("Erro ao cadastrar combustível!")
            
    except ValueError:
        print("Preço inválido! Digite um número válido.")

def atualizar_preco_combustivel():
    """
    Atualiza o preço de um combustível existente
    """
    print("\n=== ATUALIZAR PREÇO DE COMBUSTÍVEL ===")
    
    # Listar combustíveis primeiro
    listar_combustiveis()
    
    nome = input("\nNome do combustível para atualizar: ").strip()
    if not combustivel.validar_combustivel(nome):
        print("Combustível não encontrado!")
        return
    
    preco_atual = combustivel.obter_preco_combustivel(nome)
    print(f"Preço atual: R$ {preco_atual:.2f}/L")
    
    try:
        novo_preco = float(input("Novo preço por litro (R$): "))
        if novo_preco <= 0:
            print("O preço deve ser maior que zero!")
            return
        
        if combustivel.atualizar_preco_combustivel(nome, novo_preco):
            print(f"Preço do {nome} atualizado para R$ {novo_preco:.2f}/L")
        else:
            print("Erro ao atualizar preço!")
            
    except ValueError:
        print("Preço inválido! Digite um número válido.")

def menu_informacoes_pagamento():
    """
    Exibe informações sobre formas de pagamento
    """
    print("\n" + "="*50)
    print("        INFORMAÇÕES DE PAGAMENTO")
    print("="*50)
    
    formas = pagamento.listar_formas_pagamento()
    
    print("\nFormas de pagamento disponíveis:")
    print("-" * 30)
    
    for codigo, nome in formas.items():
        info_desconto = pagamento.obter_info_desconto(nome)
        if info_desconto["tem_desconto"]:
            print(f"• {nome} - Desconto de {info_desconto['percentual_exibicao']}")
        else:
            print(f"• {nome} - Sem desconto")
    
    print("\n" + "="*50)
    print("ATENÇÃO: O desconto de 10% é aplicado automaticamente")
    print("para pagamentos em Dinheiro, PIX e Cartão de Débito.")
    print("="*50)
    
    input("\nPressione ENTER para voltar...")

def realizar_abastecimento():
    """
    FUNÇÃO PRINCIPAL: Processar um abastecimento completo
    ====================================================
    Esta função coordena todo o fluxo de um abastecimento:
    1. Coleta dados do usuário (combustível, litros, pagamento)
    2. Valida as informações inseridas  
    3. Processa os cálculos (valor bruto, desconto, final)
    4. Exibe o resumo formatado como comprovante
    
    Integração entre módulos:
    - abastecimento: coleta dados e processa
    - combustivel: valida tipo e busca preços
    - pagamento: calcula descontos
    
    Fluxo de trabalho completo demonstrando modularização.
    """
    try:
        # ETAPA 1: COLETA DE DADOS
        # Chama função do módulo abastecimento para coletar:
        # - Tipo de combustível (menu interativo)
        # - Quantidade de litros (input numérico)  
        # - Forma de pagamento (menu interativo)
        tipo_combustivel, quantidade_litros, forma_pagamento = abastecimento.obter_dados_abastecimento()
        
        # VERIFICAÇÃO DE CANCELAMENTO
        if not tipo_combustivel:  # Se usuário cancelou ou erro
            print("Abastecimento cancelado.")
            return
        
        # ETAPA 2: VALIDAÇÃO DOS DADOS
        # Verifica se todos os dados estão corretos antes de processar
        valido, mensagem = abastecimento.validar_dados_abastecimento(
            tipo_combustivel, quantidade_litros, forma_pagamento
        )
        
        # Se dados inválidos, exibe erro e cancela
        if not valido:
            print(f"Erro: {mensagem}")
            return
        
        # ETAPA 3: PROCESSAMENTO DO ABASTECIMENTO  
        # Cria objeto RegistroAbastecimento com todos os cálculos
        registro = abastecimento.processar_abastecimento(
            tipo_combustivel, quantidade_litros, forma_pagamento
        )
        
        # ETAPA 4: EXIBIÇÃO DO COMPROVANTE
        # Mostra resumo detalhado formatado para o cliente
        abastecimento.exibir_resumo_abastecimento(registro)
        
        # CONFIRMAÇÃO FINAL
        print("\nAbastecimento realizado com sucesso!")
        
    except ValueError as e:
        # Trata erros de validação (dados inválidos)
        print(f"Erro: {e}")
    except Exception as e:
        # Trata qualquer outro erro inesperado
        print(f"Erro inesperado: {e}")

def exibir_sobre():
    """
    Exibe informações sobre o sistema
    """
    print("\n" + "="*60)
    print("              SOBRE O SISTEMA")
    print("="*60)
    print("Sistema de Controle de Abastecimento")
    print("Desenvolvido para o curso de Lógica de Programação")
    print("SENAI 2025")
    print()
    print("Funcionalidades:")
    print("• Cadastro e gerenciamento de combustíveis")
    print("• Múltiplas formas de pagamento")
    print("• Aplicação automática de descontos")
    print("• Cálculo detalhado do abastecimento")
    print()
    print("Módulos:")
    print("• combustivel.py - Gerenciamento de combustíveis")
    print("• pagamento.py - Formas de pagamento e descontos")
    print("• abastecimento.py - Cálculos e processamento")
    print("• main.py - Interface principal")
    print("="*60)
    
    input("\nPressione ENTER para voltar...")

def main():
    """
    FUNÇÃO PRINCIPAL DO SISTEMA (LOOP PRINCIPAL)
    ===========================================
    Esta é a função que controla todo o fluxo do programa.
    Implementa um loop infinito que só termina quando o usuário escolhe sair.
    
    Conceitos demonstrados:
    - Loop while infinito (while True)
    - Estrutura de menu com switch-case (if/elif)
    - Tratamento de exceções (try/except)
    - Controle de fluxo e navegação
    
    Padrão de design: Menu principal com sub-menus
    """
    # LOOP PRINCIPAL DO SISTEMA
    while True:  # Loop infinito - só para quando usuário escolher sair
        try:
            # PREPARAR INTERFACE
            limpar_tela()          # Limpa terminal para melhor visual
            exibir_cabecalho()     # Mostra título do sistema
            exibir_menu_principal() # Exibe opções disponíveis
            
            # CAPTURAR ESCOLHA DO USUÁRIO
            opcao = int(input("Escolha uma opção: "))
            
            # ESTRUTURA DE DECISÃO (SWITCH-CASE SIMULADO)
            if opcao == 0:
                # OPÇÃO DE SAÍDA - quebra o loop principal
                print("\nObrigado por usar o Sistema de Controle de Abastecimento!")
                print("Sistema desenvolvido para SENAI 2025")
                break  # Sai do while True
                
            elif opcao == 1:
                # FUNCIONALIDADE PRINCIPAL - Realizar abastecimento
                realizar_abastecimento()
                
            elif opcao == 2:
                # MENU ADMINISTRATIVO - Gerenciar combustíveis  
                menu_gerenciar_combustiveis()
                
            elif opcao == 3:
                # INFORMAÇÕES - Consultar formas de pagamento
                menu_informacoes_pagamento()
                
            elif opcao == 4:
                # AJUDA - Sobre o sistema
                exibir_sobre()
                
            else:
                # OPÇÃO INVÁLIDA - número fora do range
                print("Opção inválida! Escolha uma opção de 0 a 4.")
            
            # PAUSA PARA LEITURA (exceto se saindo)
            if opcao != 0:
                input("\nPressione ENTER para continuar...")
                
        # TRATAMENTO DE EXCEÇÕES
        except ValueError:
            # Erro quando usuário digita texto em vez de número
            print("Por favor, digite um número válido!")
            input("\nPressione ENTER para continuar...")
            
        except KeyboardInterrupt:
            # Ctrl+C pressionado - saída forçada
            print("\n\nSistema interrompido pelo usuário.")
            break
            
        except Exception as e:
            # Qualquer outro erro não previsto
            print(f"\nErro inesperado: {e}")
            input("\nPressione ENTER para continuar...")

# PONTO DE ENTRADA DO PROGRAMA
# Esta condição garante que main() só executa se o arquivo for rodado diretamente
# (não quando importado como módulo)
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o sistema