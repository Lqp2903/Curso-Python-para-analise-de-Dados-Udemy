# Entendendo os comandos If, Else e Elif

# Exemplo 1 - Entendendo o comando If
Idade = 11
if Idade >= 18:
  print (f'Você é maior de idade \n')

# Exemplo 2 - Adicionando o comando Else
if Idade >= 18:
  print(f'Você é maior de idade.')
else:
  print(f'Você é menor de idade! \n')

# Exemplo 3 - Adicionando o comando Elif 
Idade_3 = 16
if Idade_3 > 18:
  print(f'Você é maior de idade!')
elif Idade_3 == 18:
  print(f'Já pode tirar a CNH!!')

elif Idade_3 <18 and Idade_3 >= 14:
  
 if Idade_3 % 2 == 0:  
  print(f' Quase um adulto!')

else: 
  print(f'Você é menor de idade!')

