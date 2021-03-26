from InvalidDataError import InvalidDataError
from productfactory import ProductFactory
from workshop import Workshop
from reindeer import Reindeer
from canes import Canes


class ChristmasProductFactory(ProductFactory):

    def create_candy(self, item):
        # Creating Candy Canes for Christmas.
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        has_lactose = other_info['has_lactose']
        has_nuts = other_info['has_nuts']
        color = other_info['colour']
        if has_lactose != "N":
            raise InvalidDataError("Candy Canes are Lactose Free")
        elif has_nuts != "N":
            raise InvalidDataError("Candy Canes are Nut Free")
        return Canes(has_nuts, has_lactose, name, description, product_id, color)

    def create_toy(self, item):
        # creating Santa's Workshops for Christmas
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        dimensions = other_info['dimensions']
        rooms = other_info['num_rooms']
        formatted = dimensions.split(',')
        height = formatted[0]
        width = formatted[1]
        min_age = other_info['min_age']
        has_batteries = other_info['has_batteries']
        if has_batteries != "N":
            raise InvalidDataError("Santa's Workshop doesnt need batteries")
        return Workshop(has_batteries, min_age, name, description, product_id, height, width, rooms)

    def create_stuffed_animal(self, item):
        # creating Reindeer for Christmas
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        fabric = other_info['fabric']
        size = other_info['size']
        stuffing = other_info['stuffing']
        glow = other_info['has_glow']
        if fabric != "Cotton":
            raise InvalidDataError("Reindeer Fabric must be Cotton")
        elif stuffing != "Wool":
            raise InvalidDataError("Reindeer Stuffing must be Wool")
        elif glow != "Y":
            raise InvalidDataError("Reindeer have Glow in the Dark Noses")
        return Reindeer(stuffing, size, fabric, name, description, product_id, glow)
