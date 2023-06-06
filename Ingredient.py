import csv

class IngredientData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, ingredients):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'unit'])
            for ingredient in ingredients:
                writer.writerow([ingredient.name, ingredient.unit])

    def load(self):
        ingredients = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ingredients.append(Ingredient(row['name'], row['unit']))
        return ingredients


class Ingredient:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit
        
    def set_name(self, new_name):
        self.name = new_name
        
    def set_unit(self, new_unit):
        self.unit = new_unit
        
    def __str__(self):
        return f"1 {self.unit} {self.name}"
        
    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.name == other.name and self.unit == other.unit
        return False


class TestIngredient():
    def setUp(self):
        self.ingredient = Ingredient('Sugar', 'cup')
        
    def test_set_name(self):
        self.ingredient.set_name('Salt')
        self.assertEqual(self.ingredient.name, 'Salt')
        
    def test_set_unit(self):
        self.ingredient.set_unit('teaspoon')
        self.assertEqual(self.ingredient.unit, 'teaspoon')
        
    def test_str(self):
        self.assertEqual(str(self.ingredient), '1 cup Sugar')
        
    def test_eq(self):
        other_ingredient = Ingredient('Sugar', 'cup')
        self.assertEqual(self.ingredient, other_ingredient)
        
        different_ingredient = Ingredient('Salt', 'teaspoon')
        self.assertNotEqual(self.ingredient, different_ingredient)
        
