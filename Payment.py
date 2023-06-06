
import csv
from io import StringIO
import sys

class PaymentData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, payments):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['transactions'])
            for payment in payments:
                writer.writerow([payment])

    def load(self):
        payments = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                payments.append(int(row['transactions']))
        return payments
    


class Payment:
   def __init__(self,transactions):
    self.transactions=transactions

   def make_payment(self, payment_amount):
        self.transactions.append(payment_amount)

   def view_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

   def refund(self, refund_amount):
        self.transactions.append(-refund_amount)


def test_payment():
    
    payment = Payment([])

   
    payment.make_payment(200)
    payment.make_payment(154)
    assert payment.transactions == [200, 154]
    payment.refund(6)
    assert payment.transactions == [10, 20, -5]
    captured_output = StringIO()
    sys.stdout = captured_output
    payment.view_transaction_history()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "10\n20\n-5"

    # Test that a negative payment raises a ValueError
    try:
        payment.make_payment(-10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"
