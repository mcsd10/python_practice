y1 = int(input( "Enter the price for current year: "))
y2 = int(input( "Enter the price for second year: "))
t = (float)(y2 - y1) / y1 * 100
y3 = y2 + y2 * t
print("Extra=%", t, "\t\tPrice next year = ", y3)
