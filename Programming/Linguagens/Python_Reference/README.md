# Python Reference

Um catálogo pessoal para **estudar Python, experimentar conceitos e consultar rapidamente no futuro**.

A ideia não é substituir a documentação oficial nem ser uma lista de comandos. Cada arquivo reúne conceitos relacionados, buscando manter três coisas próximas:

* **o que é** o conceito;
* **como funciona** na prática;
* **como aparece em código real**.

O catálogo deve servir tanto para estudar algo pela primeira vez quanto para recuperar rapidamente algo que você já estudou, mas esqueceu.

---

## Estrutura

```text
Python/
├── 01_Python_Basics.py
├── 02_Python_Collections.py
├── 03_Python_Functions.py
├── 04_Python_OOP.py
├── 05_Python_Exceptions.py
├── 06_Python_Files_IO.py
├── 07_Python_Modules.py
├── 08_Python_Types.py
├── 09_Python_Advanced.py
├── 10_Python_Data_Processing.py
└── README.md
```

Os arquivos seguem uma progressão aproximada: fundamentos → estruturas → funções → objetos → erros → I/O → módulos → tipos → recursos avançados → processamento de dados.

A divisão não é rígida. Um conceito pode aparecer em mais de um arquivo quando fizer sentido explicá-lo em contextos diferentes.

---

# 01 — Python Basics

Fundamentos necessários para ler e escrever Python.

### Principais conceitos

* variáveis;
* tipos básicos;
* operadores;
* strings;
* conversão de tipos;
* condições;
* loops;
* `break`;
* `continue`;
* truthiness;
* `input()`;
* `print()`;
* `__name__`;
* main guard.

**Pergunta central:**

> Como Python representa valores e executa instruções?

---

# 02 — Python Collections

Estruturas utilizadas para armazenar e organizar múltiplos valores.

### Principais conceitos

* `list`;
* `tuple`;
* `set`;
* `dict`;
* indexing;
* slicing;
* `enumerate()`;
* `zip()`;
* comprehensions;
* unpacking;
* operações comuns sobre coleções.

**Pergunta central:**

> Como escolher e manipular uma estrutura para representar meus dados?

---

# 03 — Python Functions

Funções como unidade de comportamento e reutilização.

### Principais conceitos

* definição de funções;
* parâmetros;
* argumentos;
* valores padrão;
* argumentos nomeados;
* `*args`;
* `**kwargs`;
* `return`;
* `None`;
* escopo;
* `lambda`;
* funções como valores;
* `Callable`;
* recursão;
* generators.

**Pergunta central:**

> Como transformar comportamento em algo reutilizável e combinável?

---

# 04 — Python OOP

Programação orientada a objetos em Python.

### Principais conceitos

* classes;
* objetos;
* atributos;
* métodos;
* construtores;
* encapsulamento;
* `property`;
* variáveis de classe;
* `classmethod`;
* `staticmethod`;
* herança;
* `super()`;
* overriding;
* abstração;
* `ABC`;
* `abstractmethod`;
* polimorfismo;
* composição;
* `Protocol`;
* nested classes.

**Pergunta central:**

> Como organizar comportamento e responsabilidades entre diferentes objetos?

---

# 05 — Python Exceptions

Como Python representa, gera e trata situações de erro.

### Principais conceitos

* exceptions;
* `try`;
* `except`;
* `else`;
* `finally`;
* `raise`;
* `Exception`;
* hierarquia de exceções;
* exceções personalizadas;
* tratamento específico de erros.

**Pergunta central:**

> O que acontece quando algo não pode ser executado normalmente?

---

# 06 — Python Files and I/O

Interação com arquivos e fluxos de entrada e saída.

### Principais conceitos

* `open()`;
* file objects;
* leitura;
* escrita;
* `read()`;
* `readline()`;
* iteração sobre arquivos;
* modos `r`, `w` e `a`;
* `with`;
* encoding;
* `stdin`;
* `stdout`;
* `stderr`.

**Pergunta central:**

> Como um programa troca dados com o mundo externo?

---

# 07 — Python Modules

Como organizar código e utilizar código existente.

### Principais conceitos

* módulos;
* `import`;
* `from ... import`;
* aliases;
* `sys`;
* `sys.argv`;
* `__name__`;
* packages;
* standard library;
* `pathlib`.

**Pergunta central:**

> Como dividir um programa em partes e reutilizar código?

---

# 08 — Python Type Hints

Sistema de anotações e análise estática de tipos.

### Principais conceitos

* type hints;
* annotations;
* `list[T]`;
* `dict[K, V]`;
* `tuple[...]`;
* `Any`;
* `object`;
* unions;
* `None`;
* `Callable`;
* `TypeVar`;
* `Protocol`;
* `dataclass`;
* type narrowing;
* `mypy`.

**Pergunta central:**

> Como comunicar e verificar as expectativas de tipos do meu código?

---

# 09 — Python Advanced

Recursos da linguagem que aparecem com mais frequência em código Python sofisticado.

### Principais conceitos

* decorators;
* iterables;
* iterators;
* generators;
* `yield`;
* context managers;
* `with`;
* dunder methods;
* introspection;
* `type()`;
* `isinstance()`;
* `hasattr()`.

**Pergunta central:**

> O que existe por trás das abstrações que Python oferece?

---

# 10 — Python Data Processing

Processamento, transformação e comunicação de dados.

### Principais conceitos

* transformação de coleções;
* filtragem;
* ordenação;
* `key`;
* funções de transformação;
* JSON;
* serialização;
* desserialização;
* interfaces;
* processamento polimórfico;
* pipelines;
* plugins;
* `Protocol`.

**Pergunta central:**

> Como receber dados, transformá-los, processá-los e entregá-los a outra parte do sistema?

---

# Como usar este catálogo

O catálogo funciona melhor como **laboratório**, não apenas como material de leitura.

Ao encontrar um conceito desconhecido:

```text
1. Leia a definição.
       ↓
2. Observe o exemplo.
       ↓
3. Execute o código.
       ↓
4. Modifique alguma coisa.
       ↓
5. Observe o comportamento.
       ↓
6. Tente explicar o que aconteceu.
```

Se uma alteração produzir um resultado inesperado, isso é útil: significa que existe alguma suposição sobre o funcionamento da linguagem que ainda precisa ser investigada.

---

# Filosofia

> Observe a realidade.
> Questione suas suposições.
> Construa hipóteses.
> Teste-as.
> Aprenda com os resultados.
> Se parece mágica, você ainda não cavou fundo o suficiente.

A intenção deste catálogo é justamente reduzir essa sensação de "mágica".

Quando algo parecer automático, vale perguntar:

* O que Python está fazendo por baixo?
* Qual objeto está realmente envolvido?
* Qual método está sendo chamado?
* Qual tipo está sendo produzido?
* O que acontece se eu mudar a entrada?
* Qual é a regra que explica esse comportamento?

---

# Regra de manutenção

O catálogo deve crescer conforme novos conceitos forem encontrados.

Ao adicionar um conceito importante, prefira:

**contexto → definição → exemplo → relação com outros conceitos**

em vez de simplesmente adicionar um novo snippet isolado.

O objetivo é que, daqui a meses, abrir qualquer arquivo ainda permita reconstruir mentalmente **como e por que aquilo funciona**, e não apenas lembrar qual sintaxe deve ser digitada.
