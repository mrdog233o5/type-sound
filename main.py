import subprocess
import os
import tkinter as tk
from os import system as osys

soundPlayer = os.fork()

localaddr = subprocess.run("pwd", capture_output=True, text=True).stdout.strip()
osys(f"chmod 555 {localaddr}/dist/sound_making")
subprocess.Popen([f"{localaddr}/dist/sound_making"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
while 1:
    pass
