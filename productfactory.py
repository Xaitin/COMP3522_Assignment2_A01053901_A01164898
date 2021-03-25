from abc import ABC, abstractmethod


class ProductFactory(ABC):

    @abstractmethod
    def create_candy(self):
        pass

    @abstractmethod
    def create_toy(self):
        pass

    @abstractmethod
    def create_stuffed_animal(self):
        pass
