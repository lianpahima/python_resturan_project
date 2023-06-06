

# from datetime import datetime, date
# import csv

# class ReservationData:
#     def __init__(self, filename):
#         self.filename = filename

#     def save(self, reservations):
#         with open(self.filename, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['reservation_id', 'customer_id', 'table_id', 'reservation_time'])
#             for reservation in reservations:
#                 writer.writerow([reservation.reservation_id, reservation.customer_id, reservation.table_id, reservation.reservation_time])

#     def load(self):
#         reservations = []
#         with open(self.filename, 'r', newline='') as file:
#             reader = csv.reader(file)
#             next(reader)  # Skip the header row
#             for row in reader:
#                 reservation_id = int(row[0])
#                 customer_id = int(row[1])
#                 table_id = int(row[2]) if row[2].isdigit() else None
#                 reservation_time = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')  # Update the format here
#                 reservation = Reservation(reservation_id, customer_id, table_id, reservation_time)
#                 reservations.append(reservation)
#         return reservations



# class Reservation:
#     def __init__(self, reservation_id, customer_id, table_id, reservation_time):
#         self.reservation_id = reservation_id
#         self.customer_id = customer_id
#         self.table_id = table_id
#         self.reservation_time = reservation_time
#         self.status = None

#     @classmethod
#     def reserve_table(cls, reservation_id, customer_id, reservation_time):
#         reservation = cls(reservation_id, customer_id, None, reservation_time)
#         reservation.status = 'reserved'
#         return reservation

#     @classmethod
#     def create_reservation(cls, reservation_id, customer_id, table_id, reservation_time):
#         reservation = cls(reservation_id, customer_id, table_id, reservation_time)
#         reservation.status = 'reserved'
#         return reservation

#     def update_reservation(self, reservation_id, table_id, reservation_time):
#         if self.reservation_id == reservation_id:
#             self.table_id = table_id
#             self.reservation_time = reservation_time
#             return True
#         else:
#             return False

#     @classmethod
#     def delete_reservation(cls, reservations, reservation_id):
#         for reservation in reservations:
#             if reservation.reservation_id == reservation_id:
#                 reservations.remove(reservation)
#                 return True
#         return False


# def test_reservation():
#     # create a reservation object
#     reservation = Reservation(1, 1, 1, datetime.datetime(2023, 5, 20, 18, 0))

#     # check that the reservation was created with the correct attributes
#     assert reservation.reservation_id == 1
#     assert reservation.customer_id == 1
#     assert reservation.table_id == 1
#     assert reservation.reservation_time == datetime.datetime(2023, 5, 20, 18, 0)

#     # test the reserve_table method
#     reservation = Reservation.reserve_table(2, 456, datetime.datetime(2023, 5, 20, 18, 0))
#     assert reservation.reservation_id == 2
#     assert reservation.customer_id == 456
#     assert reservation.reservation_time == datetime.datetime(2023, 5, 20, 18, 0)
#     assert reservation.status == 'reserved'


# class ReservationMain:
#     def __init__(self):
#         self.fileName = 'ReservationData.csv'
#         self.reservations = ReservationData(self.fileName).load()

#     def reserve_table(self, reservation_id, customer_id, reservation_time):
#         reservation = Reservation.reserve_table(reservation_id, customer_id, reservation_time)
#         self.reservations.append(reservation)
#         ReservationData(self.fileName).save(self.reservations)

#     def create_reservation(self, reservation_id, customer_id, table_id, reservation_time):
#         reservation = Reservation.create_reservation(reservation_id, customer_id, table_id, reservation_time)
#         self.reservations.append(reservation)
#         ReservationData(self.fileName).save(self.reservations)

#     def update_reservation(self, reservation_id, table_id, reservation_time):
#         for reservation in self.reservations:
#             if reservation.reservation_id == reservation_id:
#                 reservation.table_id = table_id
#                 reservation.reservation_time = reservation_time
#                 ReservationData(self.fileName).save(self.reservations)
#                 return True
#         return False

#     def delete_reservation(self, reservation_id):
#         if Reservation.delete_reservation(self.reservations, reservation_id):
#             ReservationData(self.fileName).save(self.reservations)
#             return True
#         return False

#     def run(self):
#         while True:
#             print("\nMenu Manager Options:")
#             print("1. Reserve Table")
#             print("2. Create Reservation")
#             print("3. Update Reservation")
#             print("4. Delete Reservation")
#             print("5. Exit")

#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 reservation_id = int(input("Enter reservation ID: "))
#                 customer_id = int(input("Enter customer ID: "))
#                 reservation_time = datetime.fromisoformat(input("Enter reservation time ('%Y-%m-%d %H:%M:%S'): "))
#                 self.reserve_table(reservation_id, customer_id, reservation_time)
#                 print("Table reserved successfully.")
#             elif choice == '2':
#                 reservation_id = int(input("Enter reservation ID: "))
#                 customer_id = int(input("Enter customer ID: "))
#                 table_id = int(input("Enter table ID: "))
#                 reservation_time = datetime.fromisoformat(input("Enter reservation time ('%Y-%m-%d %H:%M:%S'): "))
#                 self.create_reservation(reservation_id, customer_id, table_id, reservation_time)
#                 print("Reservation created successfully.")
#             elif choice == '3':
#                 reservation_id = int(input("Enter reservation ID to update: "))
#                 table_id = int(input("Enter new table ID: "))
#                 reservation_time = datetime.fromisoformat(input("Enter new reservation time ('%Y-%m-%d %H:%M:%S'): "))
#                 if self.update_reservation(reservation_id, table_id, reservation_time):
#                     print("Reservation updated successfully.")
#                 else:
#                     print("Reservation not found.")
#             elif choice == '4':
#                 reservation_id = int(input("Enter reservation ID to delete: "))
#                 if self.delete_reservation(reservation_id):
#                     print("Reservation deleted successfully.")
#                 else:
#                     print("Reservation not found.")
#             elif choice == '5':
#                 break
#             else:
#                 print("Invalid choice. Please try again.")

