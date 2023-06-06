import csv

class ProductData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, products):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name','price','is_vegetrian','id'])
            for product in products:
                writer.writerow([product.name, product.price, product.is_vegetrian, product.id])

    def load(self):
        products = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(Product(row['name'], float(row['price']), bool(row['is_vegetarian']),int(row['id'])))
        return products


class Product:
    def __init__(self, name, price, is_vegetarian, id):
        self.name = name
        self.price = price
        self.is_vegetarian = is_vegetarian
        self.id = id

    def __str__(self):
        return f"{self.name} - ${self.price} - {'Vegetarian' if self.is_vegetarian else 'Non-vegetarian'}"


def test_product():
    product = Product("Sushi", 72, False)

    assert product.name == "Sushi"
    assert product.price == 72
    assert product.is_vegetrian == False
    assert product.id == 1



# import csv

# class ProductData:
#     def __init__(self, filename):
#         self.filename = filename

#     def save(self, products):
#         with open(self.filename, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['name','price','is_vegetarian'])
#             for product in products:
#                 writer.writerow([product.name, product.price, product.is_vegetarian])

#     def load(self):
#         products = []
#         with open(self.filename, 'r', newline='') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 products.append(Product(row['name'], int(row['price']), bool(row['is_vegetarian'])))
#         return products


# class Product:
#     def __init__(self, name, price, is_vegetarian):
#         self.name = name
#         self.price = price
#         self.is_vegetarian = is_vegetarian

#     def __str__(self):
#         return f"{self.name} - ${self.price} - {'Vegetarian' if self.is_vegetarian else 'Non-vegetarian'}"

# def test_product():
#     product = Product("Sushi", 72, False)

#     assert product.name == "Sushi"
#     assert product.price == 72
#     assert product.is_vegetrian == False

