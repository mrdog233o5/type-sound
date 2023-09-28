alias mkdir='mkdir -p'
mkdir $HOME/.config/
mkdir $HOME/.config/type-sound
mkdir $HOME/.config/type-sound/sounds
install ./type-sound.json $HOME/.config/type-sound/type-sound.json
install -d example.pack $HOME/.config/type-sound/sounds
echo "Using sudo to install to /usr/local/bin"
sudo install ./dist/type-sound /usr/local/bin
echo "Using sudo to install to /Applications"
# install -d ./dist/type-sound.app /Applications
sudo cp -r ./dist/type-sound.app /Applications
sudo cp -r ./dist/type-sound.app /Applications
sudo mkdir /opt/user
sudo mkdir /opt/user/bin
sudo cp -r ./dist/type-sound /opt/user/bin
cd ~
echo 'export PATH="/opt/user/bin":$PATH' >> .zshrc
