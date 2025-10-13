from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def say(self):
        pass

class personA(Person):
    def __str__(self):
        return "Ismail"
    def walk(self):
        print(f"{self} go for a walk")
    def run(self):
        print(f"{self} go for a run")
    def say(self):
        print(f"{self} can talk")

personA().walk()
