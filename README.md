# **CMPT 371 A3 Socket Programming `Interactive-Remote-Terminal`**

**Course:** CMPT 371 \- Data Communications & Networking
**Instructor:** Mirza Zaeem Baig
**Semester:** Spring 2026

## **Group Members**

| Name           | Student ID | Email         |
| :------------- | :--------- | :------------ |
| Isaac Liu      | 301544334  | itl3@sfu.ca   |
| Javier Deng Xu | 301637487  | jda174@sfu.ca |
| Angelo Yap     | 301634608  | aay5@sfu.ca   |

## **1\. Project Overview & Description**

This project is a socket-based remote terminal application that lets a client connect to a server and execute terminal commands on the host machine.

## **2\. System Limitations & Edge Cases**

As required by the project specifications, we have identified and handled (or defined) the following limitations and potential issues within our application scope:

* **Single Client Limitation:**
  * **Limitation:** Server accepts one client session, then exits after that client disconnects. Additional clients cannot connect until the server is started again.
  * **Potential Solution:** Utilize python threads to support multiple clients.
* **Buffer Size / Output Limits:**
  * **Limitation:** If command output exceeds 1024 bytes (or the socket buffer), it may truncate output or block.
  * **Edge Case:** Running `dir /s` or `ls -R` in a large directory could fail to display complete output.

## **3\. Video Demo**

Our 2-minute video demo:
[**▶️ Watch Project Demo on YouTube**](
https://youtu.be/2jGgGucowtM)

## **4\. Prerequisites (Fresh Environment)**

To run this project, you need:

* **Python 3.10** or higher.
* A `.env` file containing `HOST` and `PORT`.
* Install dependency from `requirements.txt` (used for environment variable loading).
* (Optional) VS Code or Terminal.

## **4\. Step-by-Step Run Guide**

### **Step 0: create .env file containing HOST and PORT**

In the project root, rename `.env-example` to `.env`.
Then open `.env` and set:

```env
HOST=127.0.0.1
PORT=8080 # Or any available port
```

Notes:

* If client and server run on different machines, set the client's `HOST` to the server machine's local IP address.
* Set `PORT` to the same port number used by the server.

Install dependencies:

```bash
pip install -r requirements.txt
```

### **Step 1: Start the Server**

Open your terminal and navigate to the project folder.

```bash
python src/server.py  
# Binding the Port: <PORT from .env>
```

### **Step 2: Connect User (client)**

Open a **new** terminal window (keep the server running), then run:

```bash
python src/client.py  
# Connected to server at <HOST>:<PORT>
# <current working directory> >

# Server console output: 
# Connection has been established
# IP: <client IP> | Port: <client port>
```

### **Step 3: Commands**

At the prompt, type commands and press Enter. The server executes the command and sends the output back to the client.

Type `quit` to disconnect and end the session.

The server executes commands through the host machine shell, so many standard shell commands work.
Support can vary by operating system, shell type, installed tools, and user permissions.

**Navigation Commands**

| OS          | Command             | Description                                     |
| ----------- | ------------------- | ----------------------------------------------- |
| Windows     | `dir`             | List files and folders in the current directory |
| Windows     | `cd <folder>`     | Change directory                                |
| Windows     | `cd ..`           | Go up one directory                             |
| Windows     | `mkdir <folder>`  | Create a new folder                             |
| Windows     | `where <command>` | Locate an executable in PATH                    |
| Windows     | `rmdir <folder>`  | Remove an empty folder                          |
| Linux/macOS | `ls`              | List files and folders                          |
| Linux/macOS | `cd <folder>`     | Change directory                                |
| Linux/macOS | `cd ..`           | Go up one directory                             |
| Linux/macOS | `mkdir <folder>`  | Create a new folder                             |
| Linux/macOS | `pwd`             | Show current directory                          |
| Linux/macOS | `rm -r <folder>`  | Remove folder recursively                       |

---

**File Operations**

| OS          | Command               | Description                |
| ----------- | --------------------- | -------------------------- |
| Windows     | `type <file>`       | Display contents of a file |
| Linux/macOS | `cat <file>`        | Display contents of a file |
| Windows     | `copy <src> <dest>` | Copy a file                |
| Linux/macOS | `cp <src> <dest>`   | Copy a file                |
| Windows     | `move <src> <dest>` | Move or rename a file      |
| Linux/macOS | `mv <src> <dest>`   | Move or rename a file      |
| Windows     | `del <file>`        | Delete a file              |
| Linux/macOS | `rm <file>`         | Delete a file              |
| Linux/macOS | `touch <file>`      | Create an empty file       |

---

**System Commands**

| Command                                                         | Description                   |
| --------------------------------------------------------------- | ----------------------------- |
| `echo <text>`                                                 | Print text to the console     |
| `hostname`                                                    | Show the computer’s hostname |
| `whoami`                                                      | Show the current user         |
| `ipconfig` (Windows) / `ifconfig` or `ip a` (Linux/macOS) | Show network configuration    |
| `tasklist` (Windows) / `ps aux` (Linux/macOS)               | Show running processes        |
| `cls` (Windows) / `clear` (Linux/macOS)                     | Clear terminal output         |

---

**Shell Features**

* Some shell features such as output redirection and piping may only work on specific OS/shell combinations.
* Commands with interactive prompts may behave differently over remote execution.
* Very large command output can still be limited by the current socket buffer handling.

---

**Exit Commands**

| Command  | Description                                                  |
| -------- | ------------------------------------------------------------ |
| `quit` | Disconnects the client from the server and exits the session |

## **5\. Technical Protocol Details (Plain-Text over TCP)**

**Connection**

* The client connects to the server using TCP
* Server binds to all local network interfaces (`0.0.0.0`) on `PORT` (from `.env`) and listens for incoming connection
* Client connects using `HOST` and `PORT` from `.env`
* Server acknowledges connection by sending current working directory (CWD) to client

**Message Format**

* All messages are plain UTF-8 text
* Client commands are sent as strings
* Server responses are stdout/stderr output from executing commands

**Flow**

1. Server sends CWD -> Client displays prompt
2. Client sends command -> Server executes
3. Server sends output -> Client prints output
4. Repeat until client sends `"quit"` or connection is closed

**Disconnect Handling**

* If client disconnects unexpectedly, the server detects a broken socket and closes the session
* If server shuts down, the client receives no data and prints `"Server disconnected."`
* After a client session ends, the current server process exits and must be restarted for a new client session

## **6\. Academic Integrity & References**

* **References:**
  * [TA Tutorials](https://youtube.com/playlist?list=PL-8C2cUhmkO1yWLTCiqf4mFXId73phvdx&si=xMGsZF95e33OEMrb)
