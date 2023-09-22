import pyfiglet
import socket
import threading
from colorama import Fore
from datetime import datetime
import subprocess

result=pyfiglet.figlet_format("PORT SCANNER", font="standard")
print(result)

print("-"*70)

print(Fore.YELLOW+"""
     ,-~~-.___.      
    / |  x     \ 
    (  )        0       
    \_/-, ,----'  ____  
        ====      ||   \_ 
       /  \-'~;   ||     |                 v.1.0.0
      /  __/~| ...||__/|-"            PORT SCANNER TOOL
    =(  _____||________|                ~@Coder_Chintu~
   
    
""")

print(Fore.BLUE+"-"* 70)
print(Fore.BLUE+"-"* 70)

host=socket.gethostbyname(input("[+] Enter target domain: ",))
start_port=int(input("[+] Enter Start port: "))
end_port=int(input("[+] Enter End port: "))

print("-" * 50)
print("Scanning Target: " + host)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

def scan(port):
    s=socket.socket()
    s.settimeout(3)
    result=s.connect_ex((host,port,))
    if result ==0:
        print("Port {} is open".format(port,))
    s.close()

for i in range(start_port,end_port+1):
    t=threading.Thread(target=scan,args=(i,))
    t.start()
