# Manipulando listas!
# As listas são usadas para armazenar vários itens em uma linha na vertical
# As listas é um dos quatro tipos de dados internos do Python usados para armazenar coleções de dados, os outros são: Tuple, Set e Dictionary.
# Os comandos mais utilizados são: Append() - adiciona um item ao final da lista; len() - calcula o tamanho da lista; ([]) - acessar posições;
# del() - Excluir um elemento; clear() - limpa a lista; insert() - para inserir um item de lista em um índice espeficiado; extend() - anexar elementos de outra lista na lista atual;
# remove() - remove o item especificado; pop() - remove o indíce especificado; sort() - ordena os valores e reverse() - ordena de forma contrária; copy() - faz uma cópia da lista; 
# index() - retorna o index da lista.

# Exemplo 1 - Criando uma lista vazia
Lista_Vazia = []
print ('Lista Antes', Lista_Vazia, '\n')

# Exemplo 2 - Comando Append() - Inserindo itens numa lista
Lista_Vazia.append(-1)
Lista_Vazia.append(0)
Lista_Vazia.append(1)
Lista_Vazia.append('Fim')
print('Lista Depois', Lista_Vazia, '\n')

# Exemplo 3 - Comando len() - Acessando valores dentro de uma lista
print('A lista contém', len(Lista_Vazia), 'elementos', '\n')

# Exemplo 4 - Comando ([]) - Acessando os elementos dentro de uma lista
print('Acessando o 1º elemento:', Lista_Vazia[0])
print('Acessando o 2º elemento:', Lista_Vazia[1])
print('Acessando o 3º elemento:', Lista_Vazia[2])
print('Acessando o último elemento:', Lista_Vazia[-1])
print('Acessando um período:',Lista_Vazia[0:3], '\n')

# Exemplo 5 - Comando del() - Deletando um item da lista (de acordo com a posição)
del Lista_Vazia[1]
print('Depois da exclusão:', Lista_Vazia, '\n')

# Exemplo 6 - Comando clear() - Limpando os dados da lista
print ('Depois da limpeza:', Lista_Vazia.clear(), '\n')

# Exemplo 7 - Comando insert() - Inserindo valor na lista com posição
Lista_Inserir = ['Posição 1', 'Posição 2', 'Posição 3', 'Posição 4']
Lista_Inserir2 = ['Posição 5', 'Posição 6', 'Fim']
Lista_Inserir.insert(0,'Posição 5')
print(Lista_Inserir, '\n')

# Exemplo 8 - Comando extend() - Inserindo uma lista na outra
Lista_de_carros = ['WW', 'Audi', 'Tesla']
Lista_de_carros2 = ['Ford', 'Mitshubich', 'Hyundai']
Lista_de_carros.extend(Lista_de_carros2)
print(Lista_de_carros, '\n')

# Exemplo 9 - comando remove() - Removendo um item específico pelo nome 
Lista_de_carros.remove('WW')
print (Lista_de_carros, '\n')

# Exemplo 10 - comando index() - Removendo item pela posição (inicia sempre pelo 0)
Lista_de_carros2.pop(2)
print(Lista_de_carros2, '\n')

# Exemplo 11 - comando sort() - Ordenando valores em uma lista
Lista_de_dados_1 = ['C', 'A', 'E', 'B']
Lista_de_dados_1.sort()
print(Lista_de_dados_1, '\n')

# Exemplo 12 - comando reverse() - Ordenando valores inversos em uma lista
Lista_de_dados_2 = [1,2,3,4,5,6]
Lista_de_dados_2.reverse()
print(Lista_de_dados_2, '\n')

# Exemplo 13 - comando copy() - Copiando uma lista
Lista_de_dados_3 = Lista_de_dados_2.copy()
print(Lista_de_dados_3, '\n')

# Exemplo 14 - comando index() - Identificando um elemento na lista (posição)
print(Lista_de_carros.index('Ford'))
print(Lista_de_carros.index('Hyundai'), '\n')
