# Python Collections
# List, Tuple, Set and Dictionary


# ==========================================================
# List
# ==========================================================

# Listas são ordenadas, mutáveis e permitem valores repetidos.
# Podem armazenar diferentes tipos de dados.

numeros = [10, 20, 30, 40]
misturada = [10, "Python", True, 3.14]

print(numeros[0])
print(numeros[-1])

numeros[1] = 25
print(numeros)

print(len(numeros))

numeros.append(50)
numeros.insert(1, 15)

numeros.remove(15)
numeros.pop(0)

print(40 in numeros)
print(numeros.index(40))
print(numeros.count(30))

numeros.sort()
numeros.reverse()

print(numeros[1:3])
print(numeros[:2])
print(numeros[2:])
print(numeros[:])

lista1 = [1, 2]
lista2 = [3, 4]
lista3 = lista1 + lista2

print(lista3)

for numero in numeros:
    print(numero)


# ==========================================================
# Tuple
# ==========================================================

# Tuplas são ordenadas e imutáveis.
# São úteis para representar dados que não devem ser alterados.

coordenada = (10.5, 20.0, 30.5)

print(coordenada[0])
print(coordenada[-1])
print(len(coordenada))

x, y, z = coordenada

print(x)
print(y)
print(z)

print(20.0 in coordenada)
print(coordenada.count(20.0))
print(coordenada.index(20.0))

# Isso causaria um erro:
# coordenada[0] = 100


# ==========================================================
# Set
# ==========================================================

# Sets não possuem ordem definida e não permitem valores repetidos.
# São úteis quando queremos trabalhar com elementos únicos.

numeros_unicos = {1, 2, 3, 3, 4, 4}

print(numeros_unicos)

numeros_unicos.add(5)
numeros_unicos.remove(1)

print(3 in numeros_unicos)

# Operações entre conjuntos

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # União
print(a & b)  # Interseção
print(a - b)  # Diferença
print(a ^ b)  # Diferença simétrica


# ==========================================================
# Dictionary
# ==========================================================

# Dicionários armazenam dados no formato chave: valor.
# As chaves devem ser únicas.

pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

print(pessoa["nome"])
print(pessoa["idade"])

pessoa["idade"] = 31
pessoa["profissao"] = "Developer"

print(pessoa)

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

print("nome" in pessoa)

pessoa.pop("cidade")

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


# ==========================================================
# Empty Collections
# ==========================================================

lista_vazia = []
tupla_vazia = ()
set_vazio = set()
dicionario_vazio = {}

print(len(lista_vazia))
print(len(tupla_vazia))
print(len(set_vazio))
print(len(dicionario_vazio))


# ==========================================================
# Useful Functions
# ==========================================================

numeros = [10, 20, 30, 40, 50]

print(len(numeros))
print(sum(numeros))
print(min(numeros))
print(max(numeros))
print(sorted(numeros))

print(any(n > 40 for n in numeros))
print(all(n > 0 for n in numeros))


# ==========================================================
# List Comprehension
# ==========================================================

# Forma compacta de criar listas a partir de outra sequência.

numeros = [1, 2, 3, 4, 5]

quadrados = [numero ** 2 for numero in numeros]

print(quadrados)

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)


# ==========================================================
# Copy
# ==========================================================

lista = [1, 2, 3]

copia = lista.copy()

copia.append(4)

print(lista)
print(copia)


# ==========================================================
# Nested Collections
# ==========================================================

# Listas podem conter outras listas.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])
print(matrix[2][1])

for row in matrix:
    for value in row:
        print(value)


# ==========================================================
# Command Line Arguments
# ==========================================================

# sys.argv é uma lista contendo os argumentos recebidos
# pela linha de comando.

import sys

print(sys.argv)

print(sys.argv[0])

for argument in sys.argv[1:]:
    print(argument)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Running directly")
