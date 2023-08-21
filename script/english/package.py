#IMPORT 
import os
import time
import subprocess
import sqlite3

#START SCRIPT
distro_list = ["1. Ubuntu", "2. Fedora", "3. Arch", "4- Void Linux", "5. Gentoo", "6. OpenSUSE", "7. CentOS"]
os_list = ["C. ChromeOS", "m. macOS"]
spotify_package = ["flatpak", "zip", "unzip", "git", "curl"]
void_package = ["flatpak", "zip", "unzip", "git", "curl", "xdg-desktop-portal-gtk", "xdg-desktop-portal"]
gentoo_package = ["net-misc/curl", "app-arch/zip", "app-arch/unzip", "dev-vcs/git"]
flatpak_package = "com.spotify.Client"
flatpak_remote = "flathub"
macos_patch_install = 'script/english/macosinstall.sh'

#PATCH SCRIPT
ubuntu_script = os.path.join('script', 'patch', 'ubuntu.sh')
otherpathscript = os.path.join('script', 'patch', 'otherdistro.sh')

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

install_command = ["flatpak", "install", flatpak_remote, flatpak_package]

#WIFI
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

if scelta == "1":
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "apt-get", "install", program])
    os.system('clear')
    print("Procede to install Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} install successfully.")
    time.sleep(1.5)
    os.system('clear')
    print("Procede to patch Spotify")
    time.sleep(1.5)
    os.system('clear')
    subprocess.run(['bash', ubuntu_script])
elif scelta == "2":
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "dnf", "install", "-y", program])
    os.system('clear')
    print("Procede to install Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} install successfully.")
    time.sleep(1.5)
    os.system('clear')
    print("Procede to patch Spotify")
    time.sleep(1.5)
    os.system('clear')
    subprocess.run(['bash', otherpathscript])
elif scelta == 3:
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "pacman", "-Sy", "--noconfirm", program])
    os.system('clear')
    print("Procede to install Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} install successfully.")
    time.sleep(1.5)
    os.system('clear')
    print("Procede to patch Spotify")
    time.sleep(1.5)
    os.system('clear')
    subprocess.run(['bash', otherpathscript])
elif scelta == 4:
    os.system('clear')
    for program in void_package:
        subprocess.call(["sudo", "xbps-install", "-y", program])
    os.system('clear')
    print("Procede to install Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} install successfully.")
    time.sleep(1.5)
    os.system('clear')
    print("Procede to patch Spotify")
    time.sleep(1.5)
    os.system('clear')
    subprocess.run(['bash', otherpathscript])
elif scelta == 5:
    os.system('clear')
    for program in gentoo_package:
        subprocess.call(["sudo", "emerge", "--ask=n", program])
    os.system('clear')
    print("Procede to install Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} install successfully.")
    time.sleep(1.5)
    os.system('clear')
    print("Procede to patch Spotify")
    time.sleep(1.5)
    os.system('clear')
    subprocess.run(['bash', otherpathscript])
elif scelta == 6:
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "zypper", "--non-interactive", "install", program])
    os.system('clear')
    print("Procede to install Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} install successfully.")
    time.sleep(1.5)
    os.system('clear')
    print("Procede to patch Spotify")
    time.sleep(1.5)
    os.system('clear')
    subprocess.run(['bash', otherpathscript])
elif scelta == 7:
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "yum", "install", "-y", program])
    os.system('clear')
    print("Procede to install Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} install successfully.")
    time.sleep(1.5)
    os.system('clear')
    print("Procede to patch Spotify")
    time.sleep(1.5)
    os.system('clear')
    subprocess.run(['bash', otherpathscript])
elif scelta == "m":
    os.system('clear')
    subprocess.run(['bash', macos_patch_install], check=True)
elif scelta == "C":
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "apt-get", "install", program])
    os.system('clear')
    print("Procede to install Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} install successfully.")
    time.sleep(1.5)
    os.system('clear')
    print("Procede to patch Spotify")
    time.sleep(1.5)
    os.system('clear')
    subprocess.run(['bash', ubuntu_script])