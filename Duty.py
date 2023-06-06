
# import csv
# from datetime import datetime

# class DutyData:
#     def __init__(self, filename):
#         self.filename = filename

#     def save(self, dutys):
#         with open(self.filename, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['employee_id', 'date', 'start_time', 'end_time'])
#             for duty in dutys:
#                 writer.writerow([duty.employee_id, duty.date.strftime('%Y-%m-%d'), duty.start_time, duty.end_time])

#     def load(self):
#         dutys = []
#         with open(self.filename, 'r', newline='') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 duty_date = datetime.strptime(row['date'], '%Y-%m-%d')
#                 duty_start_time = datetime.strptime(row['start_time'], '%H:%M:%S')
#                 duty_end_time = datetime.strptime(row['end_time'], '%H:%M:%S')
#                 dutys.append(Duty(int(row['employee_id']), duty_date, duty_start_time, duty_end_time))
#         return dutys


# class Duty:
#     def __init__(self, employee_id, date, start_time, end_time):
#         self.employee_id = employee_id
#         self.date = date
#         self.start_time = start_time
#         self.end_time = end_time

# class TestDuty():
    
#     def test_duration(self):
#         duty = Duty(1, '2023-05-09', '08:00', '10:30')
#         duration = duty.duration()
#         self.assertEqual(duration, 150)
    
#     def test_overlap(self):
#         duty1 = Duty(1, '2023-05-09', '08:00', '10:30')
#         duty2 = Duty(2, '2023-05-09', '09:30', '12:00')
#         duty3 = Duty(3, '2023-05-10', '08:00', '10:30')
#         self.assertTrue(duty1.overlap(duty2))
#         self.assertTrue(duty2.overlap(duty1))
#         self.assertFalse(duty1.overlap(duty3))
#         self.assertFalse(duty3.overlap(duty1))
#         self.assertFalse(duty2.overlap(duty3))
#         self.assertFalse(duty3.overlap(duty2))
    
#     def test_conflict(self):
#         duty1 = Duty(1, '2023-05-09', '08:00', '10:30')
#         duty2 = Duty(2, '2023-05-09', '09:30', '12:00')
#         duty3 = Duty(3, '2023-05-10', '08:00', '10:30')
#         duty4 = Duty(4, '2023-05-09', '11:00', '13:00')
#         duty5 = Duty(5, '2023-05-10', '09:00', '10:00')
#         duties = [duty2, duty3, duty4, duty5]
#         conflicts = duty1.conflict(duties)
#         self.assertEqual(conflicts, [duty2, duty4])


# class DutyMenu():
#     def __init__(self):
#         self.fileName = 'DutyData.csv'
#         self.dutites = DutyData(self.fileName).load()

#     def duration(self):
#         for duty in self.dutites:
#             print(duty.employee_id, duty.end_time - duty.start_time)

#     def printAll(self):
#         for duty in self.dutites:
#             print(duty.employee_id, duty.date, duty.start_time, duty.end_time)

#     def deleteById(self):
#         id = input("Enter id to delete: ")

#         dutyToRemove = {}

#         for (duty) in self.dutites:
#             if duty.employee_id == int(id):
#                 dutyToRemove = duty
#                 break
        
#         self.dutites.remove(dutyToRemove)

#         with open(self.fileName, 'r') as file:
#             rows = list(csv.reader(file))
    
#         for index, row in enumerate(rows):
#             if index > 0 and int(row[0]) == int(id):
#                 del rows[index]  
    
#         with open(self.fileName, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(rows)

    
#     # def AddById(self):
#     #     id = input("Enter id to delete: ")

#     #     dutyToAdd = {}

#     #     for duty in self.dutites:
#     #         if duty.employee_id == int(id):
#     #             dutyToAdd = duty
#     #             break
    
#     #     self.dutites.append(dutyToAdd)

#     #     with open(self.fileName, 'r') as file:
#     #         rows = list(csv.reader(file))

#     #     for index, row in enumerate(rows):
#     #         if index > 0 and int(row[0]) == int(id):
#     #             del rows[index]  
    
#     #     with open(self.fileName, 'w', newline='') as file:
#     #         writer = csv.writer(file)
#     #         writer.writerows(rows)

 
#     def run(self):
#         while True:
#             print("\nMenu Manager Options:")
#             print("1 - Show durations")
#             print("2 - delete")
#             print("3 - show all")
#             print("back - go back")

#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 print('Here are all the duties durations:')
#                 self.duration()
#             elif choice == '2':
#                 self.deleteById()
#             elif choice == '3':
#                 self.printAll()
#             elif choice == 'back':
#                 break
        
#             else:
#                 print("Invalid choice. Please try again.")

import csv
from datetime import datetime

class DutyData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, duties):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['employee_id', 'date', 'start_time', 'end_time'])
                for duty in duties:
                    writer.writerow([duty.employee_id, duty.date.strftime('%Y-%m-%d'), duty.start_time, duty.end_time])
        except IOError as e:
            print(f"Error while saving duties: {e}")

    def load(self):
        duties = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        duty_date = datetime.strptime(row['date'], '%Y-%m-%d')
                        duty_start_time = datetime.strptime(row['start_time'], '%H:%M:%S')
                        duty_end_time = datetime.strptime(row['end_time'], '%H:%M:%S')
                        duties.append(Duty(int(row['employee_id']), duty_date, duty_start_time, duty_end_time))
                    except ValueError as e:
                        print(f"Error while parsing duty data: {e}")
        except IOError as e:
            print(f"Error while loading duties: {e}")
        return duties


class Duty:
    def __init__(self, employee_id, date, start_time, end_time):
        self.employee_id = employee_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time


class DutyMenu:
    def __init__(self):
        self.fileName = 'DutyData.csv'
        self.duties = DutyData(self.fileName).load()

    def duration(self):
        try:
            for duty in self.duties:
                print(duty.employee_id, duty.end_time - duty.start_time)
        except Exception as e:
            print(f"An error occurred while calculating duty durations: {e}")

    def printAll(self):
        try:
            for duty in self.duties:
                print(duty.employee_id, duty.date, duty.start_time, duty.end_time)
        except Exception as e:
            print(f"An error occurred while printing duties: {e}")

    def deleteById(self):
        try:
            id = input("Enter id to delete: ")
            dutyToRemove = None

            for duty in self.duties:
                if duty.employee_id == int(id):
                    dutyToRemove = duty
                    break

            if dutyToRemove:
                self.duties.remove(dutyToRemove)

                with open(self.fileName, 'r') as file:
                    rows = list(csv.reader(file))

                for index, row in enumerate(rows):
                    if index > 0 and int(row[0]) == int(id):
                        del rows[index]

                with open(self.fileName, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
            else:
                print("No duty found with the given id.")
        except Exception as e:
            print(f"An error occurred while deleting duty: {e}")

    def run(self):
        while True:
            print("\nMenu Manager Options:")
            print("1 - Show durations")
            print("2 - Delete")
            print("3 - Show all")
            print("4 - Go back")

            choice = input("Enter your choice: ")

            if choice == '1':
                print('Here are all the duties durations:')
                self.duration()
            elif choice == '2':
                self.deleteById()
            elif choice == '3':
                self.printAll()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")


# menu = DutyMenu()
# menu.run()
