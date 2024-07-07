import clipboard  # To interact with the clipboard
import time  # For setting intervals
import csv  # To record history in a CSV file
import os  # To check if the file already exists

# Function to save clipboard content to a CSV file
def save_clipboard_history(filename, content):
    # Check if the file already exists
    file_exists = os.path.isfile(filename)

    # Open the CSV file in append mode
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header if the file is new
        if not file_exists:
            writer.writerow(["Timestamp", "Clipboard Content"])

        # Write the content and timestamp
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), content])

# Set the interval for checking the clipboard
check_interval = 2  # Check every 2 seconds

# File to store the clipboard history
clipboard_history_file = "clipboard_history.csv"

# Variable to keep track of the last clipboard content
last_clipboard_content = None

print("Recording clipboard history. Press Ctrl+C to stop.")

try:
    while True:
        # Get the current clipboard content
        current_clipboard_content = clipboard.paste()

        # Check if the clipboard content has changed
        if current_clipboard_content != last_clipboard_content:
            # If changed, save to history and update the last content
            save_clipboard_history(clipboard_history_file, current_clipboard_content)
            last_clipboard_content = current_clipboard_content

        # Wait for the next interval
        time.sleep(check_interval)

except KeyboardInterrupt:
    print("Clipboard history recording stopped.")
