from pywinauto.application import Application
import time 

def automate_notepad():
    app = Application(backend="uia").start("notepad.exe")
    time.sleep(2)

    notepad = app.window(title_re=".*notepad")

    notepad.type_keys(
        "Hello, this is an automated message.\n",
        with_spaces=True
        )

    notepad.type_keys(
        "This is another line of text.",
        with_spaces=True
        )

    print("Notepad automation completed.")

    