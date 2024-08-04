#include <stdio.h> // C tem diversas bibliotecas diferentes, eu irei precisar de uma ou muitas delas para trabalhar com C

void limpar_entrada(); // Funcoes podem ser colocadas acima do codigo desse jeito, sem ter que empurrar o main muito para baixo

int main() {
    int numInt = 42; // Normalmente 4 bytes (32 bits), variando de -2,147,483,648 a 2,147,483,647.
    float numFloat = 3.14159; // Normalmente 4 bytes (32 bits), com precisão de cerca de 7 dígitos decimais.
    double numDouble = 2.718281828459; // Normalmente 8 bytes (64 bits), com precisão de cerca de 15 dígitos decimais.
    char caractere = 'A'; // Normalmente 1 byte (8 bits), variando de -128 a 127 (signed) ou 0 a 255 
    char nome[] = "Olá, Mundo!"; // Representa uma cadeia de caracteres (array de char).

    // Modos de formatação das variaveis
    printf("int: %d\n", numInt);
    printf("float: %f\n", numFloat);
    printf("double: %lf\n", numDouble);
    printf("char: %c\n", caractere);
    printf("string: %s\n", nome);

    // Array 
    int arr[5];
    int arrInitialized[5] = {1, 2, 3, 4, 5};

    printf("Primeiro elemento: %d\n", arrInitialized[0]);
    printf("Terceiro elemento: %d\n", arrInitialized[2]);

    // Maztriz
    int matrix[3][3];

    int matrixInitialized[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    printf("Elemento da primeira linha e primeira coluna: %d\n", matrixInitialized[0][0]);
    printf("Elemento da terceira linha e segunda coluna: %d\n", matrixInitialized[2][1]);


    // Estrutura condicional
    int hora; 

    printf("Digite uma hora do dia: "); 
    scanf("%d", &hora); // Funcao para leitura de dados

    if (hora < 12) 
    { 
        printf("Bom dia!\n"); 
    } 
    else 
    { 
        printf("Boa tarde!\n"); 
    } 

    // Estrutura While
    int x, soma; 

    soma = 0; 
    printf("Digite o primeiro numero: "); 
    scanf("%d", &x); 

    while (x != 0) 
    { 
        soma = soma + x; 
        printf("Digite outro numero: "); 
        scanf("%d", &x); 
    }

    printf("SOMA = %d\n", soma); 

    // Estrutura Do-While
    double C, F; 
    char resp; 

    do 
    { 
        printf("Digite a temperatura em Celsius: "); 
        scanf("%lf", &C); 
        F = 9.0 * C / 5.0 + 32.0; 
        printf("Equivalente em Fahrenheit: %.1lf\n", F); 
        printf("Deseja repetir (s/n)? "); 
        limpar_entrada(); 
        scanf("%c", &resp); 
    } 
    while (resp == 's'); 

    // Estrutura For
    int N, i, x1, soma2; 

    printf("Quantos numeros serao digitados? "); 
    scanf("%d", &N); 

    soma2 = 0; 
    for (i = 1; i <= N; i++) 
    { 
        printf("Digite um numero: "); 
        scanf("%d", &x1); 
        soma2 = soma2 + x1; 
    } 

    printf("SOMA = %d\n", soma2); 

    // o valor de retorno da função main indica ao sistema operacional se o programa foi executado com sucesso ou se ocorreu algum erro. 
    // O valor de retorno 0 geralmente indica uma execução bem-sucedida.
    return 0;
}

void limpar_entrada() // Uma declaração de função em C
{ 
    char c; 
    while ((c = getchar()) != '\n' && c != EOF) {} 
} 
