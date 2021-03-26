from InvalidDataError import InvalidDataError
from productfactory import ProductFactory
from eggs import Eggs
from eBunny import EBunny
from rbunny import RBunny


class EasterProductFactory(ProductFactory):

    def create_candy(self, item):
        # Creating creme eggs for easter.
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        has_lactose = other_info['has_lactose']
        has_nuts = other_info['has_nuts']
        pack_size = other_info['pack_size']
        if has_lactose != "N":
            raise InvalidDataError("Creme Eggs must be Lactose Free")
        elif has_nuts != "Y":
            raise InvalidDataError("Creme Eggs may have nuts")
        return Eggs(has_nuts, has_lactose, name, description, product_id, pack_size)

    def create_toy(self, item):
        # creating Robot Bunnies for easter
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        color = other_info['colour']
        num_effects = other_info['num_sound']
        min_age = other_info['min_age']
        has_batteries = other_info['has_batteries']
        if has_batteries != "Y":
            raise InvalidDataError("Robot Bunnies need Batteries")
        if color != "Orange" or color != "Blue" or color != "Pink":
            raise InvalidDataError("Robot Bunnies must be Orange Blue or Pink")
        return RBunny(has_batteries, min_age, name, description, product_id, num_effects, color)

    def create_stuffed_animal(self, item):
        # creating Easter Bunnies for easter
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        fabric = other_info['fabric']
        size = other_info['size']
        stuffing = other_info['stuffing']
        color = other_info['colour']
        if fabric != "Linen":
            raise InvalidDataError("Easter Bunnies must be made out of Linen")
        if stuffing != "Polyester Fiberfill":
            raise InvalidDataError("Easter Bunnies must be stuffed with Polyester Fiberfill")
        return EBunny(stuffing, size, fabric, name, description, product_id, color)
