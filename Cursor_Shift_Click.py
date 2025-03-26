import time
import pyautogui

# Set time interval (in seconds)
INTERVAL = 2  # Adjust as needed

while True:
    # Press Shift key to prevent screen lock
    pyautogui.press('shift')
    
    # Get current cursor position
    x, y = pyautogui.position()
    
    # Move cursor slightly
    pyautogui.moveTo(x + 20, y)  
    pyautogui.moveTo(x, y)  
    
    # Perform a left mouse click
    pyautogui.click()
    
    # Wait before repeating
    time.sleep(INTERVAL)
