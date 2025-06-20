class WaterBottle:
    def __init__ (self, volume, color, material):
        self.volume = volume
        self.color = color
        self.material = material

    def describe(self):
        return f"This is a Water Bottle with volume = {self.volume}, of {self.color} color, made out of {self.material}"

class InsulatedWaterBottle(WaterBottle):
    def __init__ (self, volume, color, material, insulation_type):
        super().__init__(volume, color, material)
        self.insulation_type = insulation_type

    def describe(self):
        return f"This is an Insulated Water Bottle with volume = {self.volume}, of {self.color} color, made out of {self.material}, with {self.insulation_type} insulation"
    
class SmartWaterBottle(WaterBottle):
    def __init__ (self, volume, color, material, temperature):
        super().__init__(volume, color, material)
        self.temperature = temperature

def describe(self):
        return f"This is a Smart Water Bottle with volume = {self.volume}, of {self.color} color, made out of {self.material}, with {self.temperature}"

regular_bottle = WaterBottle(500, 'green', "plastic")
insulated_bottle = InsulatedWaterBottle(200, 'blue', 'metal', "vacuum")
smart_bottle = SmartWaterBottle(750, "red", "wood", 36) 

bottles = [regular_bottle, insulated_bottle, smart_bottle]

for bottle in bottles:
    print(bottle.describe())