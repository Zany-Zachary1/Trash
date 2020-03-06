#/bin/bash
echo "Installing MacTrash Locally"
mkdir /home/$USER/.local/MacTrash
mv mactrash.py /home/$USER/.local/MacTrash
mv trashcan.desktop /home/$USER/.local/share/applications
echo "MacTrash has been Installed"
