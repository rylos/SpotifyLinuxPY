#!/bin/bash

chmod +x script/english/macosinstall.sh
echo "I proceed to install the packages for patch Spotify"
sleep 1.5
wait
clear
xcode-select --install
sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
echo "Brew and need package successfully installed"
sleep 1.5
wait
clear
echo "Proceed to install Spotify"
sleep 1.5
wait
clear
curl -O https://github.com/KRTirtho/spotube/releases/latest/download/Spotube-macos-universal.dmg
hdiutil attach Spotube-macos-universal.dmg
cp -R /Volumes/Spotube/Spotube.app /Applications/
hdiutil detach /Volumes/Spotube
rm Spotube-macos-universal.dmg
clear
echo "Spotify has been successfully installed."