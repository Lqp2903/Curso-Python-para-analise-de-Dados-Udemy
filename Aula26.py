# Aprendendo a função Lambda
# É uma função anônima porque não precisa declarar uma variável.
# Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.
# Recomenda-se usar para expressões simples.

# Exemplo 1 - Soma
Funcao_soma = lambda valor: valor + 10
print(Funcao_soma(1))

Funcao_soma2 = lambda valor_1, valor_2: valor_1 + valor_2
print(Funcao_soma2(-100,20))    

# Exemplo 2 - Resto da divisão
Operacao_1 = lambda qualquer_valor: 'Verdadeiro' if qualquer_valor % 2 == 0 else 'Falso'
print(Operacao_1(97))

Operacao_2 = lambda qualquer_valor: 'Verdadeiro' if qualquer_valor % 2 == 0 else 'Falso'
print(Operacao_1(4))