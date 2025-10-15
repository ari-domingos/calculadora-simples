# Calculadora Simples (4 operações)
import os
sistema = True

while sistema == True:
    os.system('clear')
    print('====================================')
    print('   CALCULADORA SIMPLES (2 VALORES)  ')
    print('====================================')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('\n0 - Sair')
    print('====================================')
    operacao = float(input('Escolha a operação que deseja: '))

    if operacao == 1:
        os.system('clear')
        print('========================')
        print('    CALCULADORA SOMA    ')
        print('========================')
        valorSomaUm = float(input('Digite o primeiro valor: '))
        valorSomaDois = float(input('Digite o segundo valor: '))
        calculoSoma = valorSomaUm + valorSomaDois
        print(f'A soma dos números {valorSomaUm:.2f} e {valorSomaDois:.2f} é: {calculoSoma:.2f}')
        print('--------------------------------------')
        input("Pressione ENTER para voltar ao menu...")
    elif operacao == 2:
        os.system('clear')
        print('=============================')
        print('    CALCULADORA SUBTRAÇÃO    ')
        print('=============================')
        valorSubtracaoUm = float(input('Digite o primeiro valor: '))
        valorSubtracaoDois = float(input('Digite o segundo valor: '))
        calculoSubtracao = valorSubtracaoUm - valorSubtracaoDois
        print(f'A subtração dos números {valorSubtracaoUm:.2f} e {valorSubtracaoDois:.2f} é: {calculoSubtracao:.2f}')
        print('--------------------------------------')
        input("Pressione ENTER para voltar ao menu...")
    elif operacao == 3:
        os.system('clear')        
        print('================================')
        print('    CALCULADORA MULTIPICAÇÃO    ')
        print('================================')
        valorMultipicacaoUm = float(input('Digite o primeiro valor: '))
        valorMultipicacaoDois = float(input('Digite o segundo valor: '))
        calculoMultiplicacao = valorMultipicacaoUm * valorMultipicacaoDois
        print(f'A multiplicação dos números {valorMultipicacaoUm:.2f} e {valorMultipicacaoDois:.2f} é: {calculoMultiplicacao:.2f}')
        print('--------------------------------------')
        input("Pressione ENTER para voltar ao menu...")
    elif operacao == 4:
        os.system('clear')
        print('===========================')
        print('    CALCULADORA DIVISÃO    ')
        print('===========================')
        valorDivisaoUm = float(input('Digite o primeiro valor: '))
        valorDivisaoDois = float(input('Digite o segundo valor: '))
        calculoDivisao = valorDivisaoUm / valorDivisaoDois
        print(f'A divisão dos números {valorDivisaoUm:.2f} e {valorDivisaoDois:.2f} é: {calculoDivisao:.2f}')
        print('--------------------------------------')
        input("Pressione ENTER para voltar ao menu...")
    elif operacao == 0:
        os.system('clear')
        print('===============')
        print('    SAINDO...  ')
        print('===============')
        sistema = False
    else:
        print('===================')
        print('  OPÇÃO INVÁLIDA!  ')
        print('===================')