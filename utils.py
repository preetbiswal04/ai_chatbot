import pyautogui
import time

def copy_past():
    time.sleep(2)

    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    pyautogui.hotkey("ctrl", "v")

    time.sleep(1)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    pyautogui.hotkey("ctrl", "v")

    print("Copy paste completed.")