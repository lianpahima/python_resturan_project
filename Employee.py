from Reservation import Reservation
from Person import Person
from Menu import Menu
from Order import Order
import csv
# from pathlib import Path


class EmployeeData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, employees):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'phone', 'email', 'id', 'position','salary'])
            for employee in employees:
                writer.writerow([employee.name, employee.phone, employee.email, employee.id, employee.position, employee.salary])

    def load(self):
        employees = []
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name, phone, email, id, position, salary = row
                employee = Employee(name, phone, email, id, position, salary)
                employees.append(employee)
        return employees

class Employee(Person):
    def __init__ (self, name, phone, email, id, position, salary):
        super().__init__(name, phone, email, id)
        self.position = position
        self.salary = salary
        self.orders = []
        self.reservations = []
        self.inventory = Menu()

    def create_order(self, table_id, product_names):
        products = []
        total_amount = 0
        for name in product_names:
            product = self.inventory.find_product(name)
            if product:
                products.append(product)
                total_amount += product.price
        if not products:
            return None
        order_id = len(self.orders) + 1
        order = Order(order_id, table_id, products, total_amount)
        self.orders.append(order)
        return order

    def update_order(self, order_id, product_names):
        order = self.find_order(order_id)
        if not order:
            return False
        products = []
        total_amount = 0
        for name in product_names:
            product = self.inventory.find_product(name)
            if product:
                products.append(product)
                total_amount += product.price
        if not products:
            return False
        order.products = products
        order.total_amount = total_amount
        return True

    def delete_order(self, order_id):
        order = self.find_order(order_id)
        if not order:
            return False
        self.orders.remove(order)
        return True

    def view_inventory(self):
        return self.inventory.products

    def manage_reservation(self, customer_id, table_id, reservation_time):
        reservation_id = len(self.reservations) + 1
        reservation = Reservation(reservation_id, customer_id, table_id, reservation_time)
        self.reservations.append(reservation)
        return reservation

    def find_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None


class TestEmployee():

    def setUp(self):
        self.employee = Employee("Lian Pahima", "1234567890", "lianp12@gmail.com", 1, "Manager", 5000)
        self.employee.inventory.add_product(Product("Burger", 10, True))
        self.employee.inventory.add_product(Product("sushi", 15, False))

    def test_create_order(self):
        order = self.employee.create_order(1, ["Burger", "sushi"])
        self.assertIsNotNone(order)
        self.assertEqual(order.table_id, 1)
        self.assertEqual(len(order.products), 2)
        self.assertEqual(order.total_amount, 25)

    def test_create_order_with_invalid_product(self):
        order = self.employee.create_order(1, ["Salad"])
        self.assertIsNone(order)

    def test_update_order(self):
        order = self.employee.create_order(1, ["Burger"])
        self.assertTrue(self.employee.update_order(order.order_id, ["sushi"]))
        self.assertEqual(len(order.products), 1)
        self.assertEqual(order.products[0].name, "sushi")
        self.assertEqual(order.total_amount, 15)

    def test_update_order_with_invalid_product(self):
        order = self.employee.create_order(1, ["Burger"])
        self.assertFalse(self.employee.update_order(order.order_id, ["Salad"]))
        self.assertEqual(len(order.products), 1)
        self.assertEqual(order.products[0].name, "Burger")

    def test_delete_order(self):
        order = self.employee.create_order(1, ["Burger", "sushi"])
        self.assertTrue(self.employee.delete_order(order.order_id))
        self.assertEqual(len(self.employee.orders), 0)

    def test_delete_order_with_invalid_order_id(self):
        order = self.employee.create_order(1, ["Burger", "sushi"])
        self.assertFalse(self.employee.delete_order(999))
        self.assertEqual(len(self.employee.orders), 1)

    def test_view_inventory(self):
        inventory = self.employee.view_inventory()
        self.assertEqual(len(inventory), 2)
        self.assertEqual(inventory[0].name, "Burger")
        self.assertEqual(inventory[1].name, "sushi")

    def test_manage_reservation(self):
        reservation = self.employee.manage_reservation(1, 1, datetime.now())
        self.assertIsNotNone(reservation)
        self.assertEqual(reservation.customer_id, 1)
        self.assertEqual(reservation.table_id, 1)

    def test_find_order(self):
        order = self.employee.create_order(1, ["Burger", "sushi"])
        found_order = self.employee.find_order(order.order_id)
        self.assertIsNotNone(found_order)
        self.assertEqual(found_order.order_id, order.order_id)

    def test_find_order_with_invalid_order_id(self):
        order = self.employee.create_order(1, ["Burger", "sushi"])
        found_order = self.employee.find_order(999)
        self.assertIsNone(found_order)


