import socket
import os
import time
import subprocess

spotify_package = ["flatpak", "zip", "unzip", "curl"]
distro_list = ["1. Ubuntu", "2. Fedora", "3. Arch", "4- Void Linux", "5. Gentoo", "6. OpenSUSE", "7. CentOS"]
os_list = ["C. ChromeOS", "m. macOS"]

def check_internet_connection(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as e:
        return False

if check_internet_connection():
    print("I procede to chose the distro")
else:
    time.sleep(0.5)
    os.system('clear')
    print("Connect to wifi and relaunch the script")
    os.system('exit')

print("What distro are you using?")
print(distro_list[0])
print(distro_list[1])
print(distro_list[2])
print(distro_list[3])
print(distro_list[4])
print(distro_list[5])
print(distro_list[6])
print("\nOther OS")
print(os_list[0])
print(os_list[1])

scelta=input()



