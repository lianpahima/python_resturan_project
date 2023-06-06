
import csv

class TableData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, tables):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['table_id','capacity','status'])
            for table in tables:
                writer.writerow([table.table_id, table.capacity, table.status])

    def load(self):
        tables = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tables.append(Table(int(row['table_id']), int(row['capacity']), bool(row['status'])))
        return tables

class Table:
  def __init__(self,table_id,capacity,status):
    self.table_id=table_id
    self.capacity=capacity
    self.status=status


def test_table():
    table = Table(1, 5, "available")
    
    assert table.table_id == 1
    assert table.capacity == 5
    assert table.status == "available"

