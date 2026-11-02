EXPERIMENT 4 - DNS LOOKUP
=========================

WHAT THIS LAB DOES
Forward lookup: domain name to IP address. Reverse lookup: IP address to domain name.
It uses the computer's DNS settings. There is no server to start.

FILES
  dns.py   The program

SETUP (DO THIS ONCE ON EACH COMPUTER)
-------------------------------------
Nothing needs to be installed with pip, and no internet is needed except for looking up real internet domains.
You only need Python 3 (tested on 3.12 and 3.14).

1. Copy this Lab_4 folder from the pen drive to the Desktop.

2. Open a terminal inside the folder:
     Windows: open Lab_4 in File Explorer, click the address bar, type cmd, press Enter.
     Ubuntu : open Lab_4 in Files, right-click empty space, choose Open in Terminal.
   To open a second terminal, repeat this step.

3. Check Python:
     Windows: python --version
     Ubuntu : python3 --version

   In this README, type python on Windows and python3 on Ubuntu.
   If Windows says python is not found, try: py --version
   and then use py instead of python.

   If Python is missing, run Offline_Setup\python-3.12.10-amd64.exe from the
   pen drive, tick "Add python.exe to PATH", click Install Now, then open a new terminal.

RUN IT
------
In the terminal inside Lab_4:
    python dns.py

Forward lookup:
    Enter your choice: 1
    Enter domain name: google.com
    IP Address: 192.178.193.113      (your IP may be different; this is normal)

Reverse lookup (run the program again):
    Enter your choice: 2
    Enter IP address: 8.8.8.8
    Domain Name: dns.google

IF THERE IS NO INTERNET
-----------------------
These work offline:
    Choice 1, domain name: localhost    gives 127.0.0.1
    Choice 2, IP address : 127.0.0.1    gives this computer's name for that address.
                                        The name can differ between computers.

To compare with the system's own tool (needs internet):
    nslookup google.com

NOTES
-----
- "Domain name not found!" means the name does not exist, or there is no internet or DNS access.
- "IP address not found!" means no PTR record exists for that IP. Many IPs have none, so
  this is not a program error. 8.8.8.8 does have one.
- Forward lookup returns one IPv4 address. Large sites may give a different one each time.
