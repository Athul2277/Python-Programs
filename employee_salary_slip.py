name = input("Employee name: ")
basic = float(input("Basic salary: "))

hra = basic * 0.20
bonus = basic * 0.10
net = basic + hra + bonus

print("Name:", name)
print("Net Salary:", net)