# if __name__ == '__main__':
#     test_reservation()
#     ReservationMain().run()

from datetime import datetime
import csv


class ReservationData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, reservations):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['reservation_id', 'customer_id', 'table_id', 'reservation_time'])
            for reservation in reservations:
                writer.writerow([reservation.reservation_id, reservation.customer_id, reservation.table_id, reservation.reservation_time])

    def load(self):
        reservations = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                try:
                    reservation_id = int(row[0])
                    customer_id = int(row[1])
                    table_id = int(row[2]) if row[2].isdigit() else None
                    reservation_time = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                    reservation = Reservation(reservation_id, customer_id, table_id, reservation_time)
                    reservations.append(reservation)
                except (ValueError, IndexError) as e:
                    print(f"Invalid value encountered: {e}. Skipping the row.")
        return reservations


class Reservation:
    def __init__(self, reservation_id, customer_id, table_id, reservation_time):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.table_id = table_id
        self.reservation_time = reservation_time
        self.status = None

    @classmethod
    def reserve_table(cls, reservation_id, customer_id, reservation_time):
        reservation = cls(reservation_id, customer_id, None, reservation_time)
        reservation.status = 'reserved'
        return reservation


    def update_reservation(self, reservation_id, table_id, reservation_time):
        if self.reservation_id == reservation_id:
            self.table_id = table_id
            self.reservation_time = reservation_time
            return True
        else:
            return False

    @classmethod
    def delete_reservation(cls, reservations, reservation_id):
        for reservation in reservations:
            if reservation.reservation_id == reservation_id:
                reservations.remove(reservation)
                return True
        return False


class ReservationMain:
    def __init__(self):
        self.fileName = 'ReservationData.csv'
        self.reservations = ReservationData(self.fileName).load()

    def reserve_table(self, reservation_id, customer_id, reservation_time):
        reservation = Reservation.reserve_table(reservation_id, customer_id, reservation_time)
        self.reservations.append(reservation)
        ReservationData(self.fileName).save(self.reservations)

    def create_reservation(self, reservation_id, customer_id, table_id, reservation_time):
        reservation = Reservation.create_reservation(reservation_id, customer_id, table_id, reservation_time)
        self.reservations.append(reservation)
        ReservationData(self.fileName).save(self.reservations)

    def update_reservation(self, reservation_id, table_id, reservation_time):
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                reservation.table_id = table_id
                reservation.reservation_time = reservation_time
                ReservationData(self.fileName).save(self.reservations)
                return True
        return False

    def delete_reservation(self, reservation_id):
        if Reservation.delete_reservation(self.reservations, reservation_id):
            ReservationData(self.fileName).save(self.reservations)
            return True
        return False

    def printAll(self):
        try:
            for reservation in self.reservations:
                print(reservation.reservation_id, reservation.customer_id, reservation.table_id, 
                reservation.reservation_time)
        except Exception as e:
            print(f"An error occurred while printing reservations: {e}")

    def run(self):
        while True:
            print("\nMenu Manager Options:")
            print("1. Reserve Table")
            print("2. Update Reservation")
            print("3. Delete Reservation")
            print("4. Show all reservations")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    reservation_id = int(input("Enter reservation ID: "))
                    customer_id = int(input("Enter customer ID: "))
                    reservation_time = datetime.fromisoformat(input("Enter reservation time ('%Y-%m-%d %H:%M:%S'): "))
                    self.reserve_table(reservation_id, customer_id, reservation_time)
                    print("Table reserved successfully.")
                except ValueError:
                    print("Invalid input. Please enter numeric values for reservation ID and customer ID.")
                except ValueError as e:
                    print(f"Invalid reservation time format: {e}. Please enter time in 'YYYY-MM-DD HH:MM:SS' format.")
            elif choice == '2':
                try:
                    reservation_id = int(input("Enter reservation ID to update: "))
                    table_id = int(input("Enter new table ID: "))
                    reservation_time = datetime.fromisoformat(input("Enter new reservation time ('%Y-%m-%d HH:MM:SS'): "))
                    if self.update_reservation(reservation_id, table_id, reservation_time):
                        print("Reservation updated successfully.")
                    else:
                        print("Reservation not found.")
                except ValueError:
                    print("Invalid input. Please enter numeric values for reservation ID and table ID.")
                except ValueError as e:
                    print(f"Invalid reservation time format: {e}. Please enter time in 'YYYY-MM-DD HH:MM:SS' format.")
            elif choice == '3':
                try:
                    reservation_id = int(input("Enter reservation ID to delete: "))
                    if self.delete_reservation(reservation_id):
                        print("Reservation deleted successfully.")
                    else:
                        print("Reservation not found.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value for reservation ID.")
            elif choice == '4':
                self.printAll()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

# ReservationMain().run()
