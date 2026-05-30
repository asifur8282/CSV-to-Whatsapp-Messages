# Quick Start Guide - WhatsApp AutoMessenger

Get started in 5 minutes!

## Prerequisites

- Python 3.14 or higher
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

## Step 1: Setup

### Windows:
```bash
setup.bat
```

### macOS/Linux:
```bash
chmod +x setup.sh
./setup.sh
```

### Manual Setup (All Platforms):
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate.bat
# Or on Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# Install packages
pip install -r requirements.txt
```

## Step 2: Download ChromeDriver

1. Check your Chrome version:
   - Open Chrome
   - Go to Menu (⋮) > Settings > About Chrome
   - Note the version number

2. Download matching ChromeDriver:
   - Visit: https://chromedriver.chromium.org/downloads
   - Download the driver for your Chrome version
   - Extract the executable

3. Add to PATH or place in project directory

**Verify**:
```bash
python check_chromedriver.py
```

## Step 3: Run the Application

You can use either the **Graphical User Interface (GUI)** or the command-line **CLI**.

### Option A: Running the GUI (Recommended)

- **On Windows:** Double-click the `gui.bat` launcher file in the project folder, or run:
  ```bash
  .venv\Scripts\python.exe gui.py
  ```
- **On macOS/Linux:**
  ```bash
  source .venv/bin/activate
  python gui.py
  ```

### Option B: Running the CLI

- **On Windows:**
  ```bash
  .venv\Scripts\python.exe main.py
  ```
- **On macOS/Linux:**
  ```bash
  source .venv/bin/activate
  python main.py
  ```

## Step 4: Choose Your Method

### Method 0: Graphical User Interface (GUI) - *Recommended*

The GUI is the easiest and most user-friendly way to use the application. Simply run it via Option A above.

1. **Select Input Mode:** Toggle between **Excel / CSV Spreadsheet** or **Manual Numbers List** using the radio buttons.
2. **Setup Recipients:**
   - **For Excel/CSV:** Click **Browse File** to select your sheet. The sheet name and phone column will be automatically loaded and detected.
   - **For Manual:** Enter the country code and number, then click **Add** to populate your recipient list.
3. **Compose Message:** Type your message in the text box.
4. **Automate:** Click **Start Automating**. Once the browser opens, scan the WhatsApp Web QR code to start sending.
5. **Control:** Click **Stop / Close Browser** at any time if you need to abort the sending process.

---

### Method 1: Manual Number Entry (Simplest CLI)

```
❓ Do you have an Excel or CSV file? (yes/no): no
❓ How many users do you want to send messages to?: 2
✍️  Enter the message you want to send: Hello!
   Enter recipient 1's number: 919876543210
   Enter recipient 2's number: 919876543211
```

### Method 2: Excel File

```
❓ Do you have an Excel or CSV file? (yes/no): yes
❓ Do you have an Excel or CSV file? (excel/csv): excel
❓ Enter the EXCEL file path: C:\Users\User\Documents\numbers.xlsx
📄 Available sheets: Contacts, Backup
❓ Enter sheet name: Contacts
❓ Use column A (Number)? (yes/no): yes
✍️  Enter the message you want to send: Hello!
```

### Method 3: CSV File

```
❓ Do you have an Excel or CSV file? (yes/no): yes
❓ Do you have an Excel or CSV file? (excel/csv): csv
❓ Enter the CSV file path: /home/user/numbers.csv
❓ Use column 'Number'? (yes/no): yes
❓ Use all numbers? (yes/no): no
❓ Enter the row number to limit to: 5
✍️  Enter the message you want to send: Hello!
```

## Step 5: Login to WhatsApp

1. Browser opens WhatsApp Web
2. Scan QR code with your phone or login manually
3. Wait for login to complete
4. Messages send automatically!

## Complete Example

### Using Excel File

**Excel file structure (numbers.xlsx)**:
```
| Number       | Name  |
|--------------|-------|
| 919876543210 | John  |
| 919876543211 | Jane  |
| 919876543212 | Bob   |
```

**Command flow**:
```bash
$ .venv\Scripts\python.exe main.py

============================================================
  WhatsApp AutoMessenger
============================================================

❓ Do you have an Excel or CSV file with phone numbers? (yes/no): yes

📁 File Type Selection
❓ Do you have an Excel or CSV file? (excel/csv): excel

❓ Enter the EXCEL file path: C:\Users\User\numbers.xlsx

📄 Available sheets: Sheet1
❓ Enter sheet name: Sheet1

❓ Use column A (Number)? (yes/no): yes

✅ Found 3 phone numbers in column A

❓ Use all numbers? (yes/no): yes
✅ Limited to 3 numbers

✍️  Enter the message you want to send: Hey! This is an automated message.

📋 Summary:
   Recipients: 3
   Message: Hey! This is an automated message.

❓ Proceed to send messages? (yes/no): yes

✅ Chrome driver initialized successfully
✅ WhatsApp Web opened

⏳ Waiting for you to login (timeout: 300s)...
   👉 Scan the QR code with your phone or login with your credentials

✅ Login successful!

============================================================
📨 Sending to recipient 1/3: 919876543210
============================================================
✅ Contact found for 919876543210
✅ Message sent

⏳ Waiting before next message...

============================================================
📨 Sending to recipient 2/3: 919876543211
============================================================
⚠️  No existing contact found for 919876543211. Creating new chat...
✅ New chat created for 919876543211
✅ Message sent

⏳ Waiting before next message...

============================================================
📨 Sending to recipient 3/3: 919876543212
============================================================
✅ Contact found for 919876543212
✅ Message sent

============================================================
  📊 MESSAGING SUMMARY
============================================================
✅ Successful: 3/3
❌ Failed: 0/3

🎉 All messages sent successfully!
============================================================
```

## Tips & Tricks

1. **Test First**: Try with 1-2 numbers before bulk sending
2. **Format Numbers**: Always use international format (e.g., 919876543210)
3. **Message Length**: Max 4096 characters per message
4. **Avoid Rate Limits**: Use delays and smaller batches
5. **Keep Active**: Don't close browser during sending
6. **Backup Data**: Save your contact list before using

## Next Steps

- Read [README.md](README.md) for detailed documentation
- Check [EXAMPLES.md](EXAMPLES.md) for more scenarios
- See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) if you encounter issues

## Support

Having issues? Check:
1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common issues and fixes
2. Chrome/ChromeDriver version match
3. Valid phone number format
4. File path is correct
5. Python environment is activated

Good luck! 🚀
