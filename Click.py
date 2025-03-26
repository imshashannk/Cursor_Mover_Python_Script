import time
import pyautogui

# Set time interval (in seconds)
INTERVAL = 2  # Adjust as needed

while True:
    # Perform a left mouse click
    pyautogui.click()
    
    # Wait before repeating
    time.sleep(INTERVAL)
