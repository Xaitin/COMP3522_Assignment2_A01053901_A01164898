import pandas as pd
from order import Order
from christmasproductfactory import ChristmasProductFactory
from easterproductfactory import EasterProductFactory
from spookyproductfactory import SpookyProductFactory


class OrderProcessor:
    def __init__(self):
        self._order_list = []

    def get_orders(self):
        return self._order_list

    def read_order_file(self, file_name):
        orders = pd.read_excel(file_name)
        #print('Excel Sheet to Dict:', orders.to_dict(orient='records'))
        details = orders.drop(['holiday'], ['order_number'], ['product_id'], ['item'], ['name'])
        details = details.to_dict(orient='records')
        orders = orders.to_dict(orient='records')
        for order in orders:
            if order['holiday'] == 'Christmas':
                factory = ChristmasProductFactory
            elif order['holiday'] == 'Easter':
                factory = EasterProductFactory
            else:
                factory = SpookyProductFactory

            new_order = Order(order['order_number'], order['product_id'], order['quantity'], order['item'],
                              order['name'], details, factory)
            self._order_list.append(new_order)
