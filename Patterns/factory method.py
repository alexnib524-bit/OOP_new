from abc import ABC, abstractmethod

# 1. Абстрактный класс Animal
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# 2. Конкретные классы животных
class Lion(Animal):
    def make_sound(self):
        return "Рычание!"

class Monkey(Animal):
    def make_sound(self):
        return "Визг!"

class Elephant(Animal):
    def make_sound(self):
        return "Фырканье!"

# 3. Абстрактная фабрика AnimalFactory
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

# 4. Конкретные фабрики
class LionFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Lion()

class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Monkey()

class ElephantFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Elephant()

# 5. Функция для взаимодействия с животным
def interact_with_animal(factory: AnimalFactory):
    animal = factory.create_animal()
    print(f"Звук: {animal.make_sound()}")