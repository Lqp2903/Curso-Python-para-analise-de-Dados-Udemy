# Biblioteca para modelagem de dados
import pandas as pd

# Biblioteca para recursos matemáticos
import numpy as np

# Biblioteca para plotagem de dados
# import matplotlib.pyplot as plt

# Lista com os rotulos
Labels = ['1º', '2º', '3º']

# Lista com os valores
Valores = [10, 20, 30,]

# Criando a base de dados com as listas
Serie = pd.Series( data=Valores, index=Labels )
print(Serie) # podemos usar fórmulas para acrescentar na variável.
Serie_nova = pd.Series(data=[50,100,150],index=Labels)
print(Serie + Serie_nova)

# Criando um dicionário
Dicionario = {
    'A' : [1,2,3],
    'B' : [-3,-2,-1],
    'C' : [0,10,20] }

# Criando uma lista com labels
Label = ['1ª Linha', '2ª Linha', '3ª Linha']
DataFrame_01 = pd.DataFrame(Dicionario, index=Label)
print(DataFrame_01)
print(DataFrame_01['A']) # Filtra valores que está na coluna A
print(DataFrame_01[['A','B']]) # Filtra valores que estão na coluna A e B
DataFrame_01['Nova_Coluna'] = DataFrame_01['A'] * DataFrame_01['B'] # Inclui uma nova coluna, multiplicando os valores da primeira e segunda coluna
print(DataFrame_01)
DataFrame_01.drop('Nova_Coluna', axis=1, inplace=True) # Retira a coluna nova
print(DataFrame_01)
print(DataFrame_01.loc['1ª Linha']) # Retorna valores que estão somente na primeira linha
print(DataFrame_01.loc[['1ª Linha', '3ª Linha'],['A','C']]) # Retorna valores de duas linhas das colunas A e C
print(DataFrame_01.iloc[0:3,1:]) # Apresenta as três primeiras linhas a partir da segunda coluna (inicia com 0)
print(DataFrame_01>0) # Apresenta todos os valores como "true" sendo maior que 0 e "false" como menor que 0
print(DataFrame_01[DataFrame_01['A'] > 0]['C']) # Apresenta todos os valores maior que 0, da coluna A e C

Filtro = DataFrame_01['C'] > 0 
DataFrame_02 = DataFrame_01[Filtro] 
print(DataFrame_02['A']) # Retorna valores maiores que 0, a partir da segunda linha
DataFrame_01[(DataFrame_01['A'] > 1) & (DataFrame_01['C']> 0)] # Retorna valores maior que 1 da coluna A, e valores maiores que 0. Incluiu-se a coluna B.
print(DataFrame_02)
DataFrame_01.reset_index() # reseta toda a lista
print(DataFrame_01)
