# **CMPT 371 A3 Socket Programming `Interactive-Remote-Terminal`**

**Course:** CMPT 371 \- Data Communications & Networking  
**Instructor:** Mirza Zaeem Baig  
**Semester:** Spring 2026  

## **Group Members**

| Name | Student ID | Email |
| :---- | :---- | :---- |
| Isaac Liu | 301544334 | itl3@sfu.ca |

## **1\. Project Overview & Description**

This project allows you to connect to other computer's terminal to perform terminal commands.

## **2\. System Limitations & Edge Cases**

As required by the project specifications, we have identified and handled (or defined) the following limitations and potential issues within our application scope:

* **Single Client Limitation:** 
  * <span style="color: red;">*Limitation:*</span> Server handles only one client at a time. If multiple clients try to connect simultaneously, others must wait.
  * <span style="color: green;">*Potential Solution:*</span> Utilize python threads to support multiple clients.
* **Buffer Size / Output Limits:** 
  * <span style="color: red;">*Limitation:*</span> If command output exceeds 1024 bytes (or the socket buffer), it may truncate output or block
  * <span style="color: purple;">*Edge Case:*</span> Running `dir /s` or `ls -R` in a large directory could fail to display complete output

## **3\. Video Demo**

<span style="color: purple;">***RUBRIC NOTE: Include a clickable link.***</span>  
Our 2-minute video demo:  
[**▶️ Watch Project Demo on YouTube**](link)

## **4\. Prerequisites (Fresh Environment)**

To run this project, you need:

* **Python 3.10** or higher.  
* A `.env` file containing host and port for the server (refer to `.env-example`)
* No external pip installations are required (uses standard socket, subprocess, os, sys, dotenv).  
* (Optional) VS Code or Terminal.

## **4\. Step-by-Step Run Guide**

<span style="color: purple;"></span>


### **Step 1: Start the Server**

Open your terminal and navigate to the project folder. The server binds to 127.0.0.1 on port 8081\.  
```bash
python src/server.py  
# Binding the Port: 8081
```

### **Step 2: Connect User (client)**

Open a **new** terminal window (keep the server running). Run the client script to start the first client.  
```bash
python src/client.py  
# Connected to server at 127.0.0.1:8081
# C:\Users\You\interative-remote-terminal>

# Server console output: 
# Connection has been established
# IP: 127.0.0.1 | Port 
```

### **Step 3: Commands**

**Navigation Commands**
| OS | Command | Description |
|----|---------|-------------|
| Windows | `dir` | List files and folders in the current directory |
| Windows | `cd <folder>` | Change directory |
| Windows | `cd ..` | Go up one directory |
| Windows | `mkdir <folder>` | Create a new folder |
| Windows | `rmdir <folder>` | Remove an empty folder |
| Linux/macOS | `ls` | List files and folders |
| Linux/macOS | `cd <folder>` | Change directory |
| Linux/macOS | `cd ..` | Go up one directory |
| Linux/macOS | `mkdir <folder>` | Create a new folder |
| Linux/macOS | `rm -r <folder>` | Remove folder recursively |

---

**File Operations**

| OS | Command | Description |
|----|---------|-------------|
| Windows | `type <file>` | Display contents of a file |
| Linux/macOS | `cat <file>` | Display contents of a file |
| Windows | `copy <src> <dest>` | Copy a file |
| Linux/macOS | `cp <src> <dest>` | Copy a file |
| Windows | `move <src> <dest>` | Move or rename a file |
| Linux/macOS | `mv <src> <dest>` | Move or rename a file |
| Windows | `del <file>` | Delete a file |
| Linux/macOS | `rm <file>` | Delete a file |

---

**System Commands**

| Command | Description |
|---------|-------------|
| `echo <text>` | Print text to the console |
| `hostname` | Show the computer’s hostname |
| `whoami` | Show the current user |
| `ipconfig` (Windows) / `ifconfig` or `ip a` (Linux/macOS) | Show network configuration |
| `tasklist` (Windows) / `ps aux` (Linux/macOS) | Show running processes |

---

**Exit Commands**
| Command | Description |
|---------|-------------|
| `quit` | Disconnects the client from the server and exits the session |


## **5\. Technical Protocol Details (Plain-Text over TCP)**

* **Connection**
	* The client connects to the server using TCP
	* Server binds to host and port (from `.env` file) and listens for incoming connection
	* Client connects using same host and port
	* Server acknowledges connection by sending current working directory (CWD) to client

* **Message Format**
	* All messages are plain UTF-8 text
	* Client commands are sent as strings
	* Server responses are stdout/stderr output from executing commands

* **Flow**
	* 1. Server sends CWD -> Client displays prompt
	* 2. Client sends command -> Server executes
	* 3. Server sends output -> Client prints output
	* 4. Repeat until client sends `"quit"` or connection is closed

* **Disconnect Handling**
	* If client disconnects unexpectedly, the server detects a broken socket and closes the session
	* If server shuts down, the client receives no data and prints `"Server disconnected."`



## **6\. Academic Integrity & References**
   
Note AI usage if needed
Add references if needed
* **References:**  
  * [TA Tutorials](https://youtube.com/playlist?list=PL-8C2cUhmkO1yWLTCiqf4mFXId73phvdx&si=xMGsZF95e33OEMrb)