from abc import abstractmethod


class AbstractAdapter:
    @abstractmethod
    def request(self):
        pass


class Adapter(AbstractAdapter):
    def __init__(self):
        self.service = Service()

    def request(self):
        print('Inside Adapter:request()')
        self.service.service_request()


class Service:
    def service_request(self):
        print('Inside Service:service_request()')


adapter = Adapter()
adapter.request()
