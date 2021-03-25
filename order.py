class Order:

    def __init__(self, ord_num, prod_id, type, name, details, factory):
        self._ord_num = ord_num
        self._prod_id = prod_id
        self._type = type
        self._name = name
        self._details = details
        self._factory = factory

    def get_order_number(self):
        return self._ord_num

    def get_product_id(self):
        return self._prod_id

    def get_type(self):
        return self._type

    def get_name(self):
        return self._name

    def get_details(self):
        return self._details

    def factory(self):
        return self._factory