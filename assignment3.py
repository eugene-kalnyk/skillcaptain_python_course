# Define Vehicle class
class Vehicle:
    def __init__ (self, brand, model, color, value):
        self.brand = brand
        self.model = model
        self.color = color
        self.value = value

    def display_info(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.brand, self.color, self.model, self.value)
        return desc_str
    
# Create `car`` object and test
car = Vehicle("Ferrari", "sports car", "red", 100000)
print(car.display_info())

# Define Truck class
class Truck(Vehicle):
    def __init__ (self, brand, model, color, value, load_capacity):
        super().__init__(brand, model, color, value)
        self.load_capacity = load_capacity

    def display_info(self):
        desc_str = "%s is a %s %s worth $%.2f. with a load capacity of %s tons" % (self.brand, self.color, self.model, self.value, self.load_capacity)
        return desc_str

# Create `truck` object and test
ford = Truck("Ford", "pickup truck", "white", 10000, 8)
print(ford.display_info())