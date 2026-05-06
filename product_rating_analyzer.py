ratings = [5, 4, 4, 3, 5, 2, 5]

avg = sum(ratings) / len(ratings)

print("Average rating:", round(avg, 2))

if avg >= 4:
    print("Product is good ")
else:
    print("Needs improvement ")
