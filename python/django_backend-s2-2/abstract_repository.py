import abc

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_all(self):
        ...

    @abc.abstractmethod
    def get_by_id(self, id):
        ...

    @abc.abstractmethod
    def create(self, instance):
        ...

    @abc.abstractmethod
    def update(self, id):
        ...

    @abc.abstractmethod
    def delete(self, id):
        ...
