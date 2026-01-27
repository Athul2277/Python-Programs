import time

alarm = input("Set alarm (HH:MM): ")

while True:
    if time.strftime("%H:%M") == alarm:
        print("Wake up!")
        break
