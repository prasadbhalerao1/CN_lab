EXPERIMENT 9 - WEB SERVER USING THE CLIENT-SERVER MODEL
======================================================

WHAT THIS LAB DOES
Runs a small web server with Python's built-in http.server. A browser or a TCP socket client
requests pages from it using HTTP.

PORT: TCP 8000

FILES
  server.py    Web server. Keeps running for many clients
  client.py    HTTP client written with a plain TCP socket
  website\     Demo website:
                 index.html, about.html, style.css, logo.png, notes.txt

SETUP (DO THIS ONCE ON EACH COMPUTER)
-------------------------------------
Nothing needs to be installed with pip, and no internet is needed.
You only need Python 3 (tested on 3.12 and 3.14).

1. Copy this Lab_9_Web_Server folder from the pen drive to the Desktop.

2. Open a terminal inside the folder:
     Windows: open Lab_9_Web_Server in File Explorer, click the address bar, type cmd, press Enter.
     Ubuntu : open Lab_9_Web_Server in Files, right-click empty space, choose Open in Terminal.
   To open a second terminal, repeat this step.

3. Check Python:
     Windows: python --version
     Ubuntu : python3 --version

   In this README, type python on Windows and python3 on Ubuntu.
   If Windows says python is not found, try: py --version
   and then use py instead of python.

   If Python is missing, run Offline_Setup\python-3.12.10-amd64.exe from the
   pen drive, tick "Add python.exe to PATH", click Install Now, then open a new terminal.

RUN IT (ONE COMPUTER)
---------------------
Terminal 1, inside Lab_9_Web_Server - start the server first:
    python server.py

    It shows: Web Server is running on port 8000...
    Leave this terminal running.

Option 1 - browser. Open:
    http://127.0.0.1:8000/index.html

Also try these:
    http://127.0.0.1:8000/about.html
    http://127.0.0.1:8000/notes.txt
    http://127.0.0.1:8000/missing.html     (404 File not found)

Option 2 - socket client. Terminal 2, inside Lab_9_Web_Server:
    python client.py

EXPECTED OUTPUT
---------------
client.py prints the raw HTTP response:
    HTTP/1.0 200 OK
    Server: SimpleHTTP/...
    Content-type: text/html
    ...
    <!DOCTYPE html>
    ...

The server terminal logs each request:
    127.0.0.1 - - [date] "GET /index.html HTTP/1.1" 200 -

The browser shows "Welcome to My Web Server!" with a test pattern image and two links.

TWO COMPUTERS
-------------
The server listens on 0.0.0.0, so it accepts connections on every network address of
any computer. You never need to edit an IP address in the code. Do not type 0.0.0.0
as the client's address; give the client the server computer's real IP instead.

1. Connect both computers to the same network.

2. On the SERVER computer, find its IP address:
     Windows: ipconfig        (read the IPv4 Address line)
     Ubuntu : hostname -I

3. Allow TCP port 8000 on the SERVER computer if its firewall is on:
     Windows: click Allow if a Windows Security popup appears. Or, in a terminal opened
              with Run as administrator:
              netsh advfirewall firewall add rule name="Lab TCP 8000" dir=in action=allow protocol=TCP localport=8000
              Remove it afterwards:
              netsh advfirewall firewall delete rule name="Lab TCP 8000"
     Ubuntu : sudo ufw allow 8000/tcp

4. Start the server on the SERVER computer as usual.

5. On the CLIENT computer, add the server's IP to the client command. Example:
     python client.py 192.168.1.35

If it fails, run this on the client first: ping <server_ip>
No reply usually means the network or firewall blocks the computers (college Wi-Fi often does).

In a browser on the client computer, open:
    http://192.168.1.35:8000/index.html
Use the server's real IP. Do not type 0.0.0.0.

STOP THE SERVER AND FREE THE PORT
---------------------------------
Press Ctrl+C in the server terminal. If it does not stop on Windows, close that terminal window.

Check that port 8000 is free (no output means it is free):
    Windows: netstat -ano | findstr :8000
    Ubuntu : ss -lntup | grep :8000

If something is still using it, stop that process using the PID shown at the end of the line:
    Windows: taskkill /PID <PID> /F
    Ubuntu : kill <PID>

A KeyboardInterrupt message after Ctrl+C is normal.

NOTES
-----
- Add your own pages by putting files in the website folder. No restart is needed.
- The page opened at http://127.0.0.1:8000/ is index.html.
- "Address already in use" or WinError 10048 means another server is on port 8000. Free it as above.
- This is Python's development web server, not Apache or Nginx. Use it for lab work only.
