# WhatsApp AutoMessenger

A Python-based automation tool to send messages to multiple recipients via WhatsApp Web using Selenium.

## Features

- **Two Input Methods:**
  - Manual: Enter phone numbers one by one
  - File-based: Upload Excel (.xlsx, .xls) or CSV files

- **Excel/CSV Support:**
  - Automatically detects phone number columns
  - Select specific sheets and number ranges
  - Process all numbers or limit to specific rows

- **WhatsApp Integration:**
  - Opens WhatsApp Web automatically
  - Waits for user login
  - Creates new chats for new numbers
  - Sends messages to multiple recipients sequentially

- **User-Friendly:**
  - Interactive prompts and validations
  - Real-time progress tracking
  - Detailed success/failure summary

## Requirements

- Python 3.14+
- Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Navigate to the project directory:
```bash
cd "d:\Auto Messeger"
```

2. Install dependencies:
```bash
"d:/Auto Messeger/.venv/Scripts/python.exe" -m pip install -r requirements.txt
```

3. Download ChromeDriver:
   - Visit: https://chromedriver.chromium.org/
   - Download the version matching your Chrome browser version
   - Add it to your PATH or place it in the project directory

## Usage

Run the main script:
```bash
"d:/Auto Messeger/.venv/Scripts/python.exe" main.py
```

### Manual Number Entry:
1. When prompted, select "no" for file input
2. Enter the number of recipients
3. Enter the message
4. Enter each phone number one by one
5. Confirm and login to WhatsApp
6. The script will automatically send messages

### File Input (Excel/CSV):
1. When prompted, select "yes" for file input
2. Choose between Excel or CSV
3. Provide the file path
4. Select the sheet (Excel only)
5. Confirm the phone number column
6. Choose to use all numbers or limit to a specific row
7. Enter the message
8. Confirm and login to WhatsApp
9. The script will automatically send messages

## Phone Number Format

- Use international format without the '+' symbol
- Example: 919876543210 (for +91 9876543210)
- Minimum 7 digits, maximum 15 digits

## File Format

### Excel (.xlsx, .xls):
- Column header should contain: "Number", "Phone", "Mobile", "Contact", "Tel", "Telephone", or "No."
- Phone numbers should start from row 2 (row 1 is header)

### CSV (.csv):
- Column header should contain: "Number", "Phone", "Mobile", "Contact", "Tel", "Telephone", or "No."
- One phone number per row

Example Excel/CSV:
```
Number       | Name
919876543210 | John
919876543211 | Jane
919876543212 | Bob
```

## Troubleshooting

### ChromeDriver Issues:
- Make sure ChromeDriver version matches your Chrome browser version
- Download from: https://chromedriver.chromium.org/

### Login Issues:
- Keep your phone connected and WhatsApp active
- Don't close the browser window during login
- If timeout occurs, make sure to scan the QR code quickly

### Message Not Sending:
- Check internet connection
- Verify phone numbers are in correct format
- Ensure contact doesn't have message restrictions
- Some numbers might be blocked by WhatsApp

## Project Structure

```
Auto Messeger/
├── main.py                 # Entry point
├── requirements.txt        # Package dependencies
├── README.md              # This file
└── src/
    ├── __init__.py
    ├── user_input.py      # User input handling
    ├── file_handler.py    # Excel/CSV file processing
    ├── whatsapp_bot.py    # WhatsApp Web automation
    └── message_sender.py  # Main messaging logic
```

## Notes

- Messages are sent sequentially with 3-second delay between each
- The script creates new chats for numbers not in your contacts
- Be cautious of WhatsApp's rate limiting
- Keep the browser window open during message sending
- Messages are sent exactly as typed (no formatting applied)

## Disclaimer

This tool is for educational and personal use only. Ensure you comply with WhatsApp's Terms of Service and local regulations. The author is not responsible for any misuse of this tool.
