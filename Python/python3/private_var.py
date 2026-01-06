import math

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius
    
if __name__ == "__main__":
    circle = Circle()