import simpleaudio as sa
import pathlib
import os
from pynput import keyboard,mouse
from os import system as osys

osys("clear")
print(f"""
████████╗██╗░░░██╗██████╗░███████╗░░░░░░░██████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░
╚══██╔══╝╚██╗░██╔╝██╔══██╗██╔════╝░░░░░░██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗
░░░██║░░░░╚████╔╝░██████╔╝█████╗░░█████╗╚█████╗░██║░░██║██║░░░██║██╔██╗██║██║░░██║
░░░██║░░░░░╚██╔╝░░██╔═══╝░██╔══╝░░╚════╝░╚═══██╗██║░░██║██║░░░██║██║╚████║██║░░██║
░░░██║░░░░░░██║░░░██║░░░░░███████╗░░░░░░██████╔╝╚█████╔╝╚██████╔╝██║░╚███║██████╔╝
░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░╚══════╝░░░░░░╚═════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░

made by William Chen""")

try:
    localaddr = os.path.expanduser('~')+"/.config/type-sound"
    configFile = open(f"{localaddr}/type-sound.json", "r").read()
    soundPack = eval(configFile)["pack"]
except:
    print(">>> ERROR - config file error, read the manual (https://github.com/mrdog233o5/type-sound)")
    exit()

try:
    press = sa.WaveObject.from_wave_file(f"{localaddr}/sounds/{soundPack}/press.wav")
    release = sa.WaveObject.from_wave_file(f"{localaddr}/sounds/{soundPack}/release.wav")
    mousePress = sa.WaveObject.from_wave_file(f"{localaddr}/sounds/{soundPack}/mousePress.wav")
    mouseRelease = sa.WaveObject.from_wave_file(f"{localaddr}/sounds/{soundPack}/mouseRelease.wav")
except:
    print(">>> ERROR - sound pack issue, read the manual (https://github.com/mrdog233o5/type-sound)")
    exit()

sounds = {}

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
    if button == mouse.Button.left:
        if pressed:
            is_mouse_pressed = True
            press.play()
        else:
            if is_mouse_pressed:
                is_mouse_pressed = False
                release.play()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as keyboard_listener:
    with mouse.Listener(on_click=on_click) as mouse_listener:
        keyboard_listener.join()
        mouse_listener.join()
