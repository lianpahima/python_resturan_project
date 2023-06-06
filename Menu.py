# import csv

# class Product:
#     def __init__(self, name, price, id):
#         self.name = name
#         self.price = price
#         self.id = id

# class MenuData:
#     def __init__(self, filename):
#         self.filename = filename

#     def save(self, menus):
#         with open(self.filename, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['name', 'price', 'id'])
#             for menu in menus:
#                 writer.writerow([menu.name, menu.price, menu.id])

#     def load(self):
#         products = []
#         with open(self.filename, 'r', newline='') as file:
#             reader = csv.reader(file)
#             next(reader)
#             for row in reader:
#                 try:
#                     product = Product(row[0], float(row[1]), int(row[2]))
#                     products.append(product)
#                 except IndexError:
#                     print("Error: Invalid row format in the CSV file.")
#         return products

# class Menu:
#     def __init__(self, products):
#         self.products = products

#     def view_menu(self):
#         for product in self.products:
#             print(product.name, product.price, product.id)

# class MainMenu:
#     def __init__(self,products):
#         self.fileName = 'MenuData.csv'
#         self.menu_data = MenuData(self.fileName)
#         self.products = self.menu_data.load()

#     def view_menu(self):
#         for product in self.products:
#             print(product.name, product.price, product.id)

#     def deleteById(self):
#         id = input("Enter id to delete: ")

#         productToRemove = None

#         for product in self.products:
#             if product.id == int(id):
#                 productToRemove = product
#                 break

#         if productToRemove is not None:
#             self.products.remove(productToRemove)
#             print(f"Product with ID {id} has been deleted.")
#         else:
#             print(f"Error: Product with ID {id} not found.")

#         self.menu_data.save(self.products)

#     def AddById(self):
#         id = input("Enter id to add: ")

#         productToAdd = None

#         for product in self.products:
#             if product.id == int(id):
#                 productToAdd = product
#                 break

#         if productToAdd is not None:
#             self.products.append(productToAdd)
#             print(f"Product {productToAdd.id} has been added to the menu.")
#         else:
#             print(f"Error: Product with id {id} does not exist.")

#         self.menu_data.save(self.products)

#     def run(self):
#         while True:
#             print("\nMenu Manager Options:")
#             print("1. View Menu")
#             print("2. Add Product to Menu")
#             print("3. Delete Product from Menu")
#             print("4. Exit")

#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 self.view_menu()
#             elif choice == '2':
#                 self.AddById()
#             elif choice == '3':
#                 self.deleteById()
#             elif choice == '4':
#                 print("Exiting Menu Manager...")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")

# def main():
#     menu = MainMenu()
#     menu.run()

# if __name__ == "__main__":
#     main()

import csv

class Product:
    def __init__(self, name, price, id):
        self.name = name
        self.price = price
        self.id = id

class MenuData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, menus):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['name', 'price', 'id'])
                for menu in menus:
                    writer.writerow([menu.name, menu.price, menu.id])
        except IOError as e:
            print(f"Error while saving menus: {e}")

    def load(self):
        products = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    try:
                        product = Product(row[0], float(row[1]), int(row[2]))
                        products.append(product)
                    except (IndexError, ValueError) as e:
                        print(f"Error while parsing menu data: {e}")
        except IOError as e:
            print(f"Error while loading menus: {e}")
        return products

class Menu:
    def __init__(self, products):
        self.products = products

    def view_menu(self):
        for product in self.products:
            print(product.name, product.price, product.id)

class MainMenu:
    def __init__(self):
        self.fileName = 'MenuData.csv'
        self.menu_data = MenuData(self.fileName)
        self.products = self.menu_data.load()

    def view_menu(self):
        try:
            for product in self.products:
                print(product.name, product.price, product.id)
        except Exception as e:
            print(f"An error occurred while viewing the menu: {e}")

    def deleteById(self):
        try:
            id = input("Enter id to delete: ")
            productToRemove = None

            for product in self.products:
                if product.id == int(id):
                    productToRemove = product
                    break

            if productToRemove is not None:
                self.products.remove(productToRemove)
                print(f"Product with ID {id} has been deleted.")
            else:
                print(f"Error: Product with ID {id} not found.")

            self.menu_data.save(self.products)
        except Exception as e:
            print(f"An error occurred while deleting a product from the menu: {e}")

    def AddById(self):
        try:
            id = input("Enter id to add: ")
            productToAdd = None

            for product in self.products:
                if product.id == int(id):
                    productToAdd = product
                    break

            if productToAdd is not None:
                self.products.append(productToAdd)
                print(f"Product {productToAdd.id} has been added to the menu.")
            else:
                print(f"Error: Product with id {id} does not exist.")

            self.menu_data.save(self.products)
        except Exception as e:
            print(f"An error occurred while adding a product to the menu: {e}")

    def run(self):
        while True:
            print("\nMenu Manager Options:")
            print("1. View Menu")
            print("2. Add Product to Menu")
            print("3. Delete Product from Menu")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_menu()
            elif choice == '2':
                self.AddById()
            elif choice == '3':
                self.deleteById()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")


