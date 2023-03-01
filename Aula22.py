# Aprendendo o comando Loop For
# Executa um comando em looping até chegar em determinada condição. Podemos usar em lista, tupla, string, etc.

# Exemplo 1 - Até 10 números que use *2 de base
for exemplo_1 in range(10):
    print((exemplo_1 *2), '\n')

# Exemplo 2 - For e Lista
Lista_de_paises = ['Brasil, Argentina, Bolivia, Uruguai, Venezuela, Paraguai, Chile, Colombia, Suriname, Guiana, Guiana Francesa']
for Loop in Lista_de_paises:
    print ((Loop), '\n')

# Exemplo 3 - For e Lista
Lista_de_paises_2 = ['Mexico, Panama, Costa Rica, Honduras, El Salvador, Guatemala, Cuba, Bahamas, Haiti, Republica Dominicana, Porto Rico']
for Loop in range(len((Lista_de_paises_2))):
    print((Lista_de_paises_2[Loop]), '\n')

# Exemplo 4 - For + Lista + If + enumerate
for Posicao, P in enumerate( Lista_de_paises_2 ):
    print(( Posicao /4 , P), '\n')  

# Exemplo 5 - For + Lista + If + Range
lista_de_numeros = [ Numero for Numero in range(1,100,5) ]
Armazenar = []

for x in lista_de_numeros:
 
 if x % 2 == 0:
    Armazenar.append( x )
    
print(Armazenar)

from pandas import DataFrame
print( DataFrame(Armazenar), '\n' )


# Exemplo 6 - For + Lista + Dicionário
Lista_1 = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai']

Dicionario = {
   'Brasil' : 'Real',
   'Argentina' : 'Peso ARG',
   'Uruguai' : 'Peso URG',
   'Paraguai': 'Guarany'
}

for Paises in Lista_1:
   
   if Paises == 'Brasil':
      print(f'A moeda do {Paises} é { Dicionario[Paises]}')
      print('A moeda do', Paises, 'é', Dicionario[Paises])
      print('A moeda do' + ' ' + str (Paises) + ' '  + 'é' + ' ' + str (Dicionario[Paises] ) )
   else:
      pass
 