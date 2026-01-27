balance = 5000

withdraw = int(input("Enter amount: "))
if withdraw <= balance:
    balance -= withdraw
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")
