from web_form import fill_web_form
from desktop_automation import automate_notepad
from utils import copy_past
from excel_pyautogui import excel_data_entry_with_formula
from gmail_automation import send_email_automation

def start_rpa():
    print("mini rpa bot started")
    
    
    excel_data_entry_with_formula() 
    # automate_notepad()
    
    # copy_past()
    
    send_email_automation() 

    print("mini rpa bot completed")

if __name__ == "__main__":
    start_rpa()