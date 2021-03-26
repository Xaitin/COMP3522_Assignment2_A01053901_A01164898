from productfactory import ProductFactory
from skeleton import Skeleton
from spider import Spider
from toffee import Toffee


class SpookyProductFactory(ProductFactory):

    def create_candy(self, item):
        other_info = item.get_details()
        return Toffee(other_info['has_nuts'], other_info['has_lactose'], item.get_name(), other_info['description'],
                      item.get_product_id(), other_info['variety'])

    def create_toy(self, item):
        other_info = item.get_details()
        return Spider(other_info['has_batteries'], other_info['min_age'], item.get_name(), other_info['description'],
                      item.get_product_id(), other_info['speed'], other_info['jump_height'], other_info['has_glow'],
                      other_info['spider_type'])

    def create_stuffed_animal(self, item):
        other_info = item.get_details()
        return Skeleton(other_info['stuffing'], other_info['size'], other_info['fabric'], item.get_name(),
                        other_info['description'], item.get_product_id(), other_info['has_glow'])
