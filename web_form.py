import pyautogui
import time 

pyautogui.FAILSAFE = True

def fill_web_form():
    time.sleep(5)

    pyautogui.hotkey("win","r")
    time.sleep(1)
    pyautogui.write("chrome")
    pyautogui.press("Enter")
    time.sleep(5)

    pyautogui.write("https://example.com/login") # Placeholder URL, user should update
    pyautogui.press("enter")
    time.sleep(5)

    # Coordinates (500,400) are screen specific, user might need to adjust
    pyautogui.click(500,400)
    pyautogui.write("my_username")

    pyautogui.click(500,450)
    pyautogui.write("my_password")

    print("web form fill sucessful")
