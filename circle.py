import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display(self):
        print("🌟 Circle Geometry 🌟")
        print(f"🔵 Radius: {self.radius}")
        print(f"📐 Area: {self.area():.2f}")
        print(f"📏 Perimeter: {self.perimeter():.2f}")
        print("✨ Keep exploring the magic of math and code! ✨")

# Example usage
if __name__ == "__main__":
    try:
        r = float(input("Enter the radius of the circle: "))
        my_circle = Circle(r)
        my_circle.display()
    except ValueError:
        print("⚠️ Please enter a valid number for the radius.")