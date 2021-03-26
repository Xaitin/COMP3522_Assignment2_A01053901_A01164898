from stuffedanimals import StuffedAnimals


class Skeleton(StuffedAnimals):
    def __init__(self, stuffing, size, fabric, name, description, p_id):
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric
        self._name = name
        self._description = description
        self._product_id = p_id
        self._glows = True

    @property
    def stuffing(self):
        return self._stuffing

    @property
    def size(self):
        return self._size

    @property
    def fabric(self):
        return self._fabric

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def product_id(self):
        return self._product_id
