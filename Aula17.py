# Aprendendo o pacote externo Time
import time

# Exemplo 1 - Trabalhando com temporizador
print(f'Esse print foi rápido!')
time.sleep(3.0)
print(f'Esse print demorou 3.0 segundos para ser printado!')

# Exemplo 2 - Capturando o atual momento
Agora = time.localtime()
print(type(Agora))
print(Agora)
print( time.strftime('%m/%d/%Y, %H:%M:%S', Agora ),'\n' )

# Exemplo 3 - Converter uma string para time
time_texto = '27 February, 2023'
Conversao = time.strptime(time_texto, '%d %B, %Y')
print(Conversao)

