# Exercício 21 - Faça um programa que solicite um número inteiro e mostre o seu valor absoluto. Dica: use a função built-in abs().

num = int(input('Digite um número inteiro: '))
print(f'O valor absoluto de {num} é {abs(num)}.\n')

# Exercício 22 - Faça um programa que peça uma string ao usuário e mostre na tela a quantidade de caracteres.
# Dica: use a função built-in len() e trate a string com o método strip().

string = input('Digite qualquer coisa: ')
print(f'Você digitou: {string}.')
print(f'Quantidade de caracteres do que você digitou é: {len(string)}.\n')

# Exercício 23 - Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. A mensagem na tela deverá seguir o seguinte formato:
# "O número [número] é [par/ímpar]"

numero_1 = int(input('Informe um número inteiro: '))
if num % 2 == 0:
    print(f'O número {numero_1} é par!')
else:
    print(f'O número {numero_1} é ímpar!\n')

# Exercício 24 - O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma pessoa. Escreva um programa que peça o nome, a idade , o peso e a altura do usuário. 
# Ao final calcule e mostre o resultado do seu IMC e classifique este resultado de acordo com a regra a seguir.
# IMC<17 - Muito abaixo do peso ideal
# 17<=IMC<18,5 - Abaixo do peso
# 18,5<=IMC<25 - Peso normal
# 25<=IMC<30 - Acima do peso
# 30<=IMC<35 - Obesidade I
# 35<=IMC<40 - Obesidade II (severa)
# IMC>=40 - Obesidade III (mórbida)
# Lembre que: IMC=massa/(altura*altura)

print('Vamos calcular seu IMC!')
altura = float(input('Qual é a sua altura? '))
peso = float(input('Qual é o seu peso? '))
imc = peso/(altura**2)
print('Um momento que estamos calculando seu IMC!\n')
if imc<17:
    print('Você está muito abaixo do seu peso. Procure um médico imediatamente.\n')
elif 17<= imc <18.5:
    print('Você está abaixo do peso. Aconselhamos a buscar um médico.\n')
elif 18.5<=imc<25:
    print('Seu peso está normal. Continue assim!\n')
elif 25<= imc<30:
    print ('Você está acima do peso. Fique atento.\n')
elif 30<= imc<35:
    print('Você está com obesidade Grau I. Aconselhamos a buscar um médico.\n')
elif 35<= imc<40:
    print('Você está com obesidade Grau II. Procure um médico com urgência!\n')
else:
    print('Obesidade Grau III. Procure um médico com urgência! Há risco de vida!\n')

# Exercício 25 - Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado. Considere a possibilidade de o usuário digitar 
# dois números iguais.

n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
if n1>n2:
    print (f'O {n1} é maior que {n2}.\n')
elif n1 == n2:
    print (f'O número {n1} é igual ao número {n2}.\n')
else:
    print(f'O número {n1} é menor que {n2}.\n')

# Exercício 26 - Escreva um programa que verifique se um determinado número digitado pelo usuário é nulo, positivo ou negativo.
numero_1_ex = float(input('Digite qualquer número: '))
if numero_1_ex>0:
    print(f'O {numero_1_ex} é positivo.\n')
elif numero_1_ex==0:
    print(f'O número que você digitou é nulo.\n')
else:
    print(f'O número {numero_1_ex} é negativo.\n')

# Exercício 27 - Escreva um programa que receba três números do usuário e mostre na tela o maior número digitado.

Variavel_1 = float(input('Digite o 1º número: '))
Variavel_2 = float(input('Digite o 2º número: '))
Variavel_3 = float(input('Digite o 3º número: '))
if (Variavel_1>=Variavel_2) and (Variavel_1>=Variavel_3):
    print(f'O maior número é: {Variavel_1}.')
elif (Variavel_2>=Variavel_1) and (Variavel_2>=Variavel_3):
    print(f'O maior número é: {Variavel_2}.')
else:
    print(f'O maior número é: {Variavel_3}.\n')

# Exercício 28 - Escreva um programa que gere um número aleatório entre 1 e 100 e mostre na tela.
# Dica: utilize o módulo random.

import random
Variavel1 = random.randint(0,100)
print(f'O número sorteado foi: {Variavel1}.\n')

# Exercício 29 - Elabore um progama para verificar se um ano é bissexto ou não. A condição para ser um ano bissexto é: o ano deve ser divisível por 400; ou se for divisível 
# por 4 e não for divisível por 100.

ano = int(input('Digite o ano: '))
if ano %400==0 or (ano%4==0 and not ano%100==0):
    print('O ano digitado é bissexto.')
else:
    print('O ano digitado não é bissexto.\n')

# Exercício 30 - Elabore um programa para calcular o tamanho de uma string.

string = input('Digite alguma coisa: ')
print(len(string))