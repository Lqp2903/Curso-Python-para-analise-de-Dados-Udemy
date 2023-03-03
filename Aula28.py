# Aprendendo a função Classes/Objetos
# Python é uma linguagem orientada a objetos. 
# Uma classe é como um construtor de objetos, ou um "projeto" para criar objetos.

# Exemplo 1 - Cadastro

class cadastro:

# Método de construção
  def __init__(self, Nome, Idade):
    self.Nome = Nome
    self.Idade = Idade

  def Boas_Vindas(self):
    print(f'Olá, seja bem-vindo(a) {self.Nome}.')

  def Recusado(self):
    print(f'Peça permissão ao seu responsável para acessar o sistema,{self.Nome}!')

  # Função
  def Maior_Idade(self):
    if self.Idade >= 18:
      print('Acesso concedido.')
      self.Boas_Vindas()
    else:
      print('Acesso negado.')
      self.Recusado()
Dados = cadastro('Laura', 17)
Dados.Maior_Idade()