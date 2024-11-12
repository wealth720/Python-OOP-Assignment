# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.__battery_capacity = battery_capacity  # Encapsulated attribute
        self.is_on = False
    
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")
    
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")
    
    def check_battery(self):
        print(f"{self.brand} {self.model} has {self.__battery_capacity}mAh battery capacity.")

# Subclass: GamingSmartphone (inherits from Smartphone)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_capacity, cooling_system):
        super().__init__(brand, model, battery_capacity)
        self.cooling_system = cooling_system
    
    # Overriding the check_battery method to include cooling system info
    def check_battery(self):
        super().check_battery()
        print(f"Cooling System: {self.cooling_system}")

# Creating objects of both classes
basic_phone = Smartphone("Apple", "iPhone 14", 3279)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 6000, "Advanced Cooling")

# Using the methods
basic_phone.turn_on()
basic_phone.check_battery()
basic_phone.turn_off()

print("\n")

gaming_phone.turn_on()
gaming_phone.check_battery()
gaming_phone.turn_off()
