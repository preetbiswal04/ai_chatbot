# RPA Automation Bot Instructions

## Prerequisites

1.  **Python Installed**: Ensure Python is installed on your system.
2.  **Dependencies**: Install required libraries using:
    ```bash
    pip install -r requirement.txt
    ```
    (Note: You might need to install `pandas` and `openpyxl` as well: `pip install pandas openpyxl`)
3.  **Image Resources**:
    - You must have `compose_button.png` and `attach.png` in the same directory as the scripts.
    - These images should be screenshots of the "Compose" and "Attach" buttons from your specific Gmail interface.
4.  **Screen Resolution**:
    - `web_form.py` uses hardcoded coordinates `(500, 400)`. You may need to adjust these in the file to match your screen resolution and browser position.

## How to Run

1.  **Open Command Prompt** or Terminal.
2.  **Navigate** to the project folder:
    ```bash
    cd c:\Users\preet\Downloads\rpa_automation_with_python
    ```
3.  **Run the Main Script**:
    ```bash
    python main.py
    ```

## What to Expect

1.  **Web Form**: (Currently commented out in `main.py` for safety) It would open Chrome and fill a form.
2.  **Excel Automation**: Opens Excel, enters data, calculates formulas, and saves as `marks_report.xlsx`.
3.  **Notepad Automation**: Opens Notepad and types a message.
4.  **Copy-Paste**: Simulates copy-paste operations.
5.  **Gmail Automation**:
    - Reads `marks_report.xlsx`.
    - Opens Gmail in Chrome.
    - Composes a new email to `preetbiswal04@gmail.com`.
    - Pastes the Excel data into the body.
    - Attaches the `marks_report.xlsx` file.
    - Sends the email.

## How to Fix "Button Not Found" (CRITICAL STEP)

The bot is "blind"—it needs reference pictures to find buttons. You must give it these pictures:

### 1. What is the "Paper Clip"?
The "Paper Clip" is the **Attach files** icon in Gmail. It looks like a small bent paper clip, usually at the bottom of the "New Message" window next to the "Send" button/formatting tools.

### 2. How to Create the Images
You need to take two small screenshots and save them in this folder: `c:\Users\preet\Downloads\rpa_automation_with_python\`

#### **Image 1: `compose_button.png`**
1.  Open Gmail in Chrome.
2.  Find the **Compose** button (top left, sometimes a pencil icon).
3.  Open the **Snipping Tool** (search "Snipping Tool" in Windows).
4.  Click **New**.
5.  Draw a box **ONLY around the button** (don't include extra background).
6.  Save the file as `compose_button.png` inside the project folder.

#### **Image 2: `attach.png`**
1.  Click "Compose" to open a new email window.
2.  Find the **Paper Clip** icon (at the bottom).
3.  Use **Snipping Tool** to take a screenshot of **just the paper clip icon**.
4.  Save the file as `attach.png` inside the project folder.

#### **Image 3: `account_avatar.png` (For Account Selection)**
1.  Open Chrome and go to Gmail (where you see the list of accounts).
2.  Take a screenshot of **your profile picture/name** (the one you want to click).
3.  Save it as `account_avatar.png` in the project folder.

### 3. Verify
Your folder should look like this:
- `main.py`
- ...
- `compose.png`
- `attach.png`
- `account_avatar.png`

If these images are missing or don't match your screen exactly, the bot will fail.
