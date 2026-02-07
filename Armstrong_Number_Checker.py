num = int(input("Enter a number: "))
total = 0

for d in str(num):
    total += int(d) ** 3

print("Armstrong" if total == num else "Not Armstrong")
