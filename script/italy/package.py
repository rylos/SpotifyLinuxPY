import os
import time
import subprocess

#START SCRIPT
distro_list = ["1. Ubuntu", "2. Fedora", "3. Arch", "4- Void Linux", "5. Gentoo", "6. OpenSUSE", "7. CentOS"]
os_list = ["C. ChromeOS", "m. macOS"]
spotify_package = ["flatpak", "zip", "unzip", "git", "curl"]
void_package = ["flatpak", "zip", "unzip", "git", "curl", "xdg-desktop-portal-gtk", "xdg-desktop-portal"]
gentoo_package = ["net-misc/curl", "app-arch/zip", "app-arch/unzip", "dev-vcs/git"]
flatpak_package = "com.github.KRTirtho.Spotube"
flatpak_remote = "flathub"
macos_patch_install = 'script/italy/macosinstall.sh'

#CHECK WIFI 
def is_wifi_enabled():
    try:
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print("Error", e)
        return False
    
def run_flatpak_command(command):
    # Implementation of the function
    pass

install_command = ["flatpak", "install", flatpak_remote, flatpak_package]

#WIFI
os.system('clear')
print("Procedo a vedere se il Wifi funziona")

time.sleep(1.5)
os.system('clear')

if is_wifi_enabled():
    print("Procedo a far scegliere la distro o l'os")
    time.sleep(1.0)
    os.system('clear')
else:
    time.sleep(0.5)
    os.system('clear')
    print('Connetti il wifi e riavvia lo script')
    exit()

#INSTALL PACKAGE
print("Che distro stai usando?")
print(distro_list[0])
print(distro_list[1])
print(distro_list[2])
print(distro_list[3])
print(distro_list[4])
print(distro_list[5])
print(distro_list[6])
print("\nAltri OS")
print(os_list[0])
print(os_list[1])

scelta=input()

if scelta == "1":
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "apt-get", "install", program])
    os.system('clear')
    print("Procedo a installare Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} installato con successo.")
    time.sleep(1.5)
    os.system('clear')
    exit()
elif scelta == "2":
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "dnf", "install", "-y", program])
    os.system('clear')
    print("Procedo a installare Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} installato con successo.")
    time.sleep(1.5)
    os.system('clear')
    exit()
elif scelta == "3":
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "pacman", "-Sy", "--noconfirm", program])
    os.system('clear')
    print("Procedo a installare Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} installato con successo.")
    time.sleep(1.5)
    os.system('clear')
    exit()
elif scelta == "4":
    os.system('clear')
    for program in void_package:
        subprocess.call(["sudo", "xbps-install", "-y", program])
    os.system('clear')
    print("Procedo a installare Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} installato con successo.")
    time.sleep(1.5)
    os.system('clear')
    exit()
elif scelta == "5":
    os.system('clear')
    for program in gentoo_package:
        subprocess.call(["sudo", "emerge", "--ask=n", program])
    os.system('clear')
    print("Procedo a installare Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} installato con successo.")
    time.sleep(1.5)
    os.system('clear')
    exit()
elif scelta == "6":
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "zypper", "--non-interactive", "install", program])
    os.system('clear')
    print("Procedo a installare Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} installato con successo.")
    time.sleep(1.5)
    os.system('clear')
    exit()
elif scelta == "7":
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "yum", "install", "-y", program])
    os.system('clear')
    print("Procedo a installare Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} installato con successo.")
    time.sleep(1.5)
    os.system('clear')
    exit()
elif scelta == "m":
    os.system('clear')
    subprocess.run(['bash', macos_patch_install], check=True)
elif scelta == "C":
    os.system('clear')
    for program in spotify_package:
        subprocess.call(["sudo", "apt-get", "install", program])
    os.system('clear')
    print("Procedo a installare Spotify")
    subprocess.run(install_command, check=True)
    print(f"{flatpak_package} installato con successo.")
    time.sleep(1.5)
    os.system('clear')
    exit()