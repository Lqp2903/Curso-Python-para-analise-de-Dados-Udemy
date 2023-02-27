# Aprendendo o pacote Statistics
import statistics

# Exemplo 1 - Qual a média da operação?
Media = statistics.mean([1,2,3,4,5,6])
print(f'A média é:{Media} \n')

# Exemplo 2 - Qual é a mediana da operação?
Mediana = statistics.median([1,4,8,10,7.20])
print(f' A mediana é:{Mediana} \n')

# Exemplo 3 - Qual é a moda da operação?
Moda = statistics.mode([1,7,8,10,5,])
print(f'A moda é:{Moda}')
