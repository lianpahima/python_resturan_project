# import csv
# from Customer import Customer
# from Product import Product
# from Table import Table
# import unittest


# class OrderData:
#     def __init__(self, filename):
#         self.filename = filename

#     def save(self, orders):
#         with open(self.filename, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['order_id', 'table_id', 'products', 'total_amount', 'customer_id'])
#             for order in orders:
#                 writer.writerow([order.order_id, order.table_id, order.products, order.total_amount, order.customer_id])

#     def load(self):
#         orders = []
#         with open(self.filename, 'r', newline='') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 order_id = row['order_id']
#                 if not order_id:
#                     print("Empty order_id encountered. Setting it to -1.")
#                     order_id = -1
#                 else:
#                     try:
#                         order_id = int(order_id)
#                     except ValueError:
#                         print(f"Invalid order_id: {order_id}. Skipping the row.")
#                         continue

#                 table_id = int(row['table_id'])
#                 total_amount = int(row['total_amount'])
#                 orders.append(Order(order_id, table_id, row['products'], total_amount, row['customer_id']))
#         return orders


# class Order:
#     def __init__(self, order_id, table_id, products, total_amount, customer_id):
#         self.order_id = int(order_id)
#         self.table_id = int(table_id)
#         self.products = products
#         self.total_amount = total_amount
#         self.customer_id = customer_id


# class TestOrder(unittest.TestCase):
#     def setUp(self):
#         self.customer_id = Customer('Alin Pahima', 'email@example.com', '053-4648833', '12345')
#         self.table = Table(1, 5, 'available')
#         self.product1 = Product('Pasta', 65, False)
#         self.product2 = Product('Sushi', 72, True)

#     def test_add_product(self):
#         order = Order(1, self.table.table_id, [], 0, self.customer_id)
#         order.add_product(self.product1)
#         self.assertEqual(order.products, [self.product1])

#     def test_delete_product(self):
#         order = Order(1, self.table.table_id, [self.product1, self.product2], 0, self.customer_id)
#         order.delete_product(self.product1)
#         self.assertEqual(order.products, [self.product2])

#     def test_update_product_quantity(self):
#         order = Order(1, self.table.table_id, [self.product1], 0, self.customer_id)
#         order.update_product_quantity(self.product1, 2)
#         self.assertEqual(order.products[0].quantity, 2)

#     def test_get_total_amount(self):
#         order = Order(1, self.table.table_id, [self.product1, self.product2], 0, self.customer_id)
#         total = order.get_total_amount()
#         self.assertEqual(total, self.product1.price + self.product2.price)


# class Ordermain:
#     def __init__(self):
#         self.fileName = 'OrderData.csv'
#         self.orders = OrderData(self.fileName).load()
#         self.customer_id = Customer('Alin Pahima', 'email@example.com', '053-4648833', '12345')
#         self.products = []
#         self.table_id = None

#     def deleteById(self):
#         id = input("Enter order id to delete: ")

#         orderToRemove = None

#         for order in self.orders:
#             if order.order_id == str(id):
#                 orderToRemove = order
#                 break

#         if orderToRemove is not None:
#             self.orders.remove(orderToRemove)

#             with open(self.fileName, 'r') as file:
#                 rows = list(csv.reader(file))

#             for index, row in enumerate(rows):
#                 if index > 0 and row[0] == str(id):
#                     del rows[index]

#             with open(self.fileName, 'w', newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerows(rows)
#         else:
#             print(f"No order found with id: {id}")

#     def printAll(self):
#         for order in self.orders:
#             print(order.order_id, order.table_id, order.products, order.total_amount, order.customer_id)

#     def place_order(self, table_id, products, total_amount, reservation_status):
#         reservation_status = "confirmed"  # Assuming a default reservation status
#         self.customer_id.place_order(self.table_id, self.products, self.get_total_amount(), reservation_status)

