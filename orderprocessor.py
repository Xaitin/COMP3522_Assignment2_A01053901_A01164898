import pandas as pd
from order import Order
from xmasfactory import xmasFactory
from easterfactory import easterFactory
from spookyfactory import spookyFactory


class OrderProcessor:
    def __init__(self):
        self._order_list = []

    def get_orders(self):
        return self._order_list

    def read_order_file(self, file_name):
        orders = pd.read_excel(file_name)
        print('Excel Sheet to Dict:', orders.to_dict(orient='records'))
        orders = orders.to_dict(orient='records')
        for order in orders:
            factory = factoryBuilder()

            details = order.drop(['holiday'], ['order_number'], ['product_id'], ['item'], ['name'])
            new_order = Order(order['order_number'], order['product_id'], order['item'],
                              order['name'], details, factory)
            self._order_list.append(new_order)
