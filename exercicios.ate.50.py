# Exercício 41 - Escreva um programa que mostre de 50 até 1 na tela.

for num in range (50,0,-1):
    print(f'{num}\n')

# Exercício 42 - Escreva um programa que mostre de 150 até 200 na tela.

for num in range(150,201):
    print(f'{num}\n')

# Exercício 43 - Escreva um programa de contagem regressiva, ou seja, imprima na tela o seguinte padrão numérico:

for num in range(5,-1,-1):
    print(f'{num} \n')

# Exercício 44 - Faça um programa que imprima na tela de 1 até um número digitado pelo usuário.

num_1 = int(input('Digite um número: '))  
 
for num_1 in range(1,num_1+1):
    print(f'{num_1} \n')

# Exercício 45 - Escreva um programa que mostre na tela os 20 primeiros múltiplos de 5.

lista = []
x = 1
while len (lista)<20:
    if x%5==0:
        lista.append(x)
        x+=1
    x+=1
for num in lista:
    print(f'{num}\n')

# Exercício 46 - Utilizando estruturas de repetição escreva um programa que mostre os resultados da tabuada (multiplicação) de um número inserido pelo usuário.

tabuada = int(input('Digite um número inteiro: '))
for num in range (1,11):
    print(f'{tabuada} x {num} = {tabuada*num}\n')

# Exercícios 47 - Utilizando estruturas de repetição escreva um programa que mostre os resultados da tabuada de multiplicação dos números entre 1 e 10,

for valor in range (1,11):
    for tabuada in range(1,11):
        print(f'{valor} x {tabuada} = {valor*tabuada}\n')

# Exercício 48 - Em um único loop escreva um programa que mostre na tela de 1 a 10 três vezes e ao final mostre a mensagem Fim . No primeiro loop utilize for e nos dois 
# loops seguintes while.

x = 1
for i in range(1,11):
    print(i)
    if i==10:
        while x<=10:
            print(x)
            x+=1
            if x==11:
                y=1
                while y<=10:
                    print(y)
                    y+=1
                    if y==11:
                        print('Fim do programa.\n')

# Exercício 49 - Escreva um programa que peça ao usuário números entre 0-10. Se o usuário inserir um número fora desse intervalo o programa deverá finalizar com uma 
# mensagem personalizada.

num1 = 0
while 0<=num1<=10:
    num1 = int(input('Insira um número inteiro entre 0 a 10: '))
    if num1<0 or num1>10:
        print('Programa encerrado.')

# Exercício 50 - Em um único loop escreva um programa que mostre na tela de 0-5, cinco vezes e ao final mostre a mensagem Fim . Utilize apenas for em sua implementação.

for i in range(0,6):
    print(i)
    if i==5:
        for j in range(0,6):
            print(j)
            if j==5:
                for k in range(0,6):
                    print(k)
                    if k==5:
                        for l in range(0,6):
                            print(l)
                            if l==5:
                                for m in range(0,6):
                                    print(m)
                                    if m==5:
                                        print('Fim.')