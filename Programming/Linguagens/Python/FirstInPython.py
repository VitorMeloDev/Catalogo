# Python não precisa de bibliotecas para funções básicas como C, mas você pode importar módulos conforme necessário.

# Importando bibliotecas
import math  # Importa uma biblioteca padrão do Python para funções matemáticas
from datetime import datetime  # Importa a função datetime da biblioteca datetime

def limpar_entrada():
    input("Pressione Enter para continuar...")  # Uma maneira simples de "limpar" a entrada do usuário

def main():
    numInt = 42  # Inteiros não têm limite de tamanho (exceto pela memória disponível).
    numFloat = 3.14159  # Números de ponto flutuante (precisão depende da máquina).
    numDouble = 2.718281828459  # Não há distinção entre float e double em Python, ambos são float.
    caractere = 'A'  # Python não tem tipo char separado, apenas strings.
    nome = "Olá, Mundo!"  # Strings em Python são objetos, não arrays de char.

    # Modos de formatação de variáveis
    print(f"int: {numInt}")
    print(f"float: {numFloat}")
    print(f"double: {numDouble}")
    print(f"char: {caractere}")
    print(f"string: {nome}")

    # Lista (equivalente a um array)
    arr = [1, 2, 3, 4, 5]
    print(f"Primeiro elemento: {arr[0]}")
    print(f"Terceiro elemento: {arr[2]}")

    # Matriz (lista de listas)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"Elemento da primeira linha e primeira coluna: {matrix[0][0]}")
    print(f"Elemento da terceira linha e segunda coluna: {matrix[2][1]}")

    # Dicionário (estrutura chave-valor)
    dicionario = {
        "nome": "João",
        "idade": 30,
        "cidade": "São Paulo"
    }
    print(f"Nome: {dicionario['nome']}")
    print(f"Idade: {dicionario['idade']}")
    print(f"Cidade: {dicionario['cidade']}")

    # Estrutura condicional
    hora = int(input("Digite uma hora do dia: "))

    if hora < 12:
        print("Bom dia!")
    else:
        print("Boa tarde!")

    # Estrutura While
    soma = 0
    x = int(input("Digite o primeiro número: "))

    while x != 0:
        soma += x
        x = int(input("Digite outro número (0 para encerrar): "))

    print(f"SOMA = {soma}")

    # File I/O (Entrada e Saída de Arquivos)
    # Abrindo um arquivo para leitura
    with open('arquivo.txt', 'r') as file:
        conteudo = file.read()
        print(f"Conteúdo do arquivo: {conteudo}")

    # Obtendo a hora atual e o dia atual
    hora_atual = datetime.now().strftime("%H:%M:%S")
    dia_atual = datetime.now().strftime("%d/%m/%Y")

    # Escrevendo no arquivo com a hora e o dia
    with open('arquivo.txt', 'w') as file:
        file.write(f"Escrevendo no arquivo!\nAgora são {hora_atual} do dia {dia_atual}\n")

    # Exceções (tratamento de erros)
    try:
        y = int(input("Digite um número para dividir 100: "))
        resultado = 100 / y
        print(f"Resultado da divisão: {resultado}")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
    except ValueError:
        print("Erro: Entrada inválida! Por favor, insira um número.")

    # Estrutura For
    N = int(input("Quantos números serão digitados? "))
    soma2 = 0

    for i in range(1, N + 1):
        x1 = int(input("Digite um número: "))
        soma2 += x1

    print(f"SOMA = {soma2}")

if __name__ == "__main__":
    main()