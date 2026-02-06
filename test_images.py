import pyautogui
import time
import os

def test_image(image_name):
    print(f"--- Testing {image_name} ---")
    if not os.path.exists(image_name):
        print(f"❌ FILE NOT FOUND: {image_name}")
        print("   -> Please check the filename and folder.")
        return

    print(f"Looking for '{image_name}' on screen... (Move the window so the image is visible!)")
    try:
        location = pyautogui.locateOnScreen(image_name, confidence=0.7, grayscale=True)
        if location:
            print(f"✅ SUCCESS: Found {image_name} at {location}")
        else:
            print(f"❌ FAILED: Could not find {image_name} on the screen.")
    except pyautogui.ImageNotFoundException:
        print(f"❌ FAILED: Could not find {image_name} (ImageNotFoundException).")
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    print("---------------------------------------------------------")
    print(" DEBUG MODE: Checking if the bot can see your images")
    print("---------------------------------------------------------")
    print("1. Open the screen where the image is visible.")
    print("2. Make sure Chrome is 100% Zoom (Ctrl + 0).")
    print("3. I will give you 10 seconds before checking each image.")
    print("---------------------------------------------------------")
    
    # Test 1: Account Avatar
    print("\n👉 Preparing to look for 'account_avatar.png'...")
    print("   Open Chrome to the 'Who's using Chrome?' profile screen NOW!")
    for i in range(10, 0, -1):
        print(f"   Checking in {i}...", end="\r")
        time.sleep(1)
    test_image("account_avatar.png")

    # Test 2: Compose Button
    print("\n👉 Preparing to look for 'compose.png'...")
    print("   Open Gmail inbox NOW!")
    for i in range(10, 0, -1):
        print(f"   Checking in {i}...", end="\r")
        time.sleep(1)
    test_image("compose.png")

    # Test 3: Attach Button
    print("\n👉 Preparing to look for 'attach.png'...")
    print("   Open a 'New Message' window in Gmail NOW!")
    for i in range(10, 0, -1):
        print(f"   Checking in {i}...", end="\r")
        time.sleep(1)
    test_image("attach.png")
    
    print("\n--- Test Completed ---")
