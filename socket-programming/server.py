import threading
import socket
import time


PORT =5050
#SERVER = "192.168.157.68" #manually typed ip(NOT A GOOD method)
SERVER= socket.gethostbyname(socket.gethostname())
#print(SERVER) #prints out the IP (fetches dynamically)
#print(socket.gethostname())
ADDR=(SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f'new connection aaya ,welcome {addr}')
    connected=True
    


def start():
    server.listen()
    while True:
        conn,addr=server.accept()
        thread = threading.Thread(target=handle_client,args=[conn,addr])
        thread.start()
        print(f'active connections {threading.activeCount() -1}')
