import pyautogui
import time
import pyperclip

# Function to click at specific coordinates
def click_at(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Function to drag from one point to another
def drag_from_to(start_x, start_y, end_x, end_y):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=1)  # Drag with a duration
    pyautogui.mouseUp()

# Function to copy selected text to clipboard
def copy_to_clipboard():
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait for the clipboard to be populated

# Function to get text from clipboard
def get_text_from_clipboard():
    return pyperclip.paste()

# Main function to perform the steps
def main():
    # Step 1: Click on the icon
    click_at(1132, 1045)
    time.sleep(1)  # Wait for any UI response

    # Step 2: Drag to select text
    drag_from_to(1065, 164, 1634, 981)
    time.sleep(1)  # Wait for the text to be selected

    # Step 3: Copy the selected text to clipboard
    copy_to_clipboard()

    # Step 4: Get the text from the clipboard
    text = get_text_from_clipboard()

    # Print the copied text
    print(f"Copied Text: {text}")

# Execute the main function
if __name__ == "__main__":
    main()
