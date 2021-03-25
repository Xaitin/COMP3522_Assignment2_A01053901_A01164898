from abc import ABC, abstractmethod


class StuffedAnimals(ABC):

    @property
    @abstractmethod
    def stuffing(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass

    @property
    @abstractmethod
    def fabric(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def product_id(self):
        pass
