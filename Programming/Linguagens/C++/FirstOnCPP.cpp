#include <iostream>   // Biblioteca padrão de entrada e saída (substitui <stdio.h>)
#include <string>     // Para trabalhar com strings de forma mais simples
#include <vector>     // Vetores dinâmicos (substitui arrays fixos na maioria dos casos)
#include <locale>

// Funções podem ser declaradas antes do main normalmente
void diga_ola(std::string nome);

int main() {

    setlocale(LC_ALL, ""); // usa o locale do sistema, assim permitindo acentuação no console

    // -------------------------
    // Tipos de variáveis
    // -------------------------
    int numInt = 42;                // Inteiro
    float numFloat = 3.14159f;      // Float (precisa do sufixo 'f')
    double numDouble = 2.718281828; // Double
    char caractere = 'A';           // Caractere
    bool ehVerdade = true;          // Booleano
    std::string nome = "Olá, Mundo!"; // String C++ (mais segura que char[])

    // Impressão com cout
    std::cout << "int: " << numInt << "\n";
    std::cout << "float: " << numFloat << "\n";
    std::cout << "double: " << numDouble << "\n";
    std::cout << "char: " << caractere << "\n";
    std::cout << "bool: " << ehVerdade << "\n";
    std::cout << "string: " << nome << "\n";

    // -------------------------
    // Vetores
    // -------------------------
    int arr[5] = {1, 2, 3, 4, 5};              // Array fixo estilo C
    std::vector<int> numeros = {10, 20, 30};  // Vetor dinâmico C++
    numeros.push_back(40);                     // Adiciona elemento

    std::cout << "Primeiro do array: " << arr[0] << "\n";
    std::cout << "Último do vector: " << numeros.back() << "\n";

    // -------------------------
    // Estruturas condicionais
    // -------------------------
    int hora;
    std::cout << "Digite uma hora do dia: ";
    std::cin >> hora; // Entrada de dados com cin

    if (hora < 12) {
        std::cout << "Bom dia!\n";
    } else {
        std::cout << "Boa tarde!\n";
    }

    // -------------------------
    // Estruturas de repetição
    // -------------------------
    int soma = 0, x;
    std::cout << "Digite números (0 para sair): ";
    std::cin >> x;

    while (x != 0) {
        soma += x;
        std::cout << "Digite outro número: ";
        std::cin >> x;
    }
    std::cout << "SOMA = " << soma << "\n";

    // For tradicional
    int N;
    std::cout << "Quantos números somar? ";
    std::cin >> N;
    int soma2 = 0;

    for (int i = 0; i < N; i++) {
        int y;
        std::cout << "Digite um número: ";
        std::cin >> y;
        soma2 += y;
    }
    std::cout << "SOMA = " << soma2 << "\n";

    // -------------------------
    // Funções
    // -------------------------
    diga_ola("Vitor");

    // -------------------------
    // Classes e Objetos
    // -------------------------
    class Pessoa {
    public:
        std::string nome;
        int idade;

        Pessoa(std::string n, int i) : nome(n), idade(i) {} // Construtor

        void apresentar() {
            std::cout << "Olá, meu nome é " << nome 
                      << " e tenho " << idade << " anos.\n";
        }
    };

    Pessoa p1("Alice", 25);
    p1.apresentar();

    // -------------------------
    // Retorno do programa
    // -------------------------
    return 0;
}

// Implementação da função
void diga_ola(std::string nome) {
    std::cout << "Olá, " << nome << "!\n";
}
