# import csv
# from Duty import DutyData, DutyMenu
# from Menu import MenuData,MainMenu
# from Product import Product,ProductData
# from InventoryManagement import InventoryManagementMain,InventoryManagementData
# from Order import Ordermain,OrderData
# from Reservation import ReservationMain,ReservationData
# from IncomeReport import IncomeReportData,IncomeReportMain

# class Restaurant:
#     def __init__(self, name):
#         self.name = name
#         print('Welcome to', self.name, '!')

#     def open(self):
#         products = self.load_products_from_csv('ProductData.csv')
#         while True:
#             print("\nMenu Manager Options:")
#             print("1.Menu")
#             print("2.Duty")
#             print("3.InventoryManagement")
#             print("4.Order")
#             print("5.Reservation")
#             print("6.IncomeReport")
        
#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 print ('This is our menu with appetite!')
#                 MainMenu(products).run()
#             elif choice == '2':
#                 DutyMenu().run()    
#             elif choice == '3':
#                 InventoryManagementMain().run()
#             elif choice == '4':
#                 Ordermain().run()
#             elif choice == '5':
#                 ReservationMain().run()
#             elif choice == '6':
#                 IncomeReportMain().run()
#             elif choice == '7':    
#                 break
#             else:
#                 print("Invalid choice. Please try again.")


#     def load_products_from_csv(self, filename):
#         products = []
#         with open(filename, 'r', newline='') as file:
#             reader = csv.reader(file)
#             header = next(reader)  # Skip the header row
#             for row in reader:
#                 product = (row[0], float(row[1]))  # Assuming the name is in the first column and price in the second column
#                 products.append(product)
#         return products

import csv
from Duty import DutyData, DutyMenu
from Menu import MenuData,MainMenu
from Product import Product,ProductData
from InventoryManagement import InventoryManagementMain,InventoryManagementData
from Order import Ordermain,OrderData
from Reservation import ReservationMain,ReservationData
from IncomeReport import IncomeReportData,IncomeReportMain

class RestaurantFacade:
    def __init__(self, name):
        self.name = name
        self.products = self.load_products_from_csv('ProductData.csv')
        self.duty_menu = DutyMenu()

    def load_products_from_csv(self, filename):
        products = []
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)  # Skip the header row
                for row in reader:
                    product = (row[0], float(row[1]))  # Assuming the name is in the first column and price in the second column
                    products.append(product)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except csv.Error as e:
            print(f"Error while reading CSV file: {e}")
        return products

    def open_menu(self):
        print('This is our menu with appetite!')
        MainMenu().run()

    def open_duty_menu(self):
        self.duty_menu.run()

    def open_inventory_management(self):
        InventoryManagementMain().run()

    def open_order(self):
        Ordermain().run()

    def open_reservation(self):
        ReservationMain().run()

    def open_income_report(self):
        IncomeReportMain().run()

    def open(self):
        print('Welcome to', self.name, '!')
        while True:
            print("\nMenu Manager Options:")
            print("1. Menu")
            print("2. Duty")
            print("3. Inventory Management")
            print("4. Order")
            print("5. Reservation")
            print("6. Income Report")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.open_menu()
            elif choice == '2':
                self.open_duty_menu()
            elif choice == '3':
                self.open_inventory_management()
            elif choice == '4':
                self.open_order()
            elif choice == '5':
                self.open_reservation()
            elif choice == '6':
                self.open_income_report()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")



restaurant = RestaurantFacade("My Restaurant")
restaurant.open()