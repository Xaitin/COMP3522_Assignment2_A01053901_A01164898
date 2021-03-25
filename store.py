from orderprocessor import OrderProcessor
from enum import Enum


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
                pass
            else:
                print("Incorrect input. Displaying menu.")

        print("Thank you for using the Cloud9 Superstore Terminal")

    def execute_order_processor(self):
        correct_file = False
        try:
            file_name = input("Please enter the name of the excel file to process (without extension)")
            self._order_list = self._order_processor.process_order(file_name + ".xlsx")
            correct_file = True
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
        print(output)


