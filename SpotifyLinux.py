import os
import subprocess
import time

#determino la path degli script python
relative_path_english = os.path.join('script', 'english', 'install.py')
relative_path_italy = os.path.join('script', 'italy', 'install.py')

#Ottieni la path assoluta per gli script
english = os.path.join(os.getcwd(), relative_path_english)
italy = os.path.join(os.getcwd(), relative_path_italy)

print("Script made by @sayoridev")

print("  ʕ•ᴥ•ʔ")
print(" (      )")
print(" /|____|\\")

time.sleep(1.5)

os.system('clear')

print("Quale lingua vuoi che venga utilizzata?")
print("---------------------------------------")
print("1. English")
print("2. Italy")
print("3. Exit")

lingua=input()

if lingua == "1":
    with open(english, "r") as file:
        script_code = file.read()
    exec(script_code)
elif lingua == "2":
    with open(italy, "r") as file:
        script_code = file.read()
    exec(script_code)
else:
    os.system('exit')