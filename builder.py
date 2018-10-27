

class Director:
    """
    Construct an object using the Builder interface.
    """

    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    # The algorithm for assembling a car
    def get_car(self):
        car = Car()

        # First goes the body
        body = self.__builder.get_body()
        car.set_body(body)

        # Then engine
        engine = self.__builder.get_engine()
        car.set_engine(engine)

        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)
            i += 1

        return car


# The whole product
class Car:
    """ The final product.
    A car is assembled by the `Director' class from
    parts made by `Builder'. Both these classes have
    influence on the resulting object.
    """

    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)


class Builder:
    """ Creates various parts of a vehicle.
    This class is responsible for constructing all
    the parts for a vehicle.
    """

    def get_wheel(self):
        pass

    def get_engine(self):
        pass

    def get_body(self):
        pass


class JeepBuilder(Builder):
    """ Concrete Builder implementation.
    This class builds parts for Jeep's SUVs.
    """

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body


class NissanBuilder(Builder):
    """ Concrete Builder implementation.
    This class builds parts for Nissan's family cars.
    """

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 85
        return engine

    def get_body(self):
        body = Body()
        body.shape = "hatchback"
        return body


# Car parts
class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


def main():
    jeep_builder = JeepBuilder()
    nissan_builder = NissanBuilder()

    director = Director()

    # Build Jeep
    print('Jeep')
    director.set_builder(jeep_builder)
    jeep = director.get_car()
    jeep.specification()

    print('\n')

    # Build Nissan
    print('Nissan')
    director.set_builder(nissan_builder)
    nissan = director.get_car()
    nissan.specification()


if __name__ == "__main__":
    main()
