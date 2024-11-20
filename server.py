import socket
from db.db import SessionLocal
from crud.crud import create_data_packet

def tcp_server():
    s = socket.socket()
    print("Socket is Created")

    s.bind(('0.0.0.0', 8111))

    s.listen(5)
    print("Waiting For connection, server Started")

    while True:
        c, address = s.accept()
        print("Connected With", address)

        data = c.recv(1024).decode()

        c.close()

        print("Received Data: ", data)

        try: 
            db = SessionLocal()
            create_data_packet(db=db,data=data)
            print("Data Saved to the Database")
        except Exception as e:
            print("Error saving data:", e)

            c.close()
