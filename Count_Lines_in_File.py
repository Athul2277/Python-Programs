file = open("sample.txt", "r")
count = 0

for _ in file:
    count += 1

print("Lines:", count)
