from InvalidDataError import InvalidDataError
from orderprocessor import OrderProcessor
from enum import Enum
from datetime import datetime


class Stock(Enum):
    OUT_OF_STOCK = 0
    IN_STOCK = 9
    LOW = 10
    VERY_LOW = 3


class Store:
    def __init__(self):
        self._inventory = list()
        self._order_processor = OrderProcessor()
        self._order_list = None
        self._transaction_list = list()

    def display_menu(self):

        user_input = None
        while user_input != 3:
            print("\nWelcome to Cloud9 Superstore Terminal")
            print("-----------------------")
            print("1. Process Web Orders")
            print("2. Check Inventory")
            print("3. Exit and print daily transactions")
            string_input = input("Please enter your choice (1-3)")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                executing = True
                while executing:
                    executing = self.execute_order_processor()
            elif user_input == 2:
                self.check_inventory()
            elif user_input == 3:
                self.print_transactions_to_file()
            else:
                print("Incorrect input. Displaying menu.")

        print("Thank you for using the Cloud9 Superstore Terminal")

    def add_to_inventory(self, param):
        self._inventory.append(param)

    def execute_order_processor(self):
        correct_file = False
        try:
            file_name = input("Please enter the name of the excel file to process (without extension)")
            self._order_list = self._order_processor.read_order_file(file_name + ".xlsx")
            correct_file = True
            for order in self._order_list:
                product_id = order.get_product_id()
                num_in_stock = 0
                factory = order.factory()
                item_type = order.get_type()
                for item in self._inventory:
                    id_to_check = item.product_id()
                    if product_id == id_to_check:
                        num_in_stock += 1
                qty_to_order = int(order.get_quantity())
                if qty_to_order > num_in_stock:
                    try:
                        for i in range(100):
                            if item_type == "Toy":
                                self.add_to_inventory(factory.create_toy(order))
                            elif item_type == "Candy":
                                self.add_to_inventory(factory.create_candy(order))
                            else:
                                self.add_to_inventory(factory.create_stuffed_animal(order))
                    except InvalidDataError as e:
                        self._transaction_list.append(order.get_order_number() + e.message)
                try:
                    for i in range(qty_to_order):
                        if item_type == "Toy":
                            self.remove_from_inventory(factory.create_toy(order))
                        elif item_type == "Candy":
                            self.remove_from_inventory(factory.create_candy(order))
                        else:
                            self.remove_from_inventory(factory.create_stuffed_animal(order))
                except InvalidDataError as e:
                    self._transaction_list.append(order.get_order_number() + e.message)
                name = order.get_name()
                order_num = order.get_order_number()
                self._transaction_list.append("{0}, Item {1}, Product ID {2}, Name {3}, Quantity {4}".format(
                    order_num, item_type, product_id, name, qty_to_order
                ))

        except FileNotFoundError:
            print("File name not found")
        return correct_file

    def check_inventory(self):
        list_of_ids = list()
        list_of_counters = list()
        for item in self._inventory:
            p_id = item.product_id()
            if p_id not in list_of_ids:
                list_of_ids.append(p_id)
                list_of_counters.append(1)
            else:
                index_to_increment = list_of_ids.index(p_id)
                list_of_counters[index_to_increment] += 1
        output = ""
        for i in range(len(list_of_ids)):
            qty = list_of_counters[i]
            item_id = list_of_ids[i]
            if qty == Stock.OUT_OF_STOCK.value:
                output += item_id + " is Out of Stock\n"
            elif qty < Stock.VERY_LOW.value:
                output += item_id + " is Very Low in Stock\n"
            elif qty < Stock.LOW.value:
                output += item_id + " is Low in Stock\n"
            elif qty > Stock.IN_STOCK.value:
                output += item_id + " is in Stock\n"
        if output == "":
            print("Inventory is empty")
        else:
            print(output)

    def print_transactions_to_file(self):
        timestamp = datetime.today().strftime('%d%m%y_%H%M')
        filename = 'DTR_' + timestamp
        file = open(filename, 'w')
        file.write('CLOUD9 SUPERSTORE - DAILY TRANSACTION REPORT')
        file.write(datetime.today().strftime('%d-%m-%Y %H%M'))
        file.writelines('%s\n' % transaction for transaction in self._transaction_list)
        file.close()

    def remove_from_inventory(self, param):
        self._inventory.remove(param)
