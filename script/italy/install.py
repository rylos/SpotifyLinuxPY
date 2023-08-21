import os
import time
import subprocess

print("Cosa vuoi fare?")
print("--------------------")
print("1. Installare")
print("2. Aggiornare")
print("\nQ. Uscire")

install_path = os.path.join('script', 'italy', 'package.py')
update_path = os.path.join('script', 'italy', 'update.py')

install = os.path.join(os.getcwd(), install_path)
update = os.path.join(os.getcwd(), update_path)

inp=input()

if inp == "1":
    with open(install, "r") as file:
        script_code = file.read()
    exec(script_code)
elif inp == "2":
    with open(update, "r") as file:
        script_code = file.read()
    exec(script_code)
elif inp == "Q":
    print("Sto uscendo, Addio!")
    time.sleep(0.5)
    os.system('clear')
    exit()
else:
    print("Non è una valida scelta")
    time.sleep(0.5)
    os.system('clear')
    exit()