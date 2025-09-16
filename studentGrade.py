id1 = -1
id2 = -1
max1 = -1
max2 = -1
n = int(input("Enter number of students: "))
if n < 2:
    print("Please enter at least 2 students")
else:
    for i in range(1, n + 1):
        id = int(input("Enter student ID: "))
        aver = float(input("Enter student average: "))
        if aver > max1:
            max2 = max1
            id2 = id1
            max1 = aver
            id1 = id
        elif aver > max2:
            max2 = aver
            id2 = id
            print("max2=", max2, '\t', "id2=", id2)
