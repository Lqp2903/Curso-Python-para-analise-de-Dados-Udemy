# Operadores de identidade
# São usados para comparar objetos, com a mesma localização da memória.
# Is(Retorna true se ambas as variáveis forem o mesmo objeto)
# Is not (Retorna true se ambas as variáveis não forem o mesmo objeto)

# Exemplo 1
String_1 = "Aprendendo operadores de identidade"
String_2 = "Aprendendo operadores de identidade1"
print (String_1 is String_1)
print (String_1 is String_2)
print (String_2 is String_2)
print (String_1 == String_2)
print (type(String_1)is type(String_2))

# Exemplo 2
String_3 = "123456"
String_4 = "123456ABC"
print (String_3 is String_4)
print (String_3 is String_3)
print (String_4 is String_4)
print (String_3 == String_4)
print (type(String_3) is type (String_4))