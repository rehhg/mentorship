from abc import abstractmethod


class AbstractInterface:
    """ Target interface.
    This is the target interface, that clients use.
    """

    def some_functionality(self):
        pass


class Bridge(AbstractInterface):
    """ Bridge class.

    This class forms a bridge between the target
    interface and background implementation.
    """

    def __init__(self):
        self.__implementation = None


class UseCase1(Bridge):
    """ Variant of the target interface.
    This is a variant of the target Abstract interface.
    It can do something little differently and it can
    also use various background implementations through
    the bridge.
    """

    def __init__(self, implementation):
        self.__implementation = implementation

    def some_functionality(self):
        print('UseCase1: ', self.__implementation.another_functionality())


class UseCase2(Bridge):
    def __init__(self, implementation):
        self.__implementation = implementation

    def some_functionality(self):
        print('UseCase2: ', self.__implementation.another_functionality())


class ImplementationInterface:
    """ Interface for the background implementation.
    This class defines how the Bridge communicates
    with various background implementations.
    """

    @abstractmethod
    def another_functionality(self):
        pass


class Linux(ImplementationInterface):
    """ Concrete background implementation.
    A variant of background implementation, in this
    case for Linux!
    """

    def another_functionality(self):
        return 'Linux!'


class Windows(ImplementationInterface):
    def another_functionality(self):
        return 'Windows.'


def main():
    linux = Linux()
    windows = Windows()

    # Couple of variants under a couple
    # of operating systems.
    use_case = UseCase1(linux)
    use_case.some_functionality()

    use_case = UseCase1(windows)
    use_case.some_functionality()

    use_case = UseCase2(linux)
    use_case.some_functionality()

    use_case = UseCase2(windows)
    use_case.some_functionality()


if __name__ == "__main__":
    main()
