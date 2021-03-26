from abc import ABC, abstractmethod


class ProductFactory(ABC):

    @classmethod
    @abstractmethod
    def create_candy(cls, item):
        pass

    @classmethod
    @abstractmethod
    def create_toy(cls, item):
        pass

    @classmethod
    @abstractmethod
    def create_stuffed_animal(cls, item):
        pass
