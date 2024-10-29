class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.available = True
    
    def mark_available(self):
        self.available = True
    
    def mark_quarantine(self):
        self.available = False
    
    def info(self):
        info = f"Name: {self.name},Age: {self.age},Habitat: {self.habitat},Available: {self.available}"
        return info
    
class Mammals(Animal):
    def __init__(self, name, age, habitat,fur_length, diet_type):
        super().__init__(name, age, habitat)
        self.fur_length = fur_length
        self.diet_type = diet_type

    def info(self):
        Basic_info = super.info()
        info = f"{Basic_info},Fur Length: {self.fur_length},Diet Type: {self.diet_type}."
        return info
    
class Birds(Animal):
    def __init__(self, name, age, habitat, wingspan, flight):
        super().__init__(name, age, habitat)
        self.wingspan = wingspan
        self.flight = flight

    def info(self):
        Basic_info = super().info()
        info = f"{Basic_info},Wingspan: {self.wingspan},Flight: {self.flight}."
        return info

class Reptiles(Animal):
    def __init__(self, name, age, habitat, pattern , venomous):
        super().__init__(name, age, habitat)
        self.pattern = pattern
        self.venomous = venomous

    def info(self):
        Basic_info = super().info()
        info = f"{Basic_info},Pattern: {self.pattern},Venomous: {self.venomous}."
        return info
    

# Creating instances of each animal type
lion = Mammals("Lion", 5, "Savannah", "Short", "Carnivore")
eagle = Birds("Eagle", 3, "Mountains", "2 meters", "3000 meters")
snake = Reptiles("Python", 2, "Rainforest", "Spotted", False)

    # Displaying their information
print(lion.display_info())
print(eagle.display_info())
print(snake.display_info())

    # Changing availability status
lion.mark_quarantine()
eagle.mark_available()
snake.mark_quarantine()

    # Displaying updated information
print("\nAfter changing availability:")
print(lion.display_info())
print(eagle.display_info())
print(snake.display_info())                                         

