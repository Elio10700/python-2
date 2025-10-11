class Parrot:
    species = "maccaw"

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Parrot("Jiggles", 2)
p2 = Parrot("Bill", 3)

print("The species is", p1.species)
print("The name of the parrot is", p1.name)
print("The age of the parrot is", p1.age)

print("The species is", p2.species)
print("The name of the parrot is", p2.name)
print("The age of the parrot is", p2.age)
