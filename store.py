from inventory import Inventory


class Store:
    def __init__(self):
        self._inventory = Inventory()
        self._order_processor = OrderProcessor()