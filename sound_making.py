from pynput import keyboard
import simpleaudio as sa

press   = sa.WaveObject.from_wave_file("./sounds/0/press.wav")
release = sa.WaveObject.from_wave_file("./sounds/0/release.wav")

sounds = {}

def on_press(key):
    if keyboard.KeyCode.from_char(key) not in sounds:
        sounds[keyboard.KeyCode.from_char(key)] = ""
        press.play()

def on_release(key):
    if keyboard.KeyCode.from_char(key) in sounds:
        del sounds[keyboard.KeyCode.from_char(key)]
        release.play()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
