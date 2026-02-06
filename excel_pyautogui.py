import pyautogui
import time

def excel_data_entry_with_formula():
    pyautogui.FAILSAFE = True

    
    pyautogui.hotkey("win", "r")      # Run dialog
    time.sleep(1)
    pyautogui.write("excel")          # Excel type
    pyautogui.press("enter")
    time.sleep(8)                     # Excel load wait
    
    # 1.5 Select "Blank Workbook" (Fix for modern Excel start screen)
    pyautogui.press("enter")
    time.sleep(2)

    
    pyautogui.write("Name")
    pyautogui.press("tab")

    pyautogui.write("Marks1")
    pyautogui.press("tab")

    pyautogui.write("Marks2")
    pyautogui.press("tab")

    pyautogui.write("Total")
    pyautogui.press("tab")

    pyautogui.write("Average")

  
    pyautogui.press("enter")

    pyautogui.write("Preet")
    pyautogui.press("tab")

    pyautogui.write("80")
    pyautogui.press("tab")

    pyautogui.write("90")
    pyautogui.press("tab")

    
    pyautogui.write("=B2+C2")
    pyautogui.press("tab")

   
    pyautogui.write("=AVERAGE(B2:C2)")
    pyautogui.press("enter")


    pyautogui.press("f12")  
    time.sleep(3)           
    
    
    pyautogui.write(r"c:\Users\preet\Downloads\rpa_automation_with_python\marks_report.xlsx")
    time.sleep(1)
    pyautogui.press("enter")
    
    
    time.sleep(1)
    pyautogui.press("y") 
    pyautogui.press("enter")

    print("✅ Excel data entry + formula automation done")
