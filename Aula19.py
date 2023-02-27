# Aprendendo o pacote Random
# Serve para gerar valores aleatórios e serve para várias distribuições.

import random

# Exemplo 1 - Lista numérica
lista_numerica = [1,2,3,4,5,6,7,8,9,10]
print(f'O número sorteado foi:{random.choice(lista_numerica)} \n')

# Exemplo 2 - Uma letra da palavra
palavra = 'Anticonstitucionalissimamente'
print(f'A letra sorteada foi:{random.choice(palavra)} \n')

# Exemplo 3 - Um número entre 0 e 1
numero_aleatorio_1 = random.random()
print(f'O número gerado foi {numero_aleatorio_1} \n')

# Exemplo 4 - Um número entre 0 e 1000
numero_aleatorio_2 = random.randint(0,1000)
print(f'O número sorteado foi {numero_aleatorio_2} \n')