#     def add_product(self):
#         product_name = input("Enter product name: ")
#         product_price = int(input("Enter product price: "))
#         product_quantity = int(input("Enter product quantity: "))
#         product = Product(product_name, product_price, True, product_quantity)
#         self.products.append(product)

#     def update_product_quantity(self):
#         product_name = input("Enter product name: ")
#         new_quantity = int(input("Enter new quantity: "))
#         for product in self.products:
#             if product.name == product_name:
#                 product.quantity = new_quantity
#                 print(f"Quantity updated for {product.name}")
#                 return
#         print(f"No product found with name: {product_name}")

#     def get_total_amount(self):
#         total = 0
#         for product in self.products:
#             total += product.price * product.quantity
#         return total

#     def run(self):
#         while True:
#             print("\nMenu Manager Options:")
#             print("1. Place Order")
#             print("2. Add Product")
#             print("3. Remove Product")
#             print("4. Update Product Quantity")
#             print("5. Get Total Amount")
#             print("6. Show All Orders")
#             print("7. Exit")

#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 self.place_order(self.table_id, self.products, self.get_total_amount(), self.reservation_status)
#             elif choice == '2':
#                 self.add_product()
#             elif choice == '3':
#                 self.deleteById()
#             elif choice == '4':
#                 self.update_product_quantity()
#             elif choice == '5':
#                 print(f"Total Amount: {self.get_total_amount()}")
#             elif choice == '6':
#                 self.printAll()
#             elif choice == '7':
#                 break
#             else:
#                 print("Invalid choice. Please try again.")


# if __name__ == '__main__':
#     unittest.main()

import csv
from Customer import Customer
from Product import Product,ProductData
from Table import Table
from Menu import Menu
import unittest


class OrderData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, orders):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['order_id', 'table_id', 'products', 'total_amount', 'customer_id', 'status'])
            for order in orders:
                writer.writerow([order.order_id, order.table_id, order.products, order.total_amount, order.customer_id, order.status])

    # def load(self):
    #     orders = []
    #     with open(self.filename, 'r', newline='') as file:
    #         reader = csv.DictReader(file)
    #         for row in reader:
    #             order_id = row['order_id']
    #             if not order_id:
    #                 print("Empty order_id encountered. Setting it to -1.")
    #                 order_id = -1
    #             else:
    #                 try:
    #                     order_id = int(order_id)
    #                 except ValueError:
    #                     print(f"Invalid order_id: {order_id}. Skipping the row.")
    #                     continue

    #             table_id = int(row['table_id'])
    #             total_amount = int(row['total_amount'])
    #             orders.append(Order(order_id, table_id, row['products'], total_amount, row['customer_id']))
    #     return orders


    def load(self):
        orders = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                order_id = row['order_id']
                if not order_id:
                    print("Empty order_id encountered. Setting it to -1.")
                    order_id = -1
                else:
                    try:
                        order_id = int(order_id)
                    except ValueError:
                        print(f"Invalid order_id: {order_id}. Skipping the row.")
                        continue

                table_id = int(row['table_id'])
                total_amount = int(row['total_amount'])
                orders.append(Order(order_id, table_id, row['products'], total_amount, row['customer_id'], row['status']))
        return orders



class Order:
    def __init__(self, order_id, table_id, products, total_amount, customer_id, status):
        self.order_id = order_id
        self.table_id = table_id
        self.products = products
        self.total_amount = total_amount
        self.customer_id = customer_id
        self.status = status

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer_id = Customer('Alin Pahima', 'email@example.com', '053-4648833', '12345')
        self.table = Table(1, 5, 'available')
        self.product1 = Product('Pasta', 65, False)
        self.product2 = Product('Sushi', 72, True)

    def test_add_product(self):
        order = Order(1, self.table.table_id, [], 0, self.customer_id)
        order.add_product(self.product1)
        self.assertEqual(order.products, [self.product1])

    def test_delete_product(self):
        order = Order(1, self.table.table_id, [self.product1, self.product2], 0, self.customer_id)
        order.delete_product(self.product1)
        self.assertEqual(order.products, [self.product2])

    def test_update_product_quantity(self):
        order = Order(1, self.table.table_id, [self.product1], 0, self.customer_id)
        order.update_product_quantity(self.product1, 2)
        self.assertEqual(order.products[0].quantity, 2)

    def test_get_total_amount(self):
        order = Order(1, self.table.table_id, [self.product1, self.product2], 0, self.customer_id)
        total = order.get_total_amount()
        self.assertEqual(total, self.product1.price + self.product2.price)

