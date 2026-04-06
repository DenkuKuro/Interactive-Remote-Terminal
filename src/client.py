import socket
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

s = socket.socket()
host = os.getenv("HOST")
port = int(os.getenv("PORT"))

# Connect to server
try:
    s.connect((host, port))
    print(f"Connected to server at {host}:{port}")
except socket.error as e:
    print(f"Error connecting to server: {e}")
    exit()

while True:
    cwd = s.recv(1024)
    if not cwd: 
        print("\nServer disconnected.")
        break
    cwd = cwd.decode("utf-8")
    cmd = input(cwd)
    if len(str.encode(cmd)) > 0:
        s.send(str.encode(cmd))
        if (cmd == "quit"):
            break
        server_res = s.recv(1024)
        if not server_res:
            print("\nServer disconnected.")
            break
        server_res = server_res.decode("utf-8")
        if server_res != "\n":
            print(server_res, end="")

s.close()
print("Client socket closed.")