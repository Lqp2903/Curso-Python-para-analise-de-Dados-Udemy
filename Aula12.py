# Operadores de comparação servem para comparar valores entre dois ou mais números.
# São alguns deles: Igual = "==", Diferente = "!=", Maior = ">", Menor = "<", Maior_Igual = ">=", Menor_Igual = "<="
# Pode ser também in (Retorna true se uma sequência com o valor especificado estiver presente no objeto) ou not in (Retorna true se o valor especificado não estiver na sequência)

# Exemplo 1 
print ("8 é maior que 74:", 8 > 74)
print ("74 é maior que 8:", 74 > 8)
print ("-1 é maior que 0:", -1 > 0)
print ("200 é igual a 200:", 200 == 200)
print ("150 é diferente de 100:", 150!=100)
print ("940 é menor que 1000:", 940<1000)
print ("30 é maior ou igual a 30:", 1 >= 1)
print ("10 é menor é igual a 10", 10 <= 10)

# Exemplo 2
Afazeres = ['Estudar','Limpar a casa', 'Cozinhar', 'Lavar roupas', 'Alimentar gatos']
print ('Banho' in Afazeres)
print ('Dormir' not in Afazeres)
print ('Estudar' in Afazeres)
print ('Alimentar gatos' not in Afazeres)