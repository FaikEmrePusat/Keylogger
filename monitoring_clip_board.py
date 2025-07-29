import pyperclip
import time

def log_clipboard():
    recent_value = ""

    while True:
        time.sleep(5)
        current_value = pyperclip.paste()
        
        if current_value != recent_value:
            recent_value = current_value
            print(f'Clipboard content: {recent_value}')

log_clipboard()
