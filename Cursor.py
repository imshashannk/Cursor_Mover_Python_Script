import time
import pyautogui

# Set time interval (in seconds)
INTERVAL = 60  # Change this to customize the movement interval

while True:
    x, y = pyautogui.position()  # Get current cursor position
    pyautogui.moveTo(x + 1, y)   # Move cursor slightly
    pyautogui.moveTo(x, y)       # Move back to original position
    time.sleep(INTERVAL)         # Wait before next move
