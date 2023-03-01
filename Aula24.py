# Aprendendo a estrutura de quebra Break e Continue
# O uso de loops no Python automatiza e repete as tarefas de maneira eficiente. Mas, às vezes, pode surgir uma condição em que você deseja sair completamente do loop, 
# pular uma iteração ou ignorar essa condição. Isso pode ser feito por instruções de controle de loop . As instruções de controle de loop alteram a execução de sua 
# sequência normal. Quando a execução sai de um escopo, todos os objetos automáticos que foram criados nesse escopo são destruídos. Python suporta as seguintes instruções 
# de controle.

# Exemplo 1 - For + Lista + If + Break
Lista_nomes = ['Laura','Alexandre','Amanda','Guilherme']
Loop = 0

for P in Lista_nomes:

  if P == 'Amanda':
    print('Chegou')
    break

else:
  pass

Loop += 1
print( Loop )

# Exemplo 2 - Contando com interrupção
Loop = 0

while Loop <= 10:
  print (Loop)
  Loop += 1

if Loop == 5:
  
  for c in range(10):
    print(c)

    break

# Exemplo 3 - Loop de 1 a 10
for i in range(1,11):
  
  # if i is equals to 6,
  # continue to next iteration
  # without printing
  if i == 5:
    continue
    print(f'{i}º iteração --> Estou no IF')

else:
  # otherwise print the value
  # of if
  print(f'{i}º Continue a nadar!')
  # print i