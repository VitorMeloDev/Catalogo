# Python OOP
# Classes, Objects, Inheritance, Composition and Polymorphism


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


def perform_attack(weapon: object) -> None:
    weapon.attack()


perform_attack(Sword())
perform_attack(Bow())


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
