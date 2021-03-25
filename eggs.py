from candy import Candy


class Eggs(Candy):
    def __init__(self, nuts, lactose, name, description, p_id, pack_size):
        self._has_nuts = nuts
        self._lactose_free = lactose
        self._name = name
        self._description = description
        self._product_id = p_id
        self._pack_size = pack_size

    @property
    def has_nuts(self):
        return self._has_nuts

    @property
    def lactose_free(self):
        return self._lactose_free

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def product_id(self):
        return self._product_id
