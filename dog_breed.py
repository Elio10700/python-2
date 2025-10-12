class Dog:
    # class variable
    species = "Canis lupus familiaris"

    def __init__(self, name, breed):
        # two instance variables
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}"


# Instantiating two dogs of different breeds
if __name__ == "__main__":
    dog1 = Dog("Bella", "Labrador Retriever")
    dog2 = Dog("Max", "German Shepherd")

    # Printing details of the dogs
    print(dog1)
    print(dog2)
   
    