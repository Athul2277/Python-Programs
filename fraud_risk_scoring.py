amount = float(input("Transaction amount: "))
new_device = input("New device? yes/no: ").lower()
late_night = input("Late night transaction? yes/no: ").lower()

score = 0
if amount > 20000: score += 40
if new_device == "yes": score += 30
if late_night == "yes": score += 30

print("Risk Score:", score)

if score >= 60:
    print("High Risk 🚨")
