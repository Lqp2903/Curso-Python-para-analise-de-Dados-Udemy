# Exercício 31 - Utilize o módulo datetime e mostre na tela a data e hora atual do sistema de acordo com o formato descrito abaixo.

import datetime
data_atual = datetime.datetime.now()
print(data_atual.strftime('%d/%m/%Y - %H:%M:%S \n'))

# Exercício 32 - Escreva um programa que inverta uma string. Exemplos:
# Hello World!
# Python
# !dlroW olleH
# nohtyP

palavra1 = 'Hello World!'
palavra2 = 'Python'
print(palavra1)
print(palavra2)
print(palavra1[::-1])
print(palavra2[::-1], '\n')

# Exercício 33 - Escreva um programa para mostrar na tela o calendário do mês de dezembro de 2020. Dica: importe o módulo calendar.

import calendar
print(calendar.month(2020,12), '\n')

# Exercício 34 - Modifique o programa anterior e permita que o usuário especifique o ano e o mês a serem mostrados na tela.

import calendar
ano = int(input('Digite um ano: '))
mes = int(input('Digite um mês: '))
print(calendar.month(ano, mes), '\n')

# Exercício 35 - Escreva um script que mostre na tela o preço de um produto associado a uma categoria especificada pelo usuário.  Caso o usuário não digite uma categoria válida 
# (número entre 1 e 10) mostre na tela uma mensagem personalizada.

categoria = int(input('Digite a categoria do produto desejada: '))
if categoria==1:
    print('O preço do produto é R$ 0,5.')
elif categoria==2:
    print('O preço do produto é R$ 11,30.')
elif categoria==3:
    print('O preço do produto é R$ 17,50.')
elif categoria==4:
    print('O preço do produto é R$ 33,97.')
elif categoria==5:
    print('O preço do produto é R$ 103,47.')
elif categoria==6:
    print('O preço do produto é R$ 44,67.')
elif categoria==7:
    print('O preço do produto é R$ 12,50.')
elif categoria==8:
    print('O preço do produto é R$ 14,87.')
elif categoria==9:
    print('O preço do produto é R$ 98,12.')
elif categoria==10:
    print('O preço do produto é R$ 131,40.')
else:
    print('Opção inválida.\n')

# Exercício 36 - Resolva o exercício anterior para as categorias de 1 a 8. Utilize estruturas aninhadas.
categoria_2 = int(input('Digite a categoria do produto desejada: '))
if categoria_2==1:
    print('O preço do produto é R$ 0,50.')
else:
    if categoria_2==2:
        print('O preço do produto é R$ 11,30.')
    else:
        if categoria_2==3:
            print('O preço do produto é R$ 17,50.')
        else:
            if categoria_2==4:
                print('O preço do produto é R$ 33,97.')
            else:
                if categoria_2==5:
                    print('O preço do produto é R$ 103,47.')
                else:
                    if categoria_2==6:
                        print('O preço do produto é R$ 44,67.')
                    else:
                        if categoria_2==7:
                            print('O preço do produto é R$ 12,50.')
                        else:
                            if categoria_2==8:
                                print('O preço do produto é R$ 14,87.\n')

# Exercício 37 - Determine se uma letra inserida pelo usuário é uma vogal ou consoante. Armazene as vogais em uma lista e implemente sua solução. 
# Desconsidere a possibilidade de o usuário inserir números ou caracteres especiais.

letra = input('Digite uma letra: ')
vogais = ['a','e','i','o','u']
if letra in vogais:
    print('A letra que você digitou é uma vogal.')
else:
    print('A letra que você digitou é uma consoante.\n')

# Exercício 38 - Escreva um script para classificar um triângulo de acordo com o tamanho dos seus lados. Considere as seguintes informações:
# Triângulo equilátero: todos os lados possuem o mesmo tamanho;
# Trângulo escaleno: todos os lados possuem medidas diferentes;
# Triângulo isósceles: caracterizado por ter dois lados com o mesmo tamanho.

ladoA = float(input('Digite o lado A do triângulo: '))
ladoB = float(input('Digite o lado B do triângulo: '))
ladoC = float(input('Digite o lado C do triângulo: '))
if ladoA==ladoB==ladoC:
    print('O triângulo é equilátero.')
elif ladoA==ladoB or ladoA==ladoC or ladoB==ladoC:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.\n')

# Exercício 39 - Implemente uma calculadora simples com as operações aritméticas básicas. O usuário deverá especificar a operação desejada (+,-,*,/) e seguidamente inserir 
# dois valores. Caso, o usuário escolha divisão e insira o valor do denominar 0 mostre uma mensagem personalizada. Para os demais casos, mostre na tela o resultado da operação 
# desejada.

calculadora = input('Digite a operação desejada: (+,-,*,/)')
if calculadora in ['+','-','*','/']:
    num1 = float(input('Digite o 1º número: '))
    num2 = float(input('Digite o 2º número: '))
    if calculadora=='+':
       print(f'{num1}+{num2} = {num1+num2}.\n')
    elif calculadora=='-':
       print(f'{num1}-{num2}={num1-num2}.\n')
    elif calculadora=='*':
       print(f'{num1}*{num2}={num1*num2}.\n')
    else:
       if num2==0:
        print('O número precisa ser diferente de 0.\n')
       else: 
        print(f'{num1}/{num2}={num1/num2}.\n')
else:
    print('Opção inválida.')
    
# Exercício 40 - Escreva um programa que mostre de 1 até 50 na tela.

for num in range(1,51):
    print(num)
