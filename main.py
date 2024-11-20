from db.db import engine, Base
from server import tcp_server
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    tcp_server()