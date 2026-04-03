import time

task = input("Enter task: ")
seconds = int(input("Remind after (sec): "))

print("Reminder set...")

time.sleep(seconds)

print("Reminder:", task)
print("Don't forget!")
