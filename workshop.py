from toys import Toys


class Workshop(Toys):

    def __init__(self, battery, min_age, name, description, p_id, width, height, rooms):
        self._is_battery_operated = battery
        self._min_rec_age = min_age
        self._name = name
        self._description = description
        self._product_id = p_id
        self._width = width
        self._height = height
        self._rooms = rooms

    @property
    def is_battery_operated(self):
        return self._is_battery_operated

    @property
    def min_rec_age(self):
        return self._min_rec_age

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def product_id(self):
        return self._product_id

