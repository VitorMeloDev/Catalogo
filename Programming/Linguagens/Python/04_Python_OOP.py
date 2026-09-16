# Python OOP
# Classes, Objects, Inheritance, Composition, Abstraction and Polymorphism


# ==========================================================
# Class and Object
# ==========================================================

class Player:
    pass


player = Player()

print(type(player))


# ==========================================================
# Constructor
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

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount


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


enemy1 = Enemy("Goblin")
enemy2 = Enemy("Orc")

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
# Abstract Base Class (ABC)
# ==========================================================

import abc


class DataProcessor(abc.ABC):

    @abc.abstractmethod
    def validate(self, data: object) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: object) -> None:
        pass

    def output(self) -> None:
        print("Output data")


class NumericProcessor(DataProcessor):

    def validate(self, data: object) -> bool:
        return isinstance(data, (int, float))

    def ingest(self, data: object) -> None:
        print(f"Ingesting numeric data: {data}")


processor = NumericProcessor()

print(processor.validate(42))
processor.ingest(42)
processor.output()


# ==========================================================
# Abstract Class Cannot Be Instantiated
# ==========================================================

class AnimalProcessor(abc.ABC):

    @abc.abstractmethod
    def process(self, data: str) -> None:
        pass


# AnimalProcessor()  # TypeError: abstract class


class DogProcessor(AnimalProcessor):

    def process(self, data: str) -> None:
        print(f"Processing dog data: {data}")


dog_processor = DogProcessor()

dog_processor.process("Dog")


# ==========================================================
# Method Overriding
# ==========================================================

class Enemy:

    def attack(self) -> None:
        print("Generic attack")


class Goblin(Enemy):

    def attack(self) -> None:
        print("Goblin attack")


enemy = Goblin()

enemy.attack()


# ==========================================================
# Polymorphism
# ==========================================================

class Sword:

    def attack(self) -> None:
        print("Sword attack")


class Bow:

    def attack(self) -> None:
        print("Bow attack")


def perform_attack(weapon: Sword | Bow) -> None:
    weapon.attack()


perform_attack(Sword())
perform_attack(Bow())


# ==========================================================
# Polymorphism Through a Common Base Class
# ==========================================================

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


def use_weapon(weapon: Weapon) -> None:
    weapon.attack()


use_weapon(Sword())
use_weapon(Bow())


# ==========================================================
# Polymorphism With Data Processors
# ==========================================================

class Processor(abc.ABC):

    @abc.abstractmethod
    def validate(self, data: object) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: object) -> None:
        pass


class NumericProcessor(Processor):

    def validate(self, data: object) -> bool:
        return isinstance(data, (int, float))

    def ingest(self, data: object) -> None:
        print(f"Numeric processor: {data}")


class TextProcessor(Processor):

    def validate(self, data: object) -> bool:
        return isinstance(data, str)

    def ingest(self, data: object) -> None:
        print(f"Text processor: {data}")


def process_data(
    processor: Processor,
    data: object
) -> None:

    if processor.validate(data):
        processor.ingest(data)


process_data(NumericProcessor(), 42)
process_data(TextProcessor(), "Hello")


# ==========================================================
# Composition
# ==========================================================

class Engine:

    def start(self) -> None:
        print("Engine started")


class Car:

    def __init__(self) -> None:
        self.engine = Engine()

    def start(self) -> None:
        self.engine.start()
        print("Car started")


car = Car()

car.start()


# ==========================================================
# Protocol
# ==========================================================

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


def export_data(
    plugin: ExportPlugin,
    data: list[str]
) -> None:

    plugin.process_output(data)


csv_plugin = CSVPlugin()
json_plugin = JSONPlugin()

export_data(csv_plugin, ["one", "two", "three"])
export_data(json_plugin, ["one", "two", "three"])


# ==========================================================
# Protocol Does Not Require Inheritance
# ==========================================================

class Logger(Protocol):

    def log(self, message: str) -> None:
        ...


class ConsoleLogger:

    def log(self, message: str) -> None:
        print(message)


class FileLogger:

    def log(self, message: str) -> None:
        print(f"Writing to file: {message}")


def write_log(logger: Logger, message: str) -> None:
    logger.log(message)


write_log(ConsoleLogger(), "Application started")
write_log(FileLogger(), "Application started")


# ==========================================================
# Nested Class
# ==========================================================

class Outer:

    class Inner:

        def hello(self) -> None:
            print("Hello from Inner")


inner = Outer.Inner()

inner.hello()


# ==========================================================
# Standalone Functions with Objects
# ==========================================================

class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height


def area(rectangle: Rectangle) -> float:
    return rectangle.width * rectangle.height


rectangle = Rectangle(10, 5)

print(area(rectangle))


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    print("Python OOP reference")
