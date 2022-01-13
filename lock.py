import os

winpath = os.environ["windir"]
os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation')