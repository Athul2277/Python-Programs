
import socket

target = input("Enter hostname or IP: ")
for port in range(1, 1025):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.settimeout(0.3)
    result = connection.connect_ex((target, port))
    if result == 0:
        print("Open port:", port)
    connection.close()
