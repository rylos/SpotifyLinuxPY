#!/bin/bash

chmod +x script/english/macosinstall.sh
echo "Procedo a installare Spotify"
sleep 1.5
wait
clear
curl -O https://github.com/KRTirtho/spotube/releases/latest/download/Spotube-macos-universal.dmg
hdiutil attach Spotube-macos-universal.dmg
cp -R /Volumes/Spotube/Spotube.app /Applications/
hdiutil detach /Volumes/Spotube
rm Spotube-macos-universal.dmg
clear
echo "Spotify è stato installato con successo."