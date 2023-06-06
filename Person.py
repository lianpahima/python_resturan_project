
class Person:
  def __init__ (self,name,phone,email,id):
    self.name = name
    self.phone = phone
    self.email = email
    self.id = id

def test_person():
    person = Person("Lian Pahima", "053-3354332", "lianpahima0812@gmail.com", "233939")

    assert person.name == "John Smith"
    assert person.phone == "555-1234"
    assert person.email == "jsmith@example.com"
    assert person.id == "233939"

