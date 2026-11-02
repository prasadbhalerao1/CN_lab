EXPERIMENT 3 - CRC ERROR DETECTION (7-BIT / 8-BIT ASCII)
=======================================================

WHAT THIS LAB DOES
Converts a message to 7-bit or 8-bit ASCII, calculates a CRC, flips one bit to simulate an
error, detects the error and simulates retransmission. It uses no port, no server and no internet.

FILES
  crc.py   The program

SETUP (DO THIS ONCE ON EACH COMPUTER)
-------------------------------------
Nothing needs to be installed with pip, and no internet is needed.
You only need Python 3 (tested on 3.12 and 3.14).

1. Copy this Lab_3_CRC folder from the pen drive to the Desktop.

2. Open a terminal inside the folder:
     Windows: open Lab_3_CRC in File Explorer, click the address bar, type cmd, press Enter.
     Ubuntu : open Lab_3_CRC in Files, right-click empty space, choose Open in Terminal.
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
In the terminal inside Lab_3_CRC:
    python crc.py

Type these answers when asked (each followed by Enter):
    Enter message: Hi
    Enter ASCII size (7 or 8): 8
    Enter generator: 1101
    Enter error position (0 for no error): 5

EXPECTED OUTPUT
---------------
    Binary Data: 0100100001101001
    CRC Remainder: 001
    Transmitted Codeword: 0100100001101001001
    Received Data: 0100000001101001001
    Receiver Remainder: 001
    Error Detected!
    Retransmitting...
    Retransmitted Data: 0100100001101001001
    Error Corrected Successfully!

To see the no-error case, run it again and enter 0 for the error position:
    No Error Detected!

NOTES
-----
- Use a valid generator such as 1101: only 0 and 1, starting and ending with 1. The program
  does not check this, so a bad generator gives an error or a wrong result.
- Error position 1 is the leftmost bit of the codeword. A position past the end flips nothing,
  so it behaves like 0.
- A remainder of all zeros means no error was detected.
- CRC only detects errors. The program fixes the data by retransmitting the original
  codeword; CRC itself does not correct the bit.
- Use normal English characters. The program does not check for characters outside ASCII.
