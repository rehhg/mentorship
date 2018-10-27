

class Car(object):

    @staticmethod
    def factory(type_):
        if type_ == "Racecar":
            return Racecar()
        if type_ == "Van":
            return Van()
        return Exception(f'Bad car creation: {type_}')


class Racecar(Car):
    def drive(self):
        return 'Racecar driving.'

    def __str__(self):
        return self.drive


class Van(Car):
    def drive(self):
        return 'Van driving.'

    def __str__(self):
        return self.drive


# Create object using factory.
obj = Car.factory("Van")
print(obj.drive())
