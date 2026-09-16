# Python OOP
# Classes, inheritance, abstraction, polymorphism, composition and Protocol
#
# Main ideas:
# Class       = blueprint for objects
# Inheritance = reuse and specialization
# Overriding  = replace inherited behavior
# ABC         = define a required interface
# Polymorphism = same interface, different behavior
# Protocol    = structural interface ("if it has the methods, it fits")


# ==========================================================
# Class and Object
# ==========================================================

class Player:
    pass


player = Player()

print(type(player))


# ==========================================================
# Constructor and Attributes
# ==========================================================

class Character:

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health


character = Character("Knight", 100)

print(character.name)
print(character.health)


# ==========================================================
# Instance Methods
# ==========================================================

class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.level = 1

    def level_up(self) -> None:
        self.level += 1


player = Player("Knight")
player.level_up()

print(player.level)


# ==========================================================
# Encapsulation Convention
# ==========================================================

class Account:

    def __init__(self, balance: float) -> None:
        self._balance = balance

    def deposit(self, amount: float) -> None:

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def get_balance(self) -> float:
        return self._balance


account = Account(100)
account.deposit(50)

print(account.get_balance())


# ==========================================================
# Properties
# ==========================================================

class Person:

    def __init__(self, age: int) -> None:
        self._age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value


person = Person(25)

print(person.age)

person.age = 26

print(person.age)


# ==========================================================
# Class Variables
# ==========================================================

class Enemy:

    total_enemies = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Enemy.total_enemies += 1


Enemy("Goblin")
Enemy("Orc")

print(Enemy.total_enemies)


# ==========================================================
# Class Method
# ==========================================================

class Game:

    game_count = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Game.game_count += 1

    @classmethod
    def get_game_count(cls) -> int:
        return cls.game_count


Game("Game A")
Game("Game B")

print(Game.get_game_count())


# ==========================================================
# Static Method
# ==========================================================

class MathUtils:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b


print(MathUtils.add(10, 20))


# ==========================================================
# Inheritance
# ==========================================================

class Animal:

    def speak(self) -> None:
        print("Animal sound")


class Dog(Animal):

    def bark(self) -> None:
        print("Woof")


dog = Dog()

dog.speak()
dog.bark()


# ==========================================================
# super()
# ==========================================================
# super() accesses behavior from the parent class.
# It is commonly used when a child extends a parent's __init__.


class Character:

    def __init__(self, name: str) -> None:
        self.name = name


class Warrior(Character):

    def __init__(self, name: str, weapon: str) -> None:
        super().__init__(name)
        self.weapon = weapon


warrior = Warrior("Knight", "Sword")

print(warrior.name)
print(warrior.weapon)


# ==========================================================
# Method Overriding
# ==========================================================
# A child class provides its own implementation of an
# inherited method.


class Enemy:

    def attack(self) -> None:
        print("Generic attack")


class Goblin(Enemy):

    def attack(self) -> None:
        print("Goblin attack")


Goblin().attack()


# ==========================================================
# Abstract Base Class (ABC)
# ==========================================================
# An ABC defines a contract for subclasses.
# abstractmethod means concrete subclasses must implement it.


import abc


class DataProcessor(abc.ABC):

    @abc.abstractmethod
    def validate(self, data: object) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: object) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return 0, "data"


class NumericProcessor(DataProcessor):

    def validate(self, data: object) -> bool:
        return isinstance(data, (int, float))

    def ingest(self, data: object) -> None:
        print(f"Numeric data: {data}")


processor = NumericProcessor()

print(processor.validate(42))
processor.ingest(42)
print(processor.output())


# DataProcessor() would fail because abstract methods
# have not been implemented.


# ==========================================================
# Polymorphism
# ==========================================================
# Different classes can be used through the same interface.


class Weapon(abc.ABC):

    @abc.abstractmethod
    def attack(self) -> None:
        pass


class Sword(Weapon):

    def attack(self) -> None:
        print("Sword attack")


class Bow(Weapon):

    def attack(self) -> None:
        print("Bow attack")


def perform_attack(weapon: Weapon) -> None:
    weapon.attack()


perform_attack(Sword())
perform_attack(Bow())


# ==========================================================
# Polymorphism in Data Processing
# ==========================================================

class Processor(abc.ABC):

    @abc.abstractmethod
    def validate(self, data: object) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: object) -> None:
        pass


class NumericDataProcessor(Processor):

    def validate(self, data: object) -> bool:
        return isinstance(data, (int, float))

    def ingest(self, data: object) -> None:
        print(f"Numeric: {data}")


class TextDataProcessor(Processor):

    def validate(self, data: object) -> bool:
        return isinstance(data, str)

    def ingest(self, data: object) -> None:
        print(f"Text: {data}")


def process_data(processor: Processor, data: object) -> None:

    if processor.validate(data):
        processor.ingest(data)


process_data(NumericDataProcessor(), 42)
process_data(TextDataProcessor(), "Hello")


# ==========================================================
# Composition
# ==========================================================
# Composition means one object contains another object.


class Engine:

    def start(self) -> None:
        print("Engine started")


class Car:

    def __init__(self) -> None:
        self.engine = Engine()

    def start(self) -> None:
        self.engine.start()
        print("Car started")


Car().start()


# ==========================================================
# Protocol
# ==========================================================
# Protocol describes what an object must provide.
# A class does not need to inherit from the Protocol.


from typing import Protocol


class ExportPlugin(Protocol):

    def process_output(self, data: list[str]) -> None:
        ...


class CSVPlugin:

    def process_output(self, data: list[str]) -> None:
        print(",".join(data))


class JSONPlugin:

    def process_output(self, data: list[str]) -> None:
        print(data)


def export_data(plugin: ExportPlugin, data: list[str]) -> None:
    plugin.process_output(data)


export_data(CSVPlugin(), ["one", "two", "three"])
export_data(JSONPlugin(), ["one", "two", "three"])


# ==========================================================
# Nested Class
# ==========================================================

class Outer:

    class Inner:

        def hello(self) -> None:
            print("Hello from Inner")


Outer.Inner().hello()


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python OOP reference")
