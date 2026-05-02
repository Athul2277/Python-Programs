cgpa = float(input("Enter CGPA: "))
skills = int(input("Number of skills: "))
backlogs = int(input("Backlogs: "))

if cgpa >= 7 and skills >= 3 and backlogs == 0:
    print("Placement Ready ")
else:
    print("Needs Improvement ")
