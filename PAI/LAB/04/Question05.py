class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = {}
        self.customer_orders = {}
    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price
        print(f"{item_name} added to the menu for ${price}.")
    def book_tables(self, table_number, customer_name):
        self.book_table[table_number] = customer_name
        print(f"Table {table_number} booked for {customer_name}.")
    def customer_order(self, table_number, order):
        if table_number in self.book_table:
            self.customer_orders[table_number] = order
            print(f"Order taken for table {table_number}: {order}.")
        else:
            print("Table not booked. Please book a table first.")
    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_table_reservations(self):
        print("Table Reservations:")
        for table, customer in self.book_table.items():
            print(f"Table {table}: {customer}")
    def print_customer_orders(self):
        print("Customer Orders:")
        for table, order in self.customer_orders.items():
            print(f"Table {table}: {order}")

restaurant = Restaurant()

restaurant.add_item_to_menu("Burger", 10.99)
restaurant.add_item_to_menu("Pizza", 14.99)
restaurant.add_item_to_menu("Salad", 8.99)

restaurant.book_tables(1, "Talha Rusman")
restaurant.book_tables(2, "Naveed")
restaurant.book_tables(3, "Rao")
restaurant.customer_order(1, "Burger and Fries")
restaurant.customer_order(2, "Pizza and Salad")

restaurant.customer_order(3, "Salad and Drink")

restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()