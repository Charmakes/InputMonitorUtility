# Input Monitor

## Overview

The **Input Monitor** is a Python-based tool that captures and logs keystrokes from the keyboard. It periodically sends the collected data to a specified email address.

## Features

- Captures keystrokes in real time.
- Sends an email with the collected data at a defined interval.
- Configurable interval for sending emails.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Charmakes/KeyCaptureUtility.git
    cd KeyCaptureUtility
    ```

2. **Install dependencies:**

    ```bash
    pip install pynput
    ```

## Configuration

1. **Set up email credentials:**

   - Open `input_monitor.py` in a text editor.
   - Replace the placeholder email and password with your actual email and password (or app password if 2FA is enabled).

     ```python
     if __name__ == "__main__":
         # Replace with your email and app password
         monitor = InputMonitor(60, 'your_email@example.com', 'your_app_password_here')
         monitor.start()
     ```

2. **Set the interval:**

   You can change this value in the `InputMonitor` class initialization.

     ```python
     monitor = InputMonitor(60, 'your_email@example.com', 'your_app_password_here')
     ```

## Running the Program

1. **Execute the script:**

    ```bash
    python input_monitor.py
    ```

2. **Check terminal output:**

![image](https://github.com/user-attachments/assets/542b2375-e128-4095-a10c-0061dcd8c021)


    Terminal output should indicate that the program has started and will log keystrokes.

3. **Verify email receipt:**

    - After running the script for the interval, check the specified email account for the report.

    ![image](https://github.com/user-attachments/assets/f4167814-d58f-4c9b-8158-02867dfdb02f)



    The email should contain the keystroke logs.

## Troubleshooting

- **SMTP Authentication Error:**
  - Ensure that you are using the correct email and password.
  - If using an Outlook account with Two-Factor Authentication, generate and use an app password.
  - Verify that the SMTP server settings are correct.

- **Keylogging Errors:**
  - Ensure that the `pynput` library is installed and correctly imported.

## Security and Privacy

- This tool is intended for educational purposes. Do not use it to capture keystrokes without proper authorization.
- Ensure that you comply with all relevant laws and regulations regarding privacy and data security.


