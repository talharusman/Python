class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = base_fare * 0.10
        return base_fare + maintenance_charge

bus = Bus(50)

fare = bus.calculate_fare()
print(f"The total fare for the bus is ${fare:.2f}")