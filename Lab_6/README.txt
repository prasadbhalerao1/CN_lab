EXPERIMENT 6 - TCP SOCKET PROGRAMMING
====================================

WHAT THIS LAB DOES
Three separate TCP client-server programs: Hello, file transfer, and an arithmetic calculator.

PORTS: Hello TCP 5000, File transfer TCP 5001, Calculator TCP 5002

FILES
  hello_server.py, hello_client.py   Task 1
  file_server.py, file_client.py     Task 2
  calc_server.py, calc_client.py     Task 3
  server_files\                      Files the file server can send:
                                       sample.txt, sample_image.png

SETUP (DO THIS ONCE ON EACH COMPUTER)
-------------------------------------
Nothing needs to be installed with pip, and no internet is needed.
You only need Python 3 (tested on 3.12 and 3.14).

1. Copy this Lab_6 folder from the pen drive to the Desktop.

2. Open a terminal inside the folder:
     Windows: open Lab_6 in File Explorer, click the address bar, type cmd, press Enter.
     Ubuntu : open Lab_6 in Files, right-click empty space, choose Open in Terminal.
   To open a second terminal, repeat this step.

3. Check Python:
     Windows: python --version
     Ubuntu : python3 --version

   In this README, type python on Windows and python3 on Ubuntu.
   If Windows says python is not found, try: py --version
   and then use py instead of python.

   If Python is missing, run Offline_Setup\python-3.12.10-amd64.exe from the
   pen drive, tick "Add python.exe to PATH", click Install Now, then open a new terminal.

IMPORTANT: each server here handles ONE client and then exits by itself. This frees its
port. To run a task again, start its server again first.

You need two terminals, both inside Lab_6.

TASK 1 - HELLO
--------------
Terminal 1:  python hello_server.py
             Shows: Server is waiting for connection...
Terminal 2:  python hello_client.py

Client shows:
    Server: Hello Client!
Server shows:
    Connected by: ('127.0.0.1', <port>)
    Client: Hello Server!

TASK 2 - FILE TRANSFER
----------------------
Terminal 1:  python file_server.py
             Shows: File Server is waiting...
Terminal 2:  python file_client.py
             Enter filename: sample.txt

Client shows:  File received successfully!
Server shows:  File sent successfully!

The file is saved in Lab_6 as received_sample.txt.
Repeat the two commands with sample_image.png to transfer a binary file.
Enter only the file name, not a path. A name that is not in server_files gives:
    ERROR: File not found

To serve your own file, copy it into server_files first.

TASK 3 - CALCULATOR
-------------------
Terminal 1:  python calc_server.py
             Shows: Calculator Server is waiting...
Terminal 2:  python calc_client.py
             Enter first number: 7
             Enter operator (+, -, *, /): +
             Enter second number: 5

Client shows:  Result: 12.0

Other results:
    7 / 0   Division by zero!
    7 % 2   Invalid operator!
    abc + 2 Invalid input!

TWO COMPUTERS
-------------
The server listens on 0.0.0.0, so it accepts connections on every network address of
any computer. You never need to edit an IP address in the code. Do not type 0.0.0.0
as the client's address; give the client the server computer's real IP instead.

1. Connect both computers to the same network.

2. On the SERVER computer, find its IP address:
     Windows: ipconfig        (read the IPv4 Address line)
     Ubuntu : hostname -I

3. Allow TCP port 5000, 5001 or 5002 on the SERVER computer if its firewall is on:
     Windows: click Allow if a Windows Security popup appears. Or, in a terminal opened
              with Run as administrator:
              netsh advfirewall firewall add rule name="Lab 6" dir=in action=allow protocol=TCP localport=5000-5002
              Remove it afterwards:
              netsh advfirewall firewall delete rule name="Lab 6"
     Ubuntu : sudo ufw allow 5000:5002/tcp

4. Start the server on the SERVER computer as usual.

5. On the CLIENT computer, add the server's IP to the client command. Example:
     python hello_client.py 192.168.1.35

If it fails, run this on the client first: ping <server_ip>
No reply usually means the network or firewall blocks the computers (college Wi-Fi often does).

STOP THE SERVER AND FREE THE PORT
---------------------------------
Press Ctrl+C in the server terminal. If it does not stop on Windows, close that terminal window.

Check that port 5000 (or 5001, 5002) is free (no output means it is free):
    Windows: netstat -ano | findstr :5000
    Ubuntu : ss -lntup | grep :5000

If something is still using it, stop that process using the PID shown at the end of the line:
    Windows: taskkill /PID <PID> /F
    Ubuntu : kill <PID>

NOTES
-----
- These servers stop by themselves after one client, so the port is normally already free.
- "connection refused" or WinError 10061 means the server is not running. It may have
  already finished, so start it again.
- Results are decimals (12.0) because the server converts numbers to floats.
