import pyautogui
import time

def mouse_wiggler(interval=10, distance=10):
    try:
        print("Mouse wiggler started. Press Ctrl+C to stop.")
        while True:
            x, y = pyautogui.position()  #
            pyautogui.moveTo(x + distance, y) 
            time.sleep(0.5) 
            pyautogui.moveTo(x, y) 
            time.sleep(interval - 0.5) 
    except KeyboardInterrupt:
        print("\nMouse wiggler stopped.")

mouse_wiggler(interval=10, distance=10)
