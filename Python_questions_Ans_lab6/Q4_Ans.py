import math

a = 5
b = 6
c = 7 # Sides of the triangle

s = (a + b + c) / 2 # Semi-perimeter

area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"The area of the triangle is: {area}")
