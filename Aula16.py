# Aprendendo o pacote datetime

import datetime

# Exemplo 1 = Dia de hoje
dia_hoje = datetime.datetime.today().date()
print(f'Hoje é {dia_hoje} \n')

# Exemplo 2 - Construindo uma data
Data = datetime.date(2023,6,20)
print(f'A data de entrega do projeto é: {Data} \n')

# Exemplo 3 - Acessando dos atributos da data
Dia = Data.day
Mes = Data.month
Ano = Data.year
print(f'Hoje é dia {Dia} do mês {Mes} do ano de {Ano} \n')

# Exemplo 4 - Operação em data
Intervalo = Data - dia_hoje
print(f'Já se passou {Intervalo} dias do ano \n')

# Exemplo 5 - Ajustando o formato da data
Novo_Formato = dia_hoje.strftime('%d/%m/%y')
print(f'O novo formato da data ficará assim: {Novo_Formato} \n')

# Exemplo 6 - Aumentando e diminuindo dias
print(f'Somando 30 dias a data ficará: {dia_hoje+datetime.timedelta(days = 30)}')
print(f'Diminuindo 30 dias a data ficará: {dia_hoje-datetime.timedelta(days=30)}')