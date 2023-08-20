import platform
import os
import time
import subprocess

spotify_package = ["flatpak", "zip", "unzip", "curl"]
distro_list = ["1. Ubuntu", "2. Fedora", "3. Arch", "4- Void Linux", "5. Gentoo", "6. OpenSUSE", "7. CentOS"]
os_list = ["C. ChromeOS", "m. macOS"]

def check_internet_connection():
    if platform.system() == "Linux":
        result = subprocess.run(['nmcli', 'radio', 'wifi'], capture_output=True, text=True)
        return "enabled" in result.stdout
    elif platform.system() == "Darwin":
        result = subprocess.run(['networksetup', '-getairportpower', 'Wi-Fi'], capture_output=True, text=True)
        return "On" in result.stdout
    else:
        return False

print("I procede to check if wifi work")

time.sleep(0.5)
os.system('clear')

if not check_internet_connection():
    print("Wi-Fi is turned off. Please turn it on and relaunch the script.")
    exit()

if check_internet_connection():
    print("Wifi is work, I proceed to choose the distro")
else:
    time.sleep(0.5)
    os.system('clear')
    print("Connect to Wi-Fi and relaunch the script")
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