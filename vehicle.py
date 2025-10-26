from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class BMW(Vehicle):
    def start_engine(self):
        print("BMW engine started with a roar!")

    def drive(self):
        print("BMW is cruising on the highway.")

    def stop_engine(self):
        print("BMW engine stopped.")


class Ferrari(Vehicle):
    def start_engine(self):
        print("Ferrari engine ignited with a thunder!")

    def drive(self):
        print("Ferrari is racing on the track.")

    def stop_engine(self):
        print("Ferrari engine shut down.")


def test_drive(vehicle: Vehicle):
    vehicle.start_engine()
    vehicle.drive()
    vehicle.stop_engine()


bmw_car = BMW()
ferrari_car = Ferrari()


print("Testing BMW:")
test_drive(bmw_car)

print("\nTesting Ferrari:")
test_drive(ferrari_car)