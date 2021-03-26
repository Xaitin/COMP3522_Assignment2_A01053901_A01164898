from InvalidDataError import InvalidDataError
from productfactory import ProductFactory
from skeleton import Skeleton
from spider import Spider
from toffee import Toffee


class SpookyProductFactory(ProductFactory):

    def create_candy(self, item):
        other_info = item.get_details()
        if other_info['has_nuts'] != 'Y':
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError - has_nuts can only be Y")
        if other_info['has_lactose'] != 'Y':
            raise InvalidDataError("Could Not process order data corrupted, "
                                   "InvalidDataError - has_lactose can only be Y")
        if other_info['variety'] != 'Regular' or other_info['variety'] != 'Sea Salt':
            raise InvalidDataError("Could Not process order data corrupted, "
                                   "InvalidDataError - variety can only be Regular or Sea Salt")
        return Toffee(other_info['has_nuts'], other_info['has_lactose'], item.get_name(), other_info['description'],
                      item.get_product_id(), other_info['variety'])

    def create_toy(self, item):
        other_info = item.get_details()
        if other_info['has_batteries'] != 'Y':
            raise InvalidDataError("Could Not process order data corrupted, "
                                   "InvalidDataError - has_batteries can only be Y")
        if other_info['spider_type'] != 'Tarantula' or other_info['spider_type'] != 'Wolf Spider':
            raise InvalidDataError("Could Not process order data corrupted, "
                                   "InvalidDataError - spider_type can only be Tarantula or Wolf")
        return Spider(other_info['has_batteries'], other_info['min_age'], item.get_name(), other_info['description'],
                      item.get_product_id(), other_info['speed'], other_info['jump_height'], other_info['has_glow'],
                      other_info['spider_type'])

    def create_stuffed_animal(self, item):
        other_info = item.get_details()
        if other_info['stuffing'] != 'Polyester Fibrefill':
            raise InvalidDataError("Could Not process order data corrupted, "
                                   "InvalidDataError - stuffing can only be Polyester Fibrefill")
        if other_info['fabric'] != 'Acrylic':
            raise InvalidDataError("Could Not process order data corrupted, "
                                   "InvalidDataError - fabric can only be Acrylic")
        if other_info['has_glow'] != 'Y':
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError - has_glow can only be Y")
        return Skeleton(other_info['stuffing'], other_info['size'], other_info['fabric'], item.get_name(),
                        other_info['description'], item.get_product_id(), other_info['has_glow'])
