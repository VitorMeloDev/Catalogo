    # ==========================================================
    # Listas (equivalente aos arrays/vetores do C, porém dinâmicas)
    # ==========================================================

    # Uma lista pode armazenar qualquer tipo de dado.
    numeros = [10, 20, 30, 40]
    nomes = ["Ana", "Carlos", "João"]
    misturada = [10, "Python", True, 3.14]

    # Acessando elementos (índices começam em 0)
    print(numeros[0])      # 10
    print(numeros[2])      # 30

    # Também aceita índices negativos
    print(numeros[-1])     # último elemento
    print(numeros[-2])     # penúltimo elemento

    # Alterando um elemento
    numeros[1] = 25

    # Tamanho da lista
    print(len(numeros))

    # Percorrendo com índices (parecido com C)
    for i in range(len(numeros)):
        print(f"Índice {i}: {numeros[i]}")

    # Percorrendo diretamente os elementos
    for numero in numeros:
        print(numero)

    # Adicionando elementos
    numeros.append(50)

    # Inserindo em uma posição específica
    numeros.insert(2, 99)

    # Removendo pelo valor
    numeros.remove(99)

    # Removendo pelo índice
    numeros.pop(0)

    # Limpando toda a lista
    copia = numeros.copy()
    copia.clear()

    # Verificando se existe um elemento
    if 40 in numeros:
        print("40 encontrado!")

    # Descobrindo a posição de um elemento
    print(numeros.index(40))

    # Contando ocorrências
    repetidos = [1, 2, 1, 3, 1]
    print(repetidos.count(1))

    # Ordenando
    numeros.sort()

    # Ordem inversa
    numeros.reverse()

    # Fatiamento (Slice)
    print(numeros[1:3])    # elementos do índice 1 até o 2
    print(numeros[:2])     # do início até índice 1
    print(numeros[2:])     # do índice 2 até o final
    print(numeros[:])      # cópia da lista

    # Concatenação
    lista1 = [1, 2]
    lista2 = [3, 4]
    lista3 = lista1 + lista2

    print(lista3)
