from abc import ABC, abstractmethod


class ProductFactory(ABC):

    @abstractmethod
    def create_candy(self, item):
        pass

    @abstractmethod
    def create_toy(self, item):
        pass

    @abstractmethod
    def create_stuffed_animal(self, item):
        pass
