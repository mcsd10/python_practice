byy = int(input("Enter your birth year: "))
bmm = int(input("Enter your birth month: "))
bdd = int(input("Enter your birth day: "))
cyy = int(input("Enter current year: "))
cmm = int(input("Enter current month: "))
cdd = int(input("Enter current day: "))
if cdd < bdd:
    cmm = cmm - 1
    cdd = cdd + 30
day = cdd - bdd
if cmm < bmm:
    cyy = cyy - 1
    cmm = cmm + 12
years = cyy - byy
months = cmm - bmm
days = day + months * 30 + years * 36
hh = days * 24
mm = hh * 60
ss = mm * 60
print("Old is: {0}, {1}, {2}".format(years, months, days))
print("Hour is (hh:mm:ss): {0}:{1}:{2}".format(hh, mm, ss))
