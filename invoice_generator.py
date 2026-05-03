customer = input("Customer name: ")
items = [100, 200, 150]

total = sum(items)
tax = total * 0.18
final = total + tax

print("Customer:", customer)
print("Items:", items)
print("Subtotal:", total)
print("Tax (18%):", tax)
print("Final Amount:", final)
