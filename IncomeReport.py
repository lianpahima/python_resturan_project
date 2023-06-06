# import unittest
# import io
# from contextlib import redirect_stdout
# import ast
# import csv


# class IncomeReportData:
#     def __init__(self, filename):
#         self.filename = filename

#     def save(self, income_reports):
#         with open(self.filename, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['restaurant_name', 'year', 'month', 'total_income', 'expenses'])
#             for report in income_reports:
#                 writer.writerow([report.restaurant_name, report.year, report.month, report.total_income, report.expenses])



#     def load(self):
#         income_reports = []
#         with open(self.filename, 'r', newline='') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 restaurant_name = row['restaurant_name']
#                 year = int(row['year'])
#                 month = row['month'].strip("'")  # Remove the single quotes around the month value
#                 total_income = float(row['total_income'])
#                 expenses = ast.literal_eval(row['expenses'])
#                 income_report = IncomeReport(restaurant_name, year, month, total_income, expenses)
#                 income_reports.append(income_report)
#         return income_reports




# class IncomeReport:
#     def __init__(self, restaurant_name, year, month, total_income, expenses=None):
#         self.restaurant_name = restaurant_name
#         self.year = year
#         self.month = month
#         self.total_income = total_income
#         if expenses is None:
#             self.expenses = {}
#         else:
#             self.expenses = expenses


#     def generate_report(self):
#         net_income = self.total_income - self.expenses if isinstance(self.expenses, int) else 0
#         print("Income Report")
#         print("Restaurant Name:", self.restaurant_name)
#         print("Year:", self.year)
#         print("Month:", self.month)
#         print("Total Income:", self.total_income)
#         if isinstance(self.expenses, int):
#             print("Expenses:")
#             print("Total Expenses:", self.expenses)
#         else:
#             print("No expense data available.")
#         print("Net Income:", net_income)


# class TestIncomeReport(unittest.TestCase):
#     def test_generate_report(self):
#         expenses = {'Rent': 1000, 'Salaries': 5000, 'Supplies': 500}
#         income_report = IncomeReport('My Restaurant', 2022, 'May', 10000, expenses)
#         expected_output = "Income Report for My Restaurant - May/2022\n==================================================\nTotal Income: $10000\nTotal Expenses: $6500\nNet Income: $3500\n\nExpenses Breakdown:\n--------------------------------------------------\nRent: $1000\nSalaries: $5000\nSupplies: $500\n\n"
#         with io.StringIO() as buffer, redirect_stdout(buffer):
#             income_report.generate_report()
#             output = buffer.getvalue()
#             self.assertEqual(output, expected_output)



# class IncomeReportMain:
#     def __init__(self):
#         self.fileName = 'IncomeReport.csv'
#         self.IncomeReports = IncomeReportData(self.fileName).load()

#     def run(self):
#         while True:
#             print("\nMenu Manager Options:")
#             print("1. Print Report")
#             print("2. Exit")

#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 self.IncomeReports[0].generate_report()
#             elif choice == '2':
#                 break
#             else:
#                 print("Invalid choice. Please try again.")

# # def main():
# #     Restaurant("Lian's place").open()


# # if __name__ == "__main__":
# #     main()


import unittest
import io
from contextlib import redirect_stdout
import ast
import csv


class IncomeReportData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, income_reports):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['restaurant_name', 'year', 'month', 'total_income', 'expenses'])
                for report in income_reports:
                    writer.writerow([report.restaurant_name, report.year, report.month, report.total_income, report.expenses])
        except IOError as e:
            print(f"Error while saving income reports: {e}")

    def load(self):
        income_reports = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        restaurant_name = row['restaurant_name']
                        year = int(row['year'])
                        month = row['month'].strip("'")  # Remove the single quotes around the month value
                        total_income = float(row['total_income'])
                        expenses = ast.literal_eval(row['expenses'])
                        income_report = IncomeReport(restaurant_name, year, month, total_income, expenses)
                        income_reports.append(income_report)
                    except (ValueError, SyntaxError, TypeError) as e:
                        print(f"Error while parsing income report data: {e}")
        except IOError as e:
            print(f"Error while loading income reports: {e}")
        return income_reports

class IncomeReport:
    def __init__(self, restaurant_name, year, month, total_income, expenses=None):
        self.restaurant_name = restaurant_name
        self.year = year
        self.month = month
        self.total_income = total_income
        if expenses is None:
            self.expenses = {}
        else:
            self.expenses = expenses

    def generate_report(self):
        try:
            if isinstance(self.expenses, int):
                net_income = self.total_income - self.expenses
                print("Income Report")
                print("Restaurant Name:", self.restaurant_name)
                print("Year:", self.year)
                print("Month:", self.month)
                print("Total Income:", self.total_income)
                print("Expenses:")
                print("Total Expenses:", self.expenses)
            else:
                net_income = self.total_income - sum(self.expenses.values())
                print("Income Report")
                print("Restaurant Name:", self.restaurant_name)
                print("Year:", self.year)
                print("Month:", self.month)
                print("Total Income:", self.total_income)
                if self.expenses:
                    print("Expenses:")
                    print("Total Expenses:", sum(self.expenses.values()))
                    print("Expenses Breakdown:")
                    for expense, amount in self.expenses.items():
                        print(f"{expense}: ${amount}")
                else:
                    print("No expense data available.")
            print("Net Income:", net_income)
        except Exception as e:
            print(f"An error occurred while generating the income report: {e}")

class TestIncomeReport(unittest.TestCase):
    def test_generate_report(self):
        expenses = {'Rent': 1000, 'Salaries': 5000, 'Supplies': 500}
        income_report = IncomeReport('My Restaurant', 2022, 'May', 10000, expenses)
        expected_output = "Income Report\nRestaurant Name: My Restaurant\nYear: 2022\nMonth: May\nTotal Income: 10000\nExpenses:\nTotal Expenses: 6500\nExpenses Breakdown:\nRent: $1000\nSalaries: $5000\nSupplies: $500\nNet Income: 3500\n"
        with io.StringIO() as buffer, redirect_stdout(buffer):
            income_report.generate_report()
            output = buffer.getvalue()
            self.assertEqual(output, expected_output)


class IncomeReportMain:
    def __init__(self):
        self.fileName = 'IncomeReport.csv'
        self.IncomeReports = IncomeReportData(self.fileName).load()

    def run(self):
        while True:
            print("\nMenu Manager Options:")
            print("1. Print Report")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    self.IncomeReports[0].generate_report()
                except IndexError:
                    print("No income reports found.")
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please try again.")


# def main():
#     menu = IncomeReportMain()
#     menu.run()


# if __name__ == "__main__":
#     main()

