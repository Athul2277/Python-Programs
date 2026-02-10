nums = [5, 3, 8, 1, 9]
minimum = nums[0]

for n in nums:
    if n < minimum:
        minimum = n

print("Minimum value:", minimum)
