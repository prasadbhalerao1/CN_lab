EXPERIMENT 7 - SECURE CLIENT-SERVER COMMUNICATION USING SSL/TLS
===============================================================

WHAT THIS LAB DOES
A TCP client and server exchange a message over an encrypted TLS connection. The client checks
the server's certificate before it sends anything.

PORT: TCP 8443

FILES
  server.py    TLS server. Keeps running for many clients
  client.py    TLS client
  server.crt   Certificate (public). Already generated, valid until 1 Nov 2027
  server.key   Private key. Already generated. Used by the server only

SETUP (DO THIS ONCE ON EACH COMPUTER)
-------------------------------------
Nothing needs to be installed with pip, and no internet is needed.
You only need Python 3 (tested on 3.12 and 3.14).

1. Copy this Lab_7_TLS folder from the pen drive to the Desktop.

2. Open a terminal inside the folder:
     Windows: open Lab_7_TLS in File Explorer, click the address bar, type cmd, press Enter.
     Ubuntu : open Lab_7_TLS in Files, right-click empty space, choose Open in Terminal.
   To open a second terminal, repeat this step.

3. Check Python:
     Windows: python --version
     Ubuntu : python3 --version

   In this README, type python on Windows and python3 on Ubuntu.
   If Windows says python is not found, try: py --version
   and then use py instead of python.

   If Python is missing, run Offline_Setup\python-3.12.10-amd64.exe from the
   pen drive, tick "Add python.exe to PATH", click Install Now, then open a new terminal.

The certificate is already in this folder, so OpenSSL is not needed to run the lab.

RUN IT (ONE COMPUTER)
---------------------
You need two terminals, both inside Lab_7_TLS.

Terminal 1 - start the server first:
    python server.py

    It shows: Secure Server is listening...
    Leave this terminal running.

Terminal 2 - run the client:
    python client.py

EXPECTED OUTPUT
---------------
Client:
    Connected securely!
    TLS Version: TLSv1.3
    Server: Secure message received!

Server:
    Connected by: ('127.0.0.1', <port>)
    TLS Version: TLSv1.3
    Client: Hello Server!

HOW THE CERTIFICATE WAS MADE (AND HOW TO MAKE A NEW ONE)
--------------------------------------------------------
Only do this if the certificate has expired or your teacher wants to see it made. It needs
OpenSSL. Run it in Windows cmd or an Ubuntu terminal inside Lab_7_TLS, as one line:

    openssl req -x509 -newkey rsa:2048 -sha256 -nodes -days 365 -keyout server.key -out server.crt -subj "/CN=localhost" -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

It replaces both server.key and server.crt. Restart the server afterwards. In Git Bash, put
MSYS_NO_PATHCONV=1 before openssl or the /CN part is changed.

What the options mean:
    req -x509            Create a self-signed certificate
    -newkey rsa:2048     Create a new 2048-bit RSA key
    -sha256              Sign using SHA-256
    -nodes               Do not put a password on the key
    -days 365            Valid for one year
    -subj "/CN=localhost"  The certificate's name
    -addext ...          Names the certificate is valid for

To view the certificate:
    openssl x509 -in server.crt -noout -subject -enddate -ext subjectAltName

TWO COMPUTERS
-------------
The server listens on 0.0.0.0, so it accepts connections on every network address of
any computer. You never need to edit an IP address in the code. Do not type 0.0.0.0
as the client's address; give the client the server computer's real IP instead.

1. Connect both computers to the same network.

2. On the SERVER computer, find its IP address:
     Windows: ipconfig        (read the IPv4 Address line)
     Ubuntu : hostname -I

3. Allow TCP port 8443 on the SERVER computer if its firewall is on:
     Windows: click Allow if a Windows Security popup appears. Or, in a terminal opened
              with Run as administrator:
              netsh advfirewall firewall add rule name="Lab TCP 8443" dir=in action=allow protocol=TCP localport=8443
              Remove it afterwards:
              netsh advfirewall firewall delete rule name="Lab TCP 8443"
     Ubuntu : sudo ufw allow 8443/tcp

4. Start the server on the SERVER computer as usual.

5. On the CLIENT computer, add the server's IP to the client command. Example:
     python client.py 192.168.1.35

If it fails, run this on the client first: ping <server_ip>
No reply usually means the network or firewall blocks the computers (college Wi-Fi often does).

Certificate note for two computers: the client needs client.py and server.crt, but not
server.key. The certificate does not need the server's IP, because client.py always checks for
the name localhost. If you make a new certificate, copy the new server.crt to the client too.

STOP THE SERVER AND FREE THE PORT
---------------------------------
Press Ctrl+C in the server terminal. If it does not stop on Windows, close that terminal window.

Check that port 8443 is free (no output means it is free):
    Windows: netstat -ano | findstr :8443
    Ubuntu : ss -lntup | grep :8443

If something is still using it, stop that process using the PID shown at the end of the line:
    Windows: taskkill /PID <PID> /F
    Ubuntu : kill <PID>

NOTES
-----
- This is server authentication only. The client checks the server; the server does not check the client.
- The certificate is self-signed, so it suits a lab only. The client trusts it because
  client.py loads server.crt directly.
- server.key is private, and only a demo key here. Do not reuse it for anything real.
- A connection that fails the TLS handshake prints "Rejected connection" and the server keeps running.
- CERTIFICATE_VERIFY_FAILED usually means the certificate has expired, the computer's date is
  wrong, or the client's server.crt does not match the server's. Check the date first.
