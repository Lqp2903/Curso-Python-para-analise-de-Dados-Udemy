# Exercício 1 - Faça um programa que mostre uma mensagem na tela.
print('Exercicíos de fixação das aulas! \n')

# Exercicío 2 - Faça um programa que solicite um número do usuário e apresente a seguinte mensagem na tela:
num = input ('Digite um número: ')
print(f'O número digitado foi: {num} \n')

# Exercício 3 - Escreva um programa que solicite o nome e o sobrenome do usuário. Ao final o programa deverá apresentar o nome completo do usuário na tela.
nome = input('Digite seu nome completo: ')
idade = input('Digite sua idade: ')
print(f'Seu nome é {nome} e sua idade é {idade}. \n')

# Exercício 4 - Faça um programa que solicite três números inteiros do usuário e imprima a soma destes.
num1 = int(input('Insira o 1º número: '))
num2 = int(input('Insira o 2º número: '))
num3 = int(input('Insira o 3º número: '))
print(f'{num1} + {num2} + {num3} = {num1+num2+num3} \n')

# Exercício 5 - Escreva um programa que solicite duas notas do usuário e apresente a média na tela da seguinte forma: "A média das notas [nota1] e [nota2] é [média]."
nota1 = float(input('Insira a 1ª nota: '))
nota2 = float(input('Insira a 2ª nota: '))
media = (nota1 + nota2)/2
print(f'A média das notas {nota1} e {nota2} é  {media}. \n')

# Exercício 6 - Faça um programa que calcule a raiz quadrada de um número. O usuário deve inserir um número e o programa deve mostrar na tela o resultado da raiz quadrada 
# do número inserido.
import math
numero_1 = float(input('Insira o número que deseja saber a raiz quadrada: '))
raiz_quadrada = math.sqrt(numero_1)
print(f'A raiz quadrada do número informado é: {raiz_quadrada}. \n')

# Exercício 7 - Faça um programa que peça 5 números de ponto flutuante do usuário e apresente no final a média dos números digitados.
numero1 = float(input('Insira o primeiro número: '))
numero2 = float(input('Insira o segundo número: '))
numero3 = float(input('Insira o terceiro número: '))
numero4 = float(input('Insira o quarto número: '))
numero5 = float(input('Insira o quinto número: '))
media = (numero1 + numero2 + numero3 + numero4 + numero5)/5
print(f'A média dos números é: {media}. \n')

# Exercício 8 - Escreva um programa que faça a conversão de um dado valor de metro para quilômetro.
mt = float(input('Digite um número em metros: '))
print(f'O {mt} metros equivale à {mt/100} km. \n')

# Exercicício 9 - Escreva um programa que calcule a área de uma circunferência. O usuário deve digitar o valor do raio e ao final o programa deverá mostrar na tela 
# a área da circunferência. Use a fórmula: área=pi*r² , em que pi é uma constante e r o raio da circunferência.
# Dica: você pode usar a biblioteca math para pegar a constante pi.

from math import pi
raio = float(input('Digite o valor do raio da circunferência: '))
print(f'A área de circunferência é: {pi*raio**2:.2f} \n')

# Exercício 10 - Faça um programa que peça uma temperatura em Fahrenheit (F) e converta esta temperatura para grau Celsius (C), mostrando o resultado da conversão na tela.
# Use a fórmula: C = 5 * ((F-32) / 9).
f = float(input(f'Insira a temperatura em Fahrenheit: '))
c=5*((f-32)/9)
print(f'A temperatura {f:.2f}]º F equivale a {c:.2f}º em C (graus celsius).')