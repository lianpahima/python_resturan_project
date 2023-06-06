# from Product import Product
# import csv

# class InventoryManagementData:
#     def __init__(self, filename):
#         self.filename = filename

#     def save(self, inventoryManagements):
#         with open(self.filename, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['product_id', 'product_name', 'quantity'])
#             for inventoryManagement in inventoryManagements:
#                 writer.writerow([inventoryManagement.product_id, inventoryManagement.product_name, inventoryManagement.quantity])

#     def load(self):
#         inventoryManagements = []
#         with open(self.filename, 'r', newline='') as file:
#          reader = csv.DictReader(file)
#          for row in reader:
#             print(row)  # Print the row to check the data
#             inventoryManagements.append(InventoryManagement(int(row['product_id']), row['product_name'], int(row['quantity'])))
#         return inventoryManagements


# class InventoryManagement:
#     def __init__(self, product_id, product_name, quantity):
#         self.product_id = product_id
#         self.product_name = product_name
#         self.quantity = quantity

      
# class TestInventoryManagement:
#     def test_is_available(self):
#         product1 = Product(1, 'Tomato', 10)
#         product2 = Product(2, 'Milk', 0)
#         inventory = InventoryManagement([product1, product2])

#         assert inventory.is_available(1) == True
#         assert inventory.is_available(2) == False
#         assert inventory.is_available(3) == False

#     def test_decrement(self):
#         product1 = Product(1, 'Tomato', 10)
#         product2 = Product(2, 'Milk', 0)
#         inventory = InventoryManagement([product1, product2])

#         inventory.decrement(1)
#         assert product1.quantity == 9

#         try:
#             inventory.decrement(2)
#         except ValueError as e:
#             assert str(e) == "Product not found or quantity is already 0"
#         else:
#             assert False, "Expected ValueError but no exception was raised"

#         try:
#             inventory.decrement(3)
#         except ValueError as e:
#             assert str(e) == "Product not found or quantity is already 0"
#         else:
#             assert False, "Expected ValueError but no exception was raised"

# class InventoryManagementMain:
#     def __init__(self):
#         self.fileName = 'InventoryManagementData.csv'
#         self.InventoryManagements = InventoryManagementData(self.fileName).load()

#     def is_available(self, product_id):
#         for product in self.InventoryManagements:
#             if product.product_id == product_id and product.quantity > 0:
#                 return True
#         return False

#     def decrement(self, product_id):
#         for product in self.InventoryManagements:
#             if product.product_id == product_id and product.quantity > 0:
#                 product.quantity -= 1
#                 return
#         raise ValueError("Product not found or quantity is already 0")

#     def printAll(self):
#         for inventoryManagement in self.InventoryManagements:
#             print(
#                 inventoryManagement.product_id,
#                 inventoryManagement.product_name,
#                 inventoryManagement.quantity,
#             )

#     def deleteById(self):
#         id = input("Enter id to delete: ")

#         inventoryManagementToRemove = {}

#         for inventoryManagement in self.InventoryManagements:
#             if inventoryManagement.product_id == int(id):
#                 inventoryManagementToRemove = inventoryManagement
#                 break

#         self.InventoryManagements.remove(inventoryManagementToRemove)

#         with open(self.fileName, "r") as file:
#             rows = list(csv.reader(file))

#         for index, row in enumerate(rows):
#             if index > 0 and int(row[0]) == int(id):
#                 del rows[index]

#         with open(self.fileName, "w", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerows(rows)

#     def run(self):
#         while True:
#             print("\nMenu Manager Options:")
#             print("1. is_available")
#             print("2. decrement")
#             print("3. printAll")
#             print("4. delete")

#             choice = input("Enter your choice: ")

#             if choice == "1":
#                 product_id = int(input("Enter product ID: "))
#                 print(self.is_available(product_id))
#             elif choice == "2":
#                 product_id = int(input("Enter product ID: "))
#                 self.decrement(product_id)
#                 print("Quantity decremented successfully.")
#             elif choice == "3":
#                 self.printAll()
#             elif choice == "4":
#                 self.deleteById()
#                 print("Product deleted successfully.")
#             elif choice == 'back':
#                 break  
#             else:
#                 print("Invalid choice. Please try again.")


