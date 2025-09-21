# Keylogger

A simple Python keylogger that captures keystrokes and sends them via email at regular intervals.

## Features

- Captures all keyboard input (letters, numbers, special keys)
- Sends logs via Gmail at configurable intervals
- Uses TLS encryption for secure email transmission
- Lightweight and easy to use

## Requirements

- Python 3.x
- Gmail account with 2-Step Verification enabled
- Gmail App Password

## Installation

1. Install required packages:
```bash
pip install pynput
```

2. Clone or download the project files

## Setup

1. Enable 2-Step Verification on your Gmail account
2. Generate an App Password:
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Navigate to "App passwords"
   - Create a new app password for "Mail"
   - Copy the 16-character password

3. Update `run.py` with your credentials:
```python
keylogger = Keylogger.Keylogger(15, "your-email@gmail.com", "your-app-password")
```

## Usage

Run the keylogger:
```bash
python run.py
```

The keylogger will:
- Start capturing keystrokes immediately
- Send the first email report right away
- Continue sending reports every 15 seconds (configurable)

## Configuration

In `run.py`, you can modify:
- **Time interval**: Change `15` to desired seconds between emails
- **Email address**: Your Gmail address
- **App password**: Your Gmail app password

## Files

- `Keylogger.py` - Main keylogger class
- `run.py` - Configuration and execution script

- `README.md` - This documentation
