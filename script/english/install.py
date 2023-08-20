import os 
import time
import subprocess

print("What do you want do?")
print("--------------------")
print("1. Install")
print("2. Update")
print("\nQ. Exit")

inp=input()

if inp == "1":
    package_path = 'script/english/package.sh'
    subprocess.run(['bash', package_path], check=True)
elif inp == "2":
    update_path = 'script/english/update.sh'
    subprocess.run(['bash', update_path], check=True)
elif inp == "Q":
    print("Exiting, Goodbye!")
    time.sleep(0.5)
    os.system('clear')
    os.system('exit')
else:
    print("Is not a valid choise")
    time.sleep(0.5)
    os.system('clear')
    os.system('exit')