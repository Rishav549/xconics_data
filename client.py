import socket

try:
    c = socket.socket()
    c.connect(('127.0.0.1', 8111))
    data = input("Enter the Data: ")
    c.send(bytes(data, 'utf-8'))
except Exception as e:
    print("Error connecting to the server:", e)
finally:
    c.close()