from Product import Product
import csv

class InventoryManagementData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, inventoryManagements):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['product_id', 'product_name', 'quantity'])
                for inventoryManagement in inventoryManagements:
                    writer.writerow([inventoryManagement.product_id, inventoryManagement.product_name, inventoryManagement.quantity])
        except IOError as e:
            print(f"Error while saving inventory management data: {e}")

    def load(self):
        inventoryManagements = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        inventoryManagement = InventoryManagement(int(row['product_id']), row['product_name'], int(row['quantity']))
                        inventoryManagements.append(inventoryManagement)
                    except (ValueError, KeyError) as e:
                        print(f"Error while parsing inventory management data: {e}")
        except IOError as e:
            print(f"Error while loading inventory management data: {e}")
        return inventoryManagements


class InventoryManagement:
    def __init__(self, product_id, product_name, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity

      
class TestInventoryManagement:
    def test_is_available(self):
        product1 = Product(1, 'Tomato', 10)
        product2 = Product(2, 'Milk', 0)
        inventory = InventoryManagement([product1, product2])

        assert inventory.is_available(1) == True
        assert inventory.is_available(2) == False
        assert inventory.is_available(3) == False

    def test_decrement(self):
        product1 = Product(1, 'Tomato', 10)
        product2 = Product(2, 'Milk', 0)
        inventory = InventoryManagement([product1, product2])

        inventory.decrement(1)
        assert product1.quantity == 9

        try:
            inventory.decrement(2)
        except ValueError as e:
            assert str(e) == "Product not found or quantity is already 0"
        else:
            assert False, "Expected ValueError but no exception was raised"

        try:
            inventory.decrement(3)
        except ValueError as e:
            assert str(e) == "Product not found or quantity is already 0"
        else:
            assert False, "Expected ValueError but no exception was raised"

class InventoryManagementMain:
    def __init__(self):
        self.fileName = 'InventoryManagementData.csv'
        self.InventoryManagements = InventoryManagementData(self.fileName).load()

    def is_available(self, product_id):
        for product in self.InventoryManagements:
            if product.product_id == product_id and product.quantity > 0:
                return True
        return False

    def decrement(self, product_id):
        for product in self.InventoryManagements:
            if product.product_id == product_id and product.quantity > 0:
                product.quantity -= 1
                return
        raise ValueError("Product not found or quantity is already 0")

    def printAll(self):
        for inventoryManagement in self.InventoryManagements:
            print(
                inventoryManagement.product_id,
                inventoryManagement.product_name,
                inventoryManagement.quantity,
            )

    def deleteById(self):
        try:
            id = int(input("Enter id to delete: "))

            inventoryManagementToRemove = None

            for inventoryManagement in self.InventoryManagements:
                if inventoryManagement.product_id == id:
                    inventoryManagementToRemove = inventoryManagement
                    break

            if inventoryManagementToRemove:
                self.InventoryManagements.remove(inventoryManagementToRemove)

                with open(self.fileName, "r") as file:
                    rows = list(csv.reader(file))

                for index, row in enumerate(rows):
                    if index > 0 and int(row[0]) == id:
                        del rows[index]

                with open(self.fileName, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
            else:
                print("Product not found.")
        except ValueError:
            print("Invalid input. Please enter a valid integer ID.")

    def run(self):
        while True:
            print("\nMenu Manager Options:")
            print("1. is_available")
            print("2. decrement")
            print("3. printAll")
            print("4. delete")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    product_id = int(input("Enter product ID: "))
                    print(self.is_available(product_id))
                except ValueError:
                    print("Invalid input. Please enter a valid integer ID.")
            elif choice == "2":
                try:
                    product_id = int(input("Enter product ID: "))
                    self.decrement(product_id)
                    print("Quantity decremented successfully.")
                except ValueError as e:
                    print(e)
            elif choice == "3":
                self.printAll()
            elif choice == "4":
                self.deleteById()
                print("Product deleted successfully.")
            elif choice == '5':
                break  
            else:
                print("Invalid choice. Please try again.")
