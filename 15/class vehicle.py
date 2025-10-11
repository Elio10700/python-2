class Vehicle:
    def __init__(self, maxspeed, mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

car = Vehicle("120km/h", "15litre")

print("The max speed is", car.maxspeed)
print("The mileage is", car.mileage)
