tasks = int(input("Tasks completed: "))
rating = float(input("Manager rating (out of 5): "))

score = (tasks * 2) + (rating * 10)

print("Performance score:", score)

if score > 80:
    print("Excellent ")
else:
    print("Average ")
