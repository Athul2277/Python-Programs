email = input("Enter email: ")

parts = email.split("@")

if len(parts) == 2:
    username = parts[0]
    domain = parts[1]

    print("Username:", username)
    print("Domain:", domain)
else:
    print("Invalid email")

print("Done processing")
