#IMPORT 
import os
import time
import subprocess

#START SCRIPT
distro_list = ["1. Ubuntu", "2. Fedora", "3. Arch", "4- Void Linux", "5. Gentoo", "6. OpenSUSE", "7. CentOS"]
os_list = ["C. ChromeOS", "m. macOS"]

need_package = ["flatpak", "zip", "unzip", "git", "curl"]
void_package = ["flatpak", "zip", "unzip", "git", "curl", "xdg-desktop-portal-gtk", "xdg-desktop-portal"]
gentoo_package = ["net-misc/curl", "app-arch/zip", "app-arch/unzip", "dev-vcs/git"]


flatpak_package = "com.github.KRTirtho.Spotube"
spotify_package = "com.spotify.Client"
flatpak_remote = "flathub"

macos_patch_install = ''
linux_path = 'script/patch/linux.sh'

#CHECK WIFI 
def is_wifi_enabled():
    try:
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print("Error", e)
        return False

#DEFINI FLATPAK PACKAGE

def run_flatpak_command(command):
    # Implementation of the function
    pass

spotify_command = ["flatpak", "install", flatpak_remote, flatpak_package]


#WIFI
os.system('clear')
print("Proceeding to check if Wifi/internet connection is working")

time.sleep(1.5)
os.system('clear')

if is_wifi_enabled():
    print("Procede to choose a distro or an os")
    time.sleep(1.0)
    os.system('clear')
else:
    time.sleep(0.5)
    os.system('clear')
    print('Connect to Wifi and relaunch the script')
    exit()

#INSTALL PACKAGE
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

