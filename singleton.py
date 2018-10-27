

# a decorator recommended in PEP
def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance


@singleton
class MyClass:
    pass


# Singleton as a base class
class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance


# metaclass
class SingletonMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMetaClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyMetaSingletonClass(metaclass=SingletonMetaClass):
    pass


# TEST 1

s = MyClass()
s1 = MyClass()
s2 = MyClass()

print(s, s1, s2)  # return 3 the same objects

# TEST 2
s = Singleton()  # Ok
# s2 = Singleton() will raise exception
print(s)

s = Singleton.get_instance()
print(s)

s = Singleton.get_instance()
print(s) # will print the same instance as before

# TEST 3
# always returns the same object, even after new initialization
s = MyMetaSingletonClass()
print(s)
s1 = MyMetaSingletonClass()
print(s1)
s2 = MyMetaSingletonClass()
print(s2)