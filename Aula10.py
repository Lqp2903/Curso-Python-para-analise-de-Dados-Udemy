# Fatiando Strings!
# Um tipo de dado bastante utilizando são as strings, ou cadeia de caracteres (ou sequência de caracteres). String ou str como é chamado em Python, possui várias operações úteis
# associadas a ele. Essas operações tornam Python uma linguagem bastante propícia para manipulação de textos. Algumas funções utilizadas: replace(), startswith(), endswith(),
# count(), capitalize(), isdigit(), isalnum(), upper(), lower(), find (), strip() e split().

# Exemplo 1 - Vamos definir uma String
String = "Aprender Python é muito divertido!"
print (String)

# Exemplo 2 - Descobrindo o tipo da String
print (type(String))

# Exemplo 3 - Descobrindo o tamanho da String
print(len(String))

# Exemplo 4 - Uma concatenação
print (String + ' ' + 'E eu estou aprendendo cada vez mais!')

# Exemplo 5 - Substituindo uma palavra na String
Substituir = String.replace('divertido!','anedótico!')
print (Substituir)

# Exemplo 6 - Verificando de uma String começa ou termina com uma condição
print(String.startswith('Vamos'))
print(String.startswith("Aprender"))
print(String.endswith('divertido!'))
print(String.endswith('Legal!'))

# Exemplo 7 - Contando quantas letras cada palavra possui
print(String.count("e"))

# Exemplo 8 - Transformando a primeira letra da primeira palavra em maiscúla
String_2 = "laura Quadros"
print(String_2.capitalize())

# Exemplo 9 - Verificando se uma String só tem números
String_3 = "123456"
String_4 = "1234ABC"
print(String_3.isdigit())
print(String_4.isdigit())

# Exemplo 10 - Verificando se uma String é alfanumérica
print("123456abc".isalnum())

# Exemplo 11 - Transformando tudo em maiúsculo
print(String.upper())

# Exemplo 12 - Transformando tudo em minúsculo
print(String.lower())

# Exemplo 13 - Procurando algo específico na String (retorna a posição na String) (-1 quando não localiza)
print(String.find("Aprender"))
print(String.find("Vamos"))

# Exemplo 14 - Removendo espaços desnecessários da String
String_5 = ' E dessa removi espaços desnecessários da String'
print(String_5.strip())

# Exemplo 15 - Aprendendo a "quebrar" uma String
String_6 = "Meu sonho é trabalhar com a área de dados."
print(String_6.split())