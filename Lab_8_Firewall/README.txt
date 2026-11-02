EXPERIMENT 8 - BASIC FIREWALL CONFIGURATION AND TESTING
======================================================

WHAT THIS LAB DOES
Configures a firewall (UFW on Ubuntu) to allow only one authorised client, and uses a small
Python TCP client and server to prove which connections are allowed or blocked.

PORT: TCP 5000

FILES
  server.py          TCP test server. Keeps running for many clients
  client.py          TCP test client. Takes the server IP
  offline_packages\  ufw_0.36.2-6_all.deb, for installing UFW without internet

SETUP (DO THIS ONCE ON EACH COMPUTER)
-------------------------------------
Nothing needs to be installed with pip, and no internet is needed (UFW installs from offline_packages).
You only need Python 3 (tested on 3.12 and 3.14).

1. Copy this Lab_8_Firewall folder from the pen drive to the Desktop.

2. Open a terminal inside the folder:
     Windows: open Lab_8_Firewall in File Explorer, click the address bar, type cmd, press Enter.
     Ubuntu : open Lab_8_Firewall in Files, right-click empty space, choose Open in Terminal.
   To open a second terminal, repeat this step.

3. Check Python:
     Windows: python --version
     Ubuntu : python3 --version

   In this README, type python on Windows and python3 on Ubuntu.
   If Windows says python is not found, try: py --version
   and then use py instead of python.

   If Python is missing, run Offline_Setup\python-3.12.10-amd64.exe from the
   pen drive, tick "Add python.exe to PATH", click Install Now, then open a new terminal.

PART A - CHECK THE PROGRAMS WORK (ONE COMPUTER, NO FIREWALL NEEDED)
------------------------------------------------------------------
You need two terminals, both inside Lab_8_Firewall.

Terminal 1:  python server.py
             Shows: Server is waiting for connection...
Terminal 2:  python client.py

Client shows:
    Connected to server!
    Server: Message received successfully!

A firewall does not filter this test, because 127.0.0.1 stays inside the computer.
A real firewall test needs Part B or Part C. Stop the server before continuing.

PART B - UFW FIREWALL TEST (MAIN EXPERIMENT)
--------------------------------------------
Needs: an Ubuntu SERVER computer with sudo access, an AUTHORISED client, and if possible a
second UNAUTHORISED client. All must be on the same network.

Warning: if you are connected to the server by SSH, first run: sudo ufw allow OpenSSH
Otherwise enabling the firewall can lock you out.

Find the IPs. On each computer run hostname -I (Ubuntu) or ipconfig (Windows).
The examples use server 192.168.1.10 and authorised client 192.168.1.20. Use your real IPs.

Do steps 1 to 7 on the UBUNTU SERVER, in a terminal inside Lab_8_Firewall.

Step 1: Install UFW. First check whether it is already there:
    sudo ufw version

  If it is missing, with internet:
    sudo apt update
    sudo apt install ufw

  If it is missing, without internet:
    sudo apt install ./offline_packages/ufw_0.36.2-6_all.deb

  The offline package needs iptables, ucf and python3, which normal Ubuntu desktops usually have.

Step 2: Check the firewall status
    sudo ufw status
  Possible output: Status: inactive

Step 3: Set the default policies
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
  This blocks incoming connections and allows outgoing connections by default.

Step 4: Enable the firewall (press y if asked)
    sudo ufw enable

Step 5: Check the status
    sudo ufw status verbose
  Example output:
    Status: active
    Default: deny (incoming), allow (outgoing)

Step 6: Allow only the authorised client to reach TCP port 5000
    sudo ufw allow from 192.168.1.20 to any port 5000 proto tcp

Step 7: View the rules and start the server
    sudo ufw status numbered
    python3 server.py

Step 8: On the AUTHORISED client (192.168.1.20), inside Lab_8_Firewall:
    python client.py 192.168.1.10
  Expected:
    Connected to server!
    Server: Message received successfully!

Step 9: On the UNAUTHORISED client (any other IP), inside Lab_8_Firewall:
    python client.py 192.168.1.10
  Expected after 3 seconds:
    Connection timed out! Firewall may be blocking traffic.

  With only one client computer, delete the allow rule instead (sudo ufw status numbered, then
  sudo ufw delete <number>) and run the client again. It should now time out.

Step 10: Clean up on the server. Stop it, then turn the firewall back off:
    sudo ufw status numbered
    sudo ufw delete <number>
    sudo ufw disable

  sudo ufw reset removes all rules, including any that were there before the lab.

PART C - ONLY ONE WINDOWS COMPUTER WITH WSL UBUNTU
--------------------------------------------------
WSL Ubuntu acts as the server and Windows acts as the client.

1. In the Ubuntu (WSL) terminal, go to the lab. Replace the path with your real one:
       cd /mnt/c/Users/<you>/Desktop/Lab_8_Firewall
2. Do Steps 1 to 6 of Part B. In Step 6, use the Windows address that WSL sees:
       ip route show default | awk '{print $3}'
3. Find the WSL IP:
       hostname -I
4. Start the server in WSL:
       python3 server.py
5. In a Windows terminal inside Lab_8_Firewall:
       python client.py <wsl_ip>
6. Delete the allow rule and repeat step 5. It should time out.
7. Clean up as in Step 10.

Real results from this setup (Ubuntu 24.04 in WSL, server 172.28.107.146, Windows 172.28.96.1):

    Rule allows only 192.168.1.20:
        Connection timed out! Firewall may be blocking traffic.

    After: sudo ufw allow from 172.28.96.1 to any port 5000 proto tcp
        Connected to server!
        Server: Message received successfully!

    After deleting that rule:
        Connection timed out! Firewall may be blocking traffic.

Your IP addresses will be different. The WSL addresses can change after a restart, so check them each time.

PART D - WINDOWS DEFENDER FIREWALL INSTEAD OF UFW
-------------------------------------------------
Use this if the server has to be Windows. Open a terminal with Run as administrator.

Allow only the authorised client:
    netsh advfirewall firewall add rule name="Lab 8 Allow" dir=in action=allow protocol=TCP localport=5000 remoteip=192.168.1.20

View it:
    netsh advfirewall firewall show rule name="Lab 8 Allow"

Remove it afterwards:
    netsh advfirewall firewall delete rule name="Lab 8 Allow"

When the Windows Security popup appears for Python, click Cancel, not Allow. Allow can let every
client through, which makes the test meaningless. Windows may also already have a rule allowing
python.exe; if so, an unauthorised client will connect. Check under Windows Defender Firewall >
Allow an app through firewall.

STOP THE SERVER AND FREE THE PORT
---------------------------------
Press Ctrl+C in the server terminal. If it does not stop on Windows, close that terminal window.

Check that port 5000 is free (no output means it is free):
    Windows: netstat -ano | findstr :5000
    Ubuntu : ss -lntup | grep :5000

If something is still using it, stop that process using the PID shown at the end of the line:
    Windows: taskkill /PID <PID> /F
    Ubuntu : kill <PID>

HOW TO READ THE RESULTS
-----------------------
  Connected to server!       The firewall allowed it and the server is running.
  Connection timed out!      The firewall silently dropped it (deny). Or the IP is wrong.
  Connection failed:
    refused / WinError 10061 The computer was reached, but no server is running on port 5000.

NOTES
-----
- UFW rules are operating system commands. Python only tests the connection.
- Do not use 127.0.0.1 for the firewall test.
- UFW exists on Ubuntu only. Windows uses Part D.
- Always disable the test rules when finished, especially on college computers.
