import os
import time
import subprocess

print("What do you want to do?")
print("--------------------")
print("1. Install")
print("2. Update")
print("\nQ. Exit")

install_path = os.path.join('script', 'english', 'package.py')
update_path = os.path.join('script', 'english', 'update.py')

install = os.path.join(os.getcwd(), install_path)
update = os.path.join(os.getcwd(), update_path)

inp = input()

if inp == "1":
    with open(install, "r") as file:
        script_code = file.read()
    exec(script_code)
elif inp == "2":
    with open(update, "r") as file:
        script_code = file.read()
    exec(script_code)
elif inp == "Q":
    print("Exiting, Goodbye!")
    time.sleep(0.5)
    os.system('clear')
    exit()
else:
    print("Is not a valid choice")
    time.sleep(0.5)
    os.system('clear')
    exit()
