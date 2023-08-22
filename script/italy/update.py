import subprocess

spotify_update_package = "com.github.KRTirtho.Spotube"

update_command = ["flatpak", "update", spotify_update_package]
result = subprocess.run(update_command, capture_output=True, text=True)

if result.returncode == 0:
    print("Pacchetti aggiornati con sucesso.")
else:
    print("L'aggiornamenti del pacchetto hanno generato un'errore.")
    print("Error:", result.stderr)