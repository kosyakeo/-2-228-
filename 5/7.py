import math
def point_circle(x: float, y: float, radius: float):
    distance = math.sqrt(x**2 + y**2)
    return distance <= radius
print(point_circle(3, 4, 5))
print(point_circle(6, 8, 5))