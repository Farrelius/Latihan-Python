import math

def circle_area_with_diameter():
    diameter = float(input("Masukkan diameter lingkaran: "))
    radius = diameter / 2
    area =  math.pi* (radius ** 2)
    print("Luas lingkaran:", area)

circle_area_with_diameter()