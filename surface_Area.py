pi = 22/7
height = float(input("Height of cylinder: "))
radius = float(input("Radius of cylinder: "))
volume = (pi * radius**2) * height
sur_area =((2 * pi * radius) * height) + ((pi * radius**2) * 2)
print("Volume of cylinder is: ", volume)
print("Surface area of cylinder is: ", sur_area)