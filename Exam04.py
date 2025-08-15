class Dog:
    def __init__(self, breed, color, height, weight):
        self.breed = breed
        self.color = color
        self.height = height
        self.weight = weight

    def growth(self):
        self.height *= 1.10
        self.weight *= 1.10
dog_A = Dog("Jack russell Terrier", "White", 30, 7)
dog_A.growth()

print('height =', dog_A.height)
print('weight =', dog_A.weight)