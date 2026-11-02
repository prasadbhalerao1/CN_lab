EXPERIMENT 2 - SLIDING WINDOW PROTOCOLS (GO-BACK-N AND SELECTIVE REPEAT)
=======================================================================

WHAT THIS LAB DOES
Simulates two sliding window protocols and shows what each one does when a frame is lost.
It prints the steps on screen. It does not send real network packets, so it uses no port,
no server and no internet.

FILES
  sliding_window.py   The program

SETUP (DO THIS ONCE ON EACH COMPUTER)
-------------------------------------
Nothing needs to be installed with pip, and no internet is needed.
You only need Python 3 (tested on 3.12 and 3.14).

1. Copy this Lab_2 folder from the pen drive to the Desktop.

2. Open a terminal inside the folder:
     Windows: open Lab_2 in File Explorer, click the address bar, type cmd, press Enter.
     Ubuntu : open Lab_2 in Files, right-click empty space, choose Open in Terminal.
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
In the terminal inside Lab_2:
    python sliding_window.py

Type these answers when asked (each followed by Enter):
    Enter total number of frames: 6
    Enter window size: 3
    Enter frame number to lose (0 for no loss): 2
    Enter your choice: 3

Choices: 1 = Go-Back-N, 2 = Selective Repeat, 3 = Both.

EXPECTED OUTPUT (FIRST PART)
----------------------------
    --- GO-BACK-N PROTOCOL ---

    Sender Window: 1 to 3
    Sender: Sending Frame 1
    Receiver: Frame 1 received
    Receiver: Cumulative ACK 1
    Sender: Sending Frame 2
    Frame 2 lost!
    Sender: Sending Frame 3
    Receiver: Frame 3 discarded
    Receiver: Duplicate ACK 1

    Timeout occurred!
    Go-Back-N: Retransmitting outstanding frames

The run ends with:
    All frames transmitted successfully using Selective Repeat.

WHAT TO NOTICE
--------------
- Go-Back-N: the receiver throws away every frame after the lost one, so the sender
  resends the lost frame and all frames after it in the window.
- Selective Repeat: the receiver keeps later frames, so only the lost frame is resent.

NOTES
-----
- One chosen frame is lost once per run. Enter 0 for no loss.
- The lost frame number must be between 0 and the total number of frames.
- Run the program again to try different values.
