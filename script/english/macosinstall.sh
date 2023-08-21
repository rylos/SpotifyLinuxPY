chmod +x script/english/macosinstall.sh
echo "I proceed to install the packages for patch Spotify"
sleep 1.5
wait
clear
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install curl zip unzip git
echo "Brew and need package successfully installed"
sleep 1.5
wait
clear
echo "Proceed to install Spotify"
sleep 1.5
wait
clear
curl -O https://download.scdn.co/Spotify.dmg
hdiutil attach Spotify.dmg
cp -R /Volumes/Spotify/Spotify.app /Applications/
hdiutil detach /Volumes/Spotify
clear
echo "i procede to patch Spotify"
bash <(curl -sSL https://gist.github.com/jetfir3/e8830cf8deba6a4f15eec094d344f7b1/raw/spotx.sh) -Bcd