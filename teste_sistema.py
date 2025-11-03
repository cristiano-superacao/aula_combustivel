#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ARQUIVO DE TESTE PARA DEMONSTRAÇÃO
==================================
Este arquivo demonstra como o sistema funciona de forma automatizada,
ideal para apresentação no curso sem precisar de interação manual.

Mostra todas as funcionalidades principais:
- Listagem de combustíveis
- Cálculos de abastecimento  
- Aplicação de descontos
- Diferentes formas de pagamento
"""

# Importar todos os módulos do sistema
import combustivel
import pagamento
import abastecimento

def linha_separadora(titulo=""):
    """Função auxiliar para criar separadores visuais"""
    print("\n" + "="*60)
    if titulo:
        print(f" {titulo.upper()} ".center(60))
        print("="*60)
    else:
        print("="*60)

def demonstrar_combustiveis():
    """Demonstra o módulo de combustíveis"""
    linha_separadora("MÓDULO COMBUSTÍVEL - DEMONSTRAÇÃO")
    
    print("1. LISTAGEM DE COMBUSTÍVEIS CADASTRADOS:")
    combustiveis_lista = combustivel.listar_combustiveis()
    
    for nome, preco in combustiveis_lista.items():
        print(f"   • {nome:<20} R$ {preco:>6.2f}/L")
    
    print(f"\n2. TOTAL DE COMBUSTÍVEIS: {len(combustiveis_lista)} tipos")
    
    print("\n3. EXEMPLO DE CONSULTA DE PREÇO:")
    preco_gasolina = combustivel.obter_preco_combustivel("Gasolina")
    print(f"   • Preço da Gasolina: R$ {preco_gasolina:.2f}/L")

def demonstrar_pagamentos():
    """Demonstra o módulo de pagamentos"""
    linha_separadora("MÓDULO PAGAMENTO - DEMONSTRAÇÃO")
    
    print("1. FORMAS DE PAGAMENTO DISPONÍVEIS:")
    formas = pagamento.listar_formas_pagamento()
    
    for codigo, nome in formas.items():
        tem_desconto = pagamento.tem_desconto(nome)
        status = "✓ COM DESCONTO (10%)" if tem_desconto else "✗ SEM DESCONTO"
        print(f"   {codigo}. {nome:<18} {status}")
    
    print("\n2. EXEMPLO DE CÁLCULO DE DESCONTO:")
    valor_teste = 100.00
    
    for _, forma in formas.items():
        desconto = pagamento.calcular_desconto(valor_teste, forma)
        print(f"   • {forma:<18} R$ {valor_teste:6.2f} → Desconto: R$ {desconto:5.2f}")

def demonstrar_abastecimento_completo():
    """Demonstra um abastecimento completo"""
    linha_separadora("ABASTECIMENTO COMPLETO - DEMONSTRAÇÃO")
    
    # Exemplo 1: Com desconto (PIX)
    print("EXEMPLO 1: GASOLINA COM PIX (COM DESCONTO)")
    print("-" * 50)
    
    try:
        registro1 = abastecimento.processar_abastecimento("Gasolina", 30.0, "PIX")
        
        print(f"Combustível: {registro1.tipo_combustivel}")
        print(f"Quantidade: {registro1.quantidade_litros:.1f} litros")
        print(f"Preço por litro: R$ {registro1.valor_por_litro:.2f}")
        print(f"Valor bruto: R$ {registro1.valor_bruto:.2f}")
        print(f"Forma de pagamento: {registro1.forma_pagamento}")
        print(f"Desconto (10%): R$ {registro1.valor_desconto:.2f}")
        print(f"VALOR FINAL: R$ {registro1.valor_final:.2f}")
        
    except Exception as e:
        print(f"Erro: {e}")
    
    print("\n" + "-" * 50)
    print("EXEMPLO 2: ETANOL COM CARTÃO DE CRÉDITO (SEM DESCONTO)")
    print("-" * 50)
    
    try:
        registro2 = abastecimento.processar_abastecimento("Etanol", 40.0, "Cartão de Crédito")
        
        print(f"Combustível: {registro2.tipo_combustivel}")
        print(f"Quantidade: {registro2.quantidade_litros:.1f} litros")
        print(f"Preço por litro: R$ {registro2.valor_por_litro:.2f}")
        print(f"Valor bruto: R$ {registro2.valor_bruto:.2f}")
        print(f"Forma de pagamento: {registro2.forma_pagamento}")
        print(f"Desconto: R$ {registro2.valor_desconto:.2f}")
        print(f"VALOR FINAL: R$ {registro2.valor_final:.2f}")
        
    except Exception as e:
        print(f"Erro: {e}")

def demonstrar_exemplo_requisito():
    """Demonstra exatamente como no exemplo do requisito"""
    linha_separadora("EXEMPLO CONFORME REQUISITO DO CURSO")
    
    try:
        # Criar o exemplo exato do requisito
        registro = abastecimento.processar_abastecimento("Gasolina", 30.0, "PIX")
        
        print("--- Registro de Abastecimento ---")
        print(f"Tipo de Combustível: {registro.tipo_combustivel}")
        print(f"Valor por litro: R$ {registro.valor_por_litro:.2f}")
        print(f"Quantidade: {registro.quantidade_litros:.0f} litros")
        print(f"Forma de pagamento: {registro.forma_pagamento}")
        print(f"Desconto aplicado: R$ {registro.valor_desconto:.2f}")
        print(f"Total a pagar: R$ {registro.valor_final:.2f}")
        
    except Exception as e:
        print(f"Erro: {e}")

def demonstrar_validacoes():
    """Demonstra o sistema de validações"""
    linha_separadora("SISTEMA DE VALIDAÇÕES - DEMONSTRAÇÃO")
    
    print("1. TESTANDO VALIDAÇÕES DE COMBUSTÍVEL:")
    
    # Teste válido
    valido = combustivel.validar_combustivel("Gasolina")
    print(f"   • 'Gasolina' é válido? {valido}")
    
    # Teste inválido  
    valido = combustivel.validar_combustivel("Combustível Inexistente")
    print(f"   • 'Combustível Inexistente' é válido? {valido}")
    
    print("\n2. TESTANDO VALIDAÇÕES DE PAGAMENTO:")
    
    # Teste válido
    valido = pagamento.validar_forma_pagamento("PIX")
    print(f"   • 'PIX' é válido? {valido}")
    
    # Teste inválido
    valido = pagamento.validar_forma_pagamento("Bitcoin")
    print(f"   • 'Bitcoin' é válido? {valido}")
    
    print("\n3. TESTANDO VALIDAÇÕES DE DADOS COMPLETOS:")
    
    # Teste válido
    valido, msg = abastecimento.validar_dados_abastecimento("Gasolina", 25.0, "Dinheiro")
    print(f"   • Dados válidos: {valido} - {msg}")
    
    # Teste inválido
    valido, msg = abastecimento.validar_dados_abastecimento("Inexistente", -5, "PayPal")
    print(f"   • Dados inválidos: {valido} - {msg}")

def main():
    """Função principal da demonstração"""
    print("SISTEMA DE CONTROLE DE ABASTECIMENTO")
    print("Desenvolvido para SENAI 2025 - Curso de Lógica")
    print("Demonstração Automática das Funcionalidades")
    
    # Executar todas as demonstrações
    demonstrar_combustiveis()
    demonstrar_pagamentos() 
    demonstrar_abastecimento_completo()
    demonstrar_exemplo_requisito()
    demonstrar_validacoes()
    
    linha_separadora("DEMONSTRAÇÃO CONCLUÍDA")
    print("Todos os módulos estão funcionando corretamente!")
    print("Sistema pronto para apresentação no curso.")
    print("\nPara usar o sistema interativo, execute: python menu.py")

if __name__ == "__main__":
    main()