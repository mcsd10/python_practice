while True:
    m = int(input( "Enter required money: "))
    tedad = int(input( "Enter number of monaths:"))
    s = int(input("Enter profit rate:  "))
    k = (12 * m) / (12 - tedad * s / 100)
    p = k / tedad
    print( "k = ", k, '\t', p)
    ansi = input("Do you want to continue? (y/n): ")
    if ansi.lower() == 'n':
        break