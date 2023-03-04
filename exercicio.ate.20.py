# Exercício 11 - Escreva um programa que peça dois números e apresente a divisão e multiplicação entre eles. A tela de apresentação deverá seguir o seguinte formato:
# "[número1]x[número2]=[multiplicação]"
#"[número1]/[número2]=[divisão]"

num1 = float(input(f'Insira o 1º número: '))
num2 = float(input(f'Insira o 2º número: '))
print(f'A multiplicação do {num1} x {num2} = {num1*num2}.')
print(f'A divisão do {num1} / {num2} = {num1/num2}.\n')

# Exercício 12 - Escreva um programa que receba o nome, sobrenome e idade do usuário e apresente a seguinte mensagem na tela: "Seja bem-vindo [nome] [sobrenome]."
# "Você possui [idade] anos de idade." No campo nome e sobrenome utilize os métodos strip() e title(). 
#Lembre-se que o primeiro método permite remover os espaços antes e depois da string, enquanto que o último permite colocar a string no formato titlecased (capitaliza a string).

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))
print(f'Seja bem-vindo, {nome.strip().title()} {sobrenome.strip().title()}!')
print(f'Você possui {idade} anos de idade.\n')

# Exercício 13 - Escreva um programa que peça um número do usuário via método input e converta esse número para o formato float.

num_1 = input('Digite um número: ')
num_1 = float(num_1)
print(type(num_1), '\n') 

# Exercício 14 - Escreva um programa que peça o nome e a idade do usuário. Caso a idade do usuário seja maior ou igual a 18 anos apresente a seguinte mensagem: 
# "Seja bem-vindo ao nosso site [nome]!"; caso contrário, apresente a seguinte mensagem: "Você não pode acessar nosso site [nome].".

nome_1_ = input('Informe seu primeiro nome: ')
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print(f'Seja bem-vindo {nome}!')
else:
    print(f'Você não pode acessar o site.\n')

# Exercício 15 - Elabore um programa para calcular a hipotenusa de um triângulo.
# Dicas: Veja o módulo math (math.hypot). Utilize a seguinte fórmula: hipotenusa=(a²+b²)¹/2:

from math import hypot
cateto_a = float(input('Digite o Cateto Adjacente: '))
cateto_b = float(input('Digite o Cateto Oposto: '))
hipotenusa1 = (cateto_a**2+cateto_b**2)**(1/2) # cálculo 1
hipotenusa2 = hypot(cateto_a,cateto_b) # cálculo 2
print(f'O primeiro cálculo da hipotenusa é: {hipotenusa1}.')
print(f'O cálculo da segunda hipotenusa é: {hipotenusa2}.\n')

# Exercício 16 - Faça um programa que recebe um número inteiro do usuário e calcule o fatorial deste número.
# Dica: utilize o módulo math do Python, especificamente math.fatorial.

import math
numero_1 = int(input('Digite um número inteiro: '))
fatorial = math.factorial(numero_1)
print(f'O fatorial de {numero_1} é {fatorial}.\n')

# Exercício 17 - Faça um programa que recebe um número inteiro do usuário e calcule o fatorial deste número.
# Dica: utilize o módulo math do Python, especificamente math.fatorial.

import math
exem_1 = float(input('Digite um número: '))
log1 = math.log10(exem_1) # ou math.log(num,10)
log2 = math.log(exem_1,2)
print(f'O log de {exem_1} na base 10 é: {log1}.')
print(f'O log de {exem_1} na base 2é: {log2}. \n')

# Exercício 18 - Faça um programa que peça a base e a altura de um retângulo e calcule e mostre na tela a área e o perímetro.

base = float(input('Digite a base do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))

area = base*altura
perimetro = 2*base+2*altura

print(f'O retângulo digitado tem base {base} e altura {altura}.')
print(f'A área deste retângulo é: {area}.')
print(f'O perímetro deste retângulo é: {perimetro}.\n')

# Exercício 19 - Escreva um programa que solicite o nome, o sobrenome e o salário atual de um funcionário. Ao fim, calcule seu novo salário considerando cenários hipotéticos, 
# com os seguintes aumentos: 10%, 25%,30% e 50%. A mensagem na tela deverá seguir o seguinte padrão:
#"Olá, [nome] [sobrenome]"
# "Seu salário atual é : [salário]"
# "Seu salário com 10% de aumento é: [salário]"
# "Seu salário com 25% de aumento é: [salário]"
# "Seu salário com 30% de aumento é: [salário]"
# "Seu salário com 50% de aumento é: [salário]"
# No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite remover os espaços antes e após a string, 
# enquanto que o último permite colocar a string no formato titlecased (capitaliza string).

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
salario = float(input('Digite seu salário: '))
salario1 = salario+salario*0.1 # salário c/ 10% de aumento
salario2 = salario+salario*0.25 # salário c/ 25% de aumento
salario3 = salario+salario*0.3 # salário c/ 30% de aumento
salario4 = salario+salario*0.5 # salário c/ 50% de aumento

print(f'Olá, {nome} {sobrenome}.!')
print(f'Seu salário atual é: R$ {salario:.2f}')
print(f'Seu salário com 10% de aumento é: R$ {salario1:.2f}')
print(f'Seu salário com 25% de aumento é: R$ {salario2:.2f}')
print(f'Seu salário com 30% de aumento é: R$ {salario3:.2f}')
print(f'Seu salário com 50% de aumento é: {salario4:.2f}.\n')

# Exercício 20 - Escreva um programa que peça um número inteiro do usuário e calcule e imprima a tabuada deste número.

num_tabuada = int(input('Digite um número inteiro: '))
print(f'A tabuada do número {num_tabuada} é:')
print(f'{num_tabuada} x 1 = {num_tabuada*1}.')
print(f'{num_tabuada} x 2 = {num_tabuada*2}.')
print(f'{num_tabuada} x 3 = {num_tabuada*3}.')
print(f'{num_tabuada} x 4 = {num_tabuada*4}.')
print(f'{num_tabuada} x 5 = {num_tabuada*5}.')
print(f'{num_tabuada} x 6 = {num_tabuada*6}.')
print(f'{num_tabuada} x 7 = {num_tabuada*7}.')
print(f'{num_tabuada} x 8 = {num_tabuada*8}.')
print(f'{num_tabuada} x 9 = {num_tabuada*9}.')
print(f'{num_tabuada} x 10 = {num_tabuada*10}.')

