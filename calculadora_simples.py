# Calculadora Simples (4 operações)
import os
sistema = True

print('------------------------------------')
print('   CALCULADORA SIMPLES (2 VALORES)')
print('         NÚMEROS INTEIROS')
print('------------------------------------')
print('1 - SOMA')
print('2 - SUBTRAÇÃO')
print('3 - MULTIPICAÇÃO')
print('4 - DIVISÃO')
print('------------------------------------')
operacao = int(input('Escolha a operação que deseja: '))

while sistema == True:
    if operacao == 1:
        os.system('clear')
        
        print('------------------------')
        print('    CALCULADORA SOMA    ')
        print('------------------------')
        valorSomaUm = int(input('Digite o primeiro valor: '))
        valorSomaDois = int(input('Digite o segundo valor: '))
        calculoSoma = valorSomaUm + valorSomaDois
        print(f'A soma dos números {valorSomaUm} e {valorSomaDois} é: {calculoSoma}')
        break

    elif operacao == 2:
        os.system('clear')
        
        print('-----------------------------')
        print('    CALCULADORA SUBTRAÇÃO    ')
        print('-----------------------------')
        valorSubtracaoUm = int(input('Digite o primeiro valor: '))
        valorSubtracaoDois = int(input('Digite o segundo valor: '))
        calculoSubtracao = valorSubtracaoUm - valorSubtracaoDois
        print(f'A subtração dos números {valorSubtracaoUm} e {valorDivisaoDois} é: {calculoSubtracao}')
        break
    elif operacao == 3:
        os.system('clear')
        
        print('--------------------------------')
        print('    CALCULADORA MULTIPICAÇÃO    ')
        print('--------------------------------')
        valorMultipicacaoUm = int(input('Digite o primeiro valor: '))
        valorMultipicacaoDois = int(input('Digite o segundo valor: '))
        calculoMultiplicacao = valorMultipicacaoUm * valorMultipicacaoDois
        print(f'A multiplicação dos números {valorMultipicacaoUm} e {valorMultipicacaoDois} é: {calculoMultiplicacao}')
        break
    else:
        os.system('clear')
        
        print('---------------------------')
        print('    CALCULADORA DIVISÃO    ')
        print('---------------------------')
        valorDivisaoUm = int(input('Digite o primeiro valor: '))
        valorDivisaoDois = int(input('Digite o segundo valor: '))
        calculoDivisao = valorDivisaoUm // valorDivisaoDois
        print(f'A divisão dos números {valorDivisaoUm} e {valorDivisaoDois} é: {calculoDivisao}')
        break