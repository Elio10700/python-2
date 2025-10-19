# Parent class
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100  # Base fare per person is 100

# Child class
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10  # 10% extra charge
        total_fare = base_fare + maintenance_charge
        return total_fare

# Example usage
bus = Bus(50)  # Bus with 50 passengers
print("Total Bus Fare:", bus.fare())