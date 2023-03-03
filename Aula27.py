# Entendendo a estrutura TRY
# O try permite testar um bloco de código quanto a erros.
# O except permite que você lide com o erro.
# O finally permite que você execute código, independentemente do resultado dos blocos try e except.

# Exemplo 1 - Operação
try:
    4/2
    print('Deu certo meu scritp!') # Retorna assim quando o script dá certo
except:
    print('Não deu certo meu scritp!') # Retorna assim quando o script não dá certo
finally:
    print('Vou ser executado mesmo assim.') # Independente de ser correto ou não, ele aparecerá assim.

# Exemplo 2 - Texto
try: 
    print (variavel_indefinida)

except NameError:
    print('Deu problema!!')

finally:
    print('Continuo sendo executado de qualquer forma.')