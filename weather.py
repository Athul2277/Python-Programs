temps = []

while True:
    t = input("Enter temperature or exit: ")
    if t == "exit":
        break
    temps.append(float(t))

print("Average:", sum(temps)/len(temps))
print("Max:", max(temps))
print("Min:", min(temps))