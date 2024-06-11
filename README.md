# Silent Keylogger for Windows

A Python keylogger that runs silently in the background on Windows using a .pyw script and a batch file.

## Introduction

This project is an enhanced and more refined version of my previous keylogger project. It is designed to run in the background silently, capturing and logging keyboard events to a text file. The keylogger uses the `pynput` library to listen to keyboard events and the `logging` module to record the events in a file.

## Requirements

- Python 3.x
- `pynput` library (install with `pip install pynput`)

## Installation

To use this keylogger, you need to have Python installed on your system. Follow the instructions below to set up the project:

1. **Clone this repository**

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
   *Using a virtual environment ensures that your project's dependencies are isolated from other projects and system-wide packages, which helps avoid potential conflicts.*

3. **Install the required dependencies:**
   ```sh
   pip install pynput
   ```

## Usage

To run the keylogger script silently in the background, double-click the batch file:

```sh
start_keylogger.bat
```

The script will start listening for keyboard events and log them to a file named `keylog.txt`.

### Stopping the Keylogger

To stop the keylogger script, you can use the provided batch file:

1. Double-click `stop_and_clean_keyloggr.bat` to terminate the keylogger process and delete the log file.

Alternatively, you can manually stop the keylogger using the Task Manager:

1. Press `Ctrl + Shift + Esc` to open the Task Manager.
2. Find `pythonw.exe` in the list of processes.
3. Right-click on `pythonw.exe` and select `End Task`.

## Files

- `keylogger.pyw`: The main keylogger script.
- `start_keylogger.bat`: Batch file to start the keylogger silently in the background.
- `stop_and_clean_keyloggr.bat`: Batch file to stop the keylogger and delete the log file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
