nums = [1, 2, 3, 2, 4, 1]
duplicates = set()

for n in nums:
    if nums.count(n) > 1:
        duplicates.add(n)

print("Duplicates:", duplicates)
