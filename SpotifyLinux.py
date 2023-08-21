import os
import time

installen = os.path.join('script', 'english', 'install.py')
installit = os.path.join('script', 'italy', 'install.py')

installeng = os.path.join(os.getcwd(), installen)
installita = os.path.join(os.getcwd(), installit)

print("Script made by @sayoridev")

print("  ʕ•ᴥ•ʔ")
print(" (      )")
print(" /|____|\\")

time.sleep(1.5)

os.system('clear')
print("What language do you want to use?")
print("---------------------------------")
print("1. English")
print("2. Italy")
print("3. Quit")

risp = input()

if risp == "1":
    os.system('clear')
    with open(installeng, "r") as file:
        script_code = file.read()
    exec(script_code)
elif risp == "2":
    os.system('clear')
    with open(installita, "r") as file:
        script_code = file.read()
    exec(script_code)
else:
    quit()
