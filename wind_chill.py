import math
v = float(input( "Enter wind speed in kilometers per hour: "))
t = float( input( "Enter temperature in degrees Celsius: "))
wci = 13.12 + 0.6215*t - 11.37*math.pow(v,0.16) + 0.3965 * t*math.pow(v,0.16)
print( " The wind chill index is ", int(round(wci,0)))

