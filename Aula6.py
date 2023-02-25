# Conhecendo dados no Python e verificando o que são
# São alguns tipos de texto: 
# Text Type: str
# Numeric Types: int, float, complex
# Sequence types: list, tuple, range
# Mapping type: dict
# Set types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview

String = str ("sera que é tipo texto?")
Inteiro = int (10)
Flutuante = float (100.52)
Complex = complex (1J)
Lista = list (("Frutas, frutas2"))
Tupla = tuple (("A","B","C"))
Range = range (6)
Dicionario = dict (nome = "Laura", age = 26)
Set = set (("A", "B", "C"))
Booleano = bool (5)
Bytes = bytes (5)
bytearray = bytearray (5)
memoryview = memoryview (bytes(5))
from datetime import datetime
Data = datetime.today().date()

# Mostrando os valores acima
print (type (String))
print (type (Inteiro))
print (type (Flutuante))
print (type (Complex))
print (type (Lista))
print (type (Tupla))
print (type (Range))
print (type (Dicionario))
print (type (Set))
print (type (Booleano))
print (type (Bytes))
print (type (bytearray))
print (type (memoryview))
