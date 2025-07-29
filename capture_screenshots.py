from PIL import ImageGrab
import time
import os

def capture_screen():
    while True:
        time.sleep(10)
        screenshot = ImageGrab.grab()
        screenshot.save(os.path.join("D:/Projects/Keylogger/screenshot", f"screenshot_{int(time.time())}.jpg"))

capture_screen()