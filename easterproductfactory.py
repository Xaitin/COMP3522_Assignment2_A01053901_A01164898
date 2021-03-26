from productfactory import ProductFactory
from toffee import Toffee
from eBunny import eBunny
from rbunny import rBunny


class EasterProductFactory(ProductFactory):

    def create_candy(self, item):
        # Creating creme eggs for easter.
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        has_lactose = other_info['has_lactose']
        has_nuts = other_info['has_nuts']
        variety = other_info['variety']
        if variety != "Sea Salt" or variety != "Regular":
            variety = "Sea Salt"
        return Toffee(has_nuts, has_lactose, name, description, product_id, variety)

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
        return rBunny(has_batteries, min_age, name, description, product_id, num_effects, color)

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
        return eBunny(stuffing, size, fabric, name, description, product_id, color)
