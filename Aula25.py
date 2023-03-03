# Aprendendo Estrutura de Funções simples
# Uma função é um bloco de código que só é executado quando é chamado.
# Você pode passar dados, conhecidos como parâmetros, para uma função.
# Uma função pode retornar dados como resultado.

# Exemplo 1 - Função de soma
def Somar (Valor1, Valor2):
    Soma = Valor1 + Valor2
    print(Soma)

Somar(-67.250,20.400)

# Exemplo 2 - Somar 2
for Loop in range(0,10):
    
    import random

x = random.random()
y = random.random()

Somar(x,y)

# Exemplo 2 - Escrito
def Boas_Vindas():
    print('***BOAS VINDAS AO PYTHON***')

Boas_Vindas()

# Exemplo 3 - Lista + Função

from random import randint

def Sobrenome (Texto_1, Numero):
    print(f'O nome dele é: {Texto_1}.')
    print(f'O número dele é: {Numero}.')

    if Numero >= 10:
        print('Maior que 10')
    else:
        print('NADA!')

Lista_Nomes = ['Laura, Alexandre', 'Fulana']

for Nome in Lista_Nomes:
    Sobrenome(Nome, randint(1,12) )