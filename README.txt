COMPUTER NETWORKS LAB PROGRAMS - EXPERIMENTS 2 TO 9
===================================================

Each Lab_N folder works on its own. Copy just that folder to another computer and follow its
README.txt, which has every step and command from scratch.

  Lab                      Topic                                   Needs server?   Port
  Lab_2_Sliding_Window     Go-Back-N and Selective Repeat          No              None
  Lab_3_CRC                CRC error detection                     No              None
  Lab_4_DNS                DNS lookup                              No              None
  Lab_5_UDP_File_Transfer  UDP file transfer                       Yes             UDP 5000
  Lab_6_TCP_Sockets        TCP Hello, file transfer, calculator    Yes             TCP 5000, 5001, 5002
  Lab_7_TLS                TLS secure communication                Yes             TCP 8443
  Lab_8_Firewall           Firewall configuration and TCP test     Yes             TCP 5000
  Lab_9_Web_Server         Web server and HTTP client              Yes             TCP 8000

REQUIREMENTS
- Python 3 only. All programs use the standard library, so there is no pip install step.
- Included already: demo files (Labs 5, 6, 9), TLS certificate (Lab 7), offline UFW package (Lab 8).
- Offline_Setup holds the official Python 3.12.10 Windows installer, for computers without Python.

RULES THAT APPLY TO EVERY LAB
- Run one lab at a time. Stop each server before starting the next.
- Start the server before the client.
- On Windows type python. On Ubuntu type python3.
- Servers listen on 0.0.0.0, so they work on any computer with no IP edits.
- Clients use 127.0.0.1 (same computer) by default. For two computers, give the server's IP:
      python client.py 192.168.1.35
