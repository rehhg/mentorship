from abc import abstractmethod


class AbstractFactory(object):

    @abstractmethod
    def create_drink(self):
        pass

    @abstractmethod
    def create_food(self):
        pass


class Drink(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Food(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ConcreteFactory1(AbstractFactory):
    def create_drink(self):
        return Drink('Coca-cola')

    def create_food(self):
        return Food('Hamburger')


class ConcreteFactory2(AbstractFactory):
    def create_drink(self):
        return Drink('Kampot')

    def create_food(self):
        return Food('Golubci')


def get_factory(id):
    if id == 1:
        return ConcreteFactory1()
    elif id == 2:
        return ConcreteFactory2()


factory = get_factory(1)
print(factory.create_drink())  # Coca-cola
print(factory.create_food())  # Hamburger