class Ordermain:
    def __init__(self):
        self.fileName = 'OrderData.csv'
        self.Order_data = OrderData(self.fileName)
        self.orders = self.Order_data.load()
        product_data = ProductData ('ProductData.csv')
        self.products = product_data.load()



    def deleteById(self):
        id = input("Enter order id to delete: ")

        try:
            id = int(id)
        except ValueError:
            print("Invalid order id. Please enter a valid integer.")
            return

        orderToRemove = None

        for order in self.orders:
            if order.order_id == id:
                orderToRemove = order
                break

        if orderToRemove is not None:
            self.orders.remove(orderToRemove)

            with open(self.fileName, 'r') as file:
                rows = list(csv.reader(file))

            for index, row in enumerate(rows):
                if index > 0 and row[0] == str(id):
                    del rows[index]

            with open(self.fileName, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        else:
            print(f"No order found with id: {id}")

    def printAll(self):
        for order in self.orders:
            print(order.order_id, order.table_id, order.products, order.total_amount, order.customer_id, order.status)

    def place_order(self):
        reservation_status = "confirmed"
        order_id = input("Enter order id: ")

        try:
            order_id = int(order_id)
        except ValueError:
            print("Invalid order id. Please enter a valid integer.")
            return

        for order in self.orders:
            if order.order_id == order_id:
                order.status = reservation_status
                print("Update succeeded!")
                break
        else:
            print(f"No order found with id: {order_id}")

        self.Order_data.save(self.orders)

    def clear_order(self):
        reservation_status = "finished"
        order_id = input("Enter order id: ")

        try:
            order_id = int(order_id)
        except ValueError:
            print("Invalid order id. Please enter a valid integer.")
            return

        for order in self.orders:
            if order.order_id == order_id:
                order.status = reservation_status
                print("Update succeeded!")
                break
        else:
            print(f"No order found with id: {order_id}")

        self.Order_data.save(self.orders)

        product_name = input("Enter product name: ")
        product_price = input("Enter product price: ")
        product_quantity = input("Enter product quantity: ")
        product_customer_id = input("Enter product customer id: ")

        try:
            product_price = int(product_price)
            product_quantity = int(product_quantity)
            product_customer_id = int(product_customer_id)
        except ValueError:
            print("Invalid input for product details. Please enter valid integers for price, quantity, and customer id.")
            return

        product = Product(product_name, product_price, True, product_quantity, product_customer_id)
        self.products.append(product)

    def update_product_quantity(self):
        product_name = input("Enter product name: ")
        new_quantity = input("Enter new quantity: ")

        try:
            new_quantity = int(new_quantity)
        except ValueError:
            print("Invalid quantity. Please enter a valid integer.")
            return

        for product in self.products:
            if product.name == product_name:
                product.quantity = new_quantity
                print(f"Quantity updated for {product.name}")
                return
        else:
            print(f"No product found with name: {product_name}")

    def get_total_amount(self,products):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

    def run(self):
        while True:
            print("\nMenu Manager Options:")
            print("1. Place Order")
            print("2. Remove Product")
            print("3. Update Product Quantity")
            print("4. Get Total Amount")
            print("5. Show All Orders")
            print("6. Finish Order")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.place_order()
            elif choice == '2':
                self.deleteById()
            elif choice == '3':
                self.update_product_quantity()
            elif choice == '4':
                print(f"Total Amount: {self.get_total_amount()}")
            elif choice == '5':
                self.printAll()
            elif choice == '6':
                self.clear_order()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")
