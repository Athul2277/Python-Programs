
temperatures = [29, 31, 30, 34, 36, 32, 28]

average = sum(temperatures) / len(temperatures)
hot_days = sum(temp >= 35 for temp in temperatures)

print("Average Temperature:", round(average, 2))
print("Maximum Temperature:", max(temperatures))
print("Minimum Temperature:", min(temperatures))
print("Hot Days:", hot_days)

if average >= 33:
    print("Above Average Heat Detected")
