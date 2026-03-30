correct_password = "admin123"
attempts = 3

while attempts > 0:
    user = input("Enter password: ")

    if user == correct_password:
        print("Access granted ✅")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

if attempts == 0:
    print("Account locked ❌")
