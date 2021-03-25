from abc import ABC, abstractmethod


class Candy(ABC):

    @property
    @abstractmethod
    def has_nuts(self):
        pass

    @property
    @abstractmethod
    def lactose_free(self):
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
