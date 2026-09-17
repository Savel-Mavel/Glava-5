import math

def square(side):
    area = side * side

    if not isinstance(area, int):
        area = math.ceil(area)
    
    return area

print("Площадь квадрата со стороной 5:", square(5))
print("Площадь квадрата со стороной 2.5:", square(2.5))
print("Площадь квадрата со стороной 3.3:", square(3.3))
print("Площадь квадрата со стороной 7:", square(7))  