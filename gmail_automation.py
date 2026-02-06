import pyautogui
import time
import pandas as pd
import subprocess

def send_email_automation():
    pyautogui.FAILSAFE = True
    excel_path = r"c:\Users\preet\Downloads\rpa_automation_with_python\marks_report.xlsx"
    
    try:
        df = pd.read_excel(excel_path)
        email_body = df.to_string(index=False)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    pyautogui.hotkey("win", "r")
    time.sleep(1)
    cmd = r'chrome --user-data-dir="C:\ChromeRPAProfile"'
    pyautogui.write(cmd)
    pyautogui.press("enter")
    
    print("Waiting for Chrome to open (Custom Profile)...")
    time.sleep(5) 

    print("Navigating directly to Gmail Compose...")
    pyautogui.write("https://mail.google.com/mail/u/0/#inbox?compose=new")
    pyautogui.press("enter")
    print("Waiting for Gmail to load and Compose window to appear...")
    time.sleep(12) 

    print("Assuming Compose window is open...")
    time.sleep(2)

    pyautogui.write("preetbiswal04@gmail.com")
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
        
    pyautogui.write("Automated Report") 
    pyautogui.press("tab")
    pyautogui.write("Hello, this is an automated message.")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write(
        "Hi,\n\nPlease find below the Excel report data:\n\n",
        interval=0.03
    )

    pyautogui.write(email_body, interval=0.01)

    pyautogui.write("\n\nRegards,\nRPA Bot")

    print("Attaching file using Copy-Paste method (No image needed)...")
    
    
    subprocess.Popen(f'explorer /select,"{excel_path}"')
    time.sleep(3) 
    
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)
    
    pyautogui.hotkey("alt", "f4")
    time.sleep(1)
    
    pyautogui.hotkey("ctrl", "v")
    time.sleep(5) 

    pyautogui.hotkey("ctrl", "enter")
    print("Excel data + attachment Gmail pe bhej diya gaya")