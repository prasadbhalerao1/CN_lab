EXPERIMENT 5 - UDP FILE TRANSFER (SCRIPT, TEXT, AUDIO AND VIDEO)
===============================================================

WHAT THIS LAB DOES
Sends four files from a client to a server over UDP. UDP has no delivery guarantee, so the
program adds sequence numbers, acknowledgements and retransmission (stop-and-wait).

PORT: UDP 5000

FILES
  server.py      Receiver. Saves files in received_files\ (created automatically)
  client.py      Sender
  demo_files\    Ready-made files to send:
                   sample_script.py, sample_text.txt, sample_audio.wav, sample_video.mp4

SETUP (DO THIS ONCE ON EACH COMPUTER)
-------------------------------------
Nothing needs to be installed with pip, and no internet is needed.
You only need Python 3 (tested on 3.12 and 3.14).

1. Copy this Lab_5_UDP_File_Transfer folder from the pen drive to the Desktop.

2. Open a terminal inside the folder:
     Windows: open Lab_5_UDP_File_Transfer in File Explorer, click the address bar, type cmd, press Enter.
     Ubuntu : open Lab_5_UDP_File_Transfer in Files, right-click empty space, choose Open in Terminal.
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
You need two terminals, both inside Lab_5_UDP_File_Transfer.

Terminal 1 - start the server first:
    python server.py

    It shows: UDP Server is waiting for files...
    Leave this terminal running.

Terminal 2 - run the client:
    python client.py

Type these four paths when asked:
    Enter script file path: demo_files/sample_script.py
    Enter text file path: demo_files/sample_text.txt
    Enter audio file path: demo_files/sample_audio.wav
    Enter video file path: demo_files/sample_video.mp4

EXPECTED OUTPUT
---------------
Client ends with:
    All four files transferred successfully!

Server shows for each file:
    Receiving: sample_script.py
    File received successfully: sample_script.py
    Saved inside: received_files

CHECK THE RESULT
----------------
Open the received_files folder. Play sample_audio.wav (3 second tone) and sample_video.mp4
(3 second test pattern), or compare a file with the original:
    Windows: fc /b demo_files\sample_video.mp4 received_files\sample_video.mp4
    Ubuntu : cmp demo_files/sample_video.mp4 received_files/sample_video.mp4

Windows prints "no differences encountered". Ubuntu prints nothing when the files match.

TWO COMPUTERS
-------------
The server listens on 0.0.0.0, so it accepts connections on every network address of
any computer. You never need to edit an IP address in the code. Do not type 0.0.0.0
as the client's address; give the client the server computer's real IP instead.

1. Connect both computers to the same network.

2. On the SERVER computer, find its IP address:
     Windows: ipconfig        (read the IPv4 Address line)
     Ubuntu : hostname -I

3. Allow UDP port 5000 on the SERVER computer if its firewall is on:
     Windows: click Allow if a Windows Security popup appears. Or, in a terminal opened
              with Run as administrator:
              netsh advfirewall firewall add rule name="Lab UDP 5000" dir=in action=allow protocol=UDP localport=5000
              Remove it afterwards:
              netsh advfirewall firewall delete rule name="Lab UDP 5000"
     Ubuntu : sudo ufw allow 5000/udp

4. Start the server on the SERVER computer as usual.

5. On the CLIENT computer, add the server's IP to the client command. Example:
     python client.py 192.168.1.35

If it fails, run this on the client first: ping <server_ip>
No reply usually means the network or firewall blocks the computers (college Wi-Fi often does).

STOP THE SERVER AND FREE THE PORT
---------------------------------
Press Ctrl+C in the server terminal. If it does not stop on Windows, close that terminal window.

Check that port 5000 is free (no output means it is free):
    Windows: netstat -ano | findstr :5000
    Ubuntu : ss -lntup | grep :5000

If something is still using it, stop that process using the PID shown at the end of the line:
    Windows: taskkill /PID <PID> /F
    Ubuntu : kill <PID>

NOTES
-----
- The server keeps running after a transfer, so you can run the client again.
- Received files with the same name are overwritten.
- If a client is stopped halfway through a file, restart the server before trying again.
- You can send your own files by typing their paths instead.
- "Server not responding!" means the server is not running or the IP or firewall is wrong.
- Port 5000 is also used by Lab 6 (Hello) and Lab 8, but those use TCP. Even so, run one
  lab at a time and stop each server before starting the next.
