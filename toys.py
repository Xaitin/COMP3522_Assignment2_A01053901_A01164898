from abc import ABC, abstractmethod


class Toys(ABC):

    @property
    @abstractmethod
    def is_battery_operated(self):
        pass

    @property
    @abstractmethod
    def min_rec_age(self):
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
