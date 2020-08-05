"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):

        self.name = name

    @abstractmethod
    def call(self):
        pass


class Bird(Animal):

    def call(self):

        print(self.name, ': Cik cik...')

class Dog(Animal):

    def call(self):

        print(self.name, ': Hav hav...')



if __name__ == '__main__':

    bird = Bird('Sarı rüzgar')
    bird.call()

    dog = Dog('Karabaş')
    dog.call()