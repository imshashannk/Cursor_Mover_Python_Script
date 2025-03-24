# Keep Screen Awake

## Overview
This Python script prevents your computer from going to sleep by periodically moving the cursor. It simulates minimal user activity, ensuring that the screen remains on without interfering with your workflow.

## Features
- 🖱️ **Prevents Screen Lock/Sleep** – Ensures your computer stays active.
- ⏳ **Customizable Interval** – Set the movement frequency as per your preference.
- 🖥️ **Lightweight & Non-Disruptive** – Minimal cursor movement to avoid workflow interruptions.
- 🔄 **Runs in Background** – Can be executed as a background process.

## Requirements
- Python 3.x
- `pyautogui` module (install if not available)

## Installation
1. Clone or download this repository.
2. Install the required dependency:
   ```bash
   pip install pyautogui
   ```

## Usage
1. Open a terminal or command prompt.
2. Run the script:
   ```bash
   python keep_awake.py
   ```
3. The script will move the cursor slightly every 60 seconds (default interval). You can modify the `INTERVAL` variable in the script to change this duration.

## Customization
To change the interval time, edit this line in `keep_awake.py`:
```python
INTERVAL = 60  # Change this value (in seconds)
```

## Stop the Script
To stop the script, simply close the terminal or press **Ctrl + C**.

## License
This script is open-source and free to use.

---

Keep your screen awake without touching the mouse! 🚀

