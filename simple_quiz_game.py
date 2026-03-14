score = 0

ans = input("Capital of France? ")
if ans.lower() == "paris":
    score += 1

ans = input("5 + 3 = ? ")
if ans == "8":
    score += 1

ans = input("Color of sky? ")
if ans.lower() == "blue":
    score += 1

print("Your score:", score, "/3")
