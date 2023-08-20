#import 
import os
import time
import subprocess

#START SCRIPT
distro_list = ["1. Ubuntu", "2. Fedora", "3. Arch", "4- Void Linux", "5. Gentoo", "6. OpenSUSE", "7. CentOS"]
os_list = ["C. ChromeOS", "m. macOS"]
spotify_package = ["flatpak", "zip", "unzip", "git", "curl"]

#check if wifi is connected
def is_wifi_enabled():
    try:
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print("Error", e)
        return False

def run_flatpak_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr

#define flatpak package
flatpak_repo = ["flatpak", "remote-add", "--if-not-exist", "flathub", "https://flathub.org/repo/flathub.flatpakrepo"]
flatpak_install = ["flatpak", "install", "flathub", "com.spotify.Client"] 

#wifi
print("I procede to check if wifi work")

time.sleep(1.5)
os.system('clear')

if is_wifi_enabled():
    print("Procede to choose the distro or os")
    time.sleep(1.0)
    os.system('clear')
else:
    time.sleep(0.5)
    os.system('clear')
    print('Connect to Wifi and relaunch the script')
    exit()

#install package
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

if scelta == "1":
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "apt-get", "install", program])
    os.system('clear')
    print("Procede to install spotify")
    repo = run_flatpak_command(flatpak_repo)
    install = run_flatpak_command(flatpak_install)
    os.system('clear')
    print("Procede to patch Spotify")
    time.sleep(1.5)
    