import socket
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

s = socket.socket()
host = os.getenv("HOST")
port = int(os.getenv("PORT"))

s.connect((host, port))
while True:
    cwd = str(s.recv(1024), "utf-8")
    cmd = input(cwd)
    if len(str.encode(cmd)) > 0:
        s.send(str.encode(cmd))
        if (cmd == "quit"):
            break
        server_res = str(s.recv(1024), "utf-8")
        print("Server output: ")
        print(server_res, end="")