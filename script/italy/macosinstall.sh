#!/bin/bash

chmod +x script/italy/macosinstall.sh
echo "Procedo a installare i paccheti e a patchare spotify"
sleep 1.5
wait
clear
xcode-select --install
sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
echo "Brew e i pacchetti necessare sono stati installati con successo"
sleep 1.5
wait
clear
echo "Procedo a installare Spotify"
sleep 1.5
wait
clear
curl -O https://download.scdn.co/Spotify.dmg
hdiutil
cp -R /Volumes/Spotify/Spotify.app /Applications/
hdiutil detach /Volumes/Spotify
clear
echo "Procedo a patchare Spotify"
curl -sSL https://gist.github.com/jetfir3/e8830cf8deba6a4f15eec094d344f7b1/raw/spotx.sh > spotx.sh
bash spotx.sh -Bcd
rm spotx.sh
