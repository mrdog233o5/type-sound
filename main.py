#!/usr/bin/env python3
import simpleaudio as sa
import pathlib
import os
from pynput import keyboard,mouse
from os import system as osys

contri = " & ".join(["William Chen","Jerry Lam"])
osys("clear")
print(f"""
████████╗██╗░░░██╗██████╗░███████╗░░░░░░░██████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░
╚══██╔══╝╚██╗░██╔╝██╔══██╗██╔════╝░░░░░░██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗
░░░██║░░░░╚████╔╝░██████╔╝█████╗░░█████╗╚█████╗░██║░░██║██║░░░██║██╔██╗██║██║░░██║
░░░██║░░░░░╚██╔╝░░██╔═══╝░██╔══╝░░╚════╝░╚═══██╗██║░░██║██║░░░██║██║╚████║██║░░██║
░░░██║░░░░░░██║░░░██║░░░░░███████╗░░░░░░██████╔╝╚█████╔╝╚██████╔╝██║░╚███║██████╔╝
░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░╚══════╝░░░░░░╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░

made by {contri}""")

try:
    localaddr = os.path.expanduser('~')+"/.config/type-sound"
    configFile = open(f"{localaddr}/type-sound.json", "r").read()
    soundPack = eval(configFile)["pack"]
except:
    print(">>> ERROR - config file error, read the manual (https://github.com/mrdog233o5/type-sound)")
    exit(1)

try:
    press = sa.WaveObject.from_wave_file(f"{localaddr}/sounds/{soundPack}/press.wav")
    release = sa.WaveObject.from_wave_file(f"{localaddr}/sounds/{soundPack}/release.wav")
    mousePress = sa.WaveObject.from_wave_file(f"{localaddr}/sounds/{soundPack}/mousePress.wav")
    mouseRelease = sa.WaveObject.from_wave_file(f"{localaddr}/sounds/{soundPack}/mouseRelease.wav")
except:
    print(">>> ERROR - sound pack issue, read the manual (https://github.com/mrdog233o5/type-sound)")
    exit(1)

sounds = {}
is_mouse_pressed = False

print(f"""
pack selected: {soundPack}
""")

def on_press(key):
    if keyboard.KeyCode.from_char(key) not in sounds:
        sounds[keyboard.KeyCode.from_char(key)] = ""
        press.play()

def on_release(key):
    if keyboard.KeyCode.from_char(key) in sounds:
        del sounds[keyboard.KeyCode.from_char(key)]
        release.play()

def on_click(x, y, button, pressed):
    global is_mouse_pressed
    if pressed:
        is_mouse_pressed = True
        mousePress.play()
    else:
        if is_mouse_pressed:
            is_mouse_pressed = False
            mouseRelease.play()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as keyboard_listener:
    with mouse.Listener(on_click=on_click) as mouse_listener:
        keyboard_listener.join()
        mouse_listener.join()
