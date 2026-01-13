
import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    print("CPU Usage:", cpu, "%")
    print("Memory Usage:", memory, "%")
    print("Disk Usage:", disk, "%")

    if cpu > 85 or memory > 90 or disk > 95:
        print("System resource warning detected")
