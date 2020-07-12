## To Install System-Wide
# Run: "install.sh"
This will place the .desktop file in /usr/share/applications, and place the mactrash.py file in /usr/share/mactrash
# Now, create a startup Application:
Activities>Startup Applications>New Startup Application
place this in the title: "MacTrash"
place this in the command box: "python /usr/share/MacTrash/mactrash.py"
Place whatever you want in the desc box.

## To Install Locally:
# Run install-local.sh
Create the startup application as seen above, but with the command box, place "python /home/$USER/.local/share/MacTrash/mactrash.py"


The Empty Trash feature has been finished!  Empty trash now Works!
