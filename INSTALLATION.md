# 🚀 WhatsApp AutoMessenger - Complete Project

## 📁 Project Structure

```
Auto Messeger/
├── .venv/                      # Python 3.14 Virtual Environment (Created)
├── .gitignore                  # Git ignore file
├── main.py                     # ⭐ Entry point - Run this file
├── requirements.txt            # Package dependencies
├── check_chromedriver.py       # Helper to verify ChromeDriver setup
├── setup.bat                   # Windows setup script
├── setup.sh                    # macOS/Linux setup script
│
├── QUICKSTART.md              # ⭐ Start here! (5-minute guide)
├── README.md                  # Full documentation
├── EXAMPLES.md                # Usage examples
├── TROUBLESHOOTING.md         # Problem solving guide
├── INSTALLATION.md            # This file
│
└── src/                       # Source code modules
    ├── __init__.py
    ├── main.py
    ├── user_input.py          # User input handling
    ├── file_handler.py        # Excel/CSV processing
    ├── whatsapp_bot.py        # WhatsApp Web automation
    └── message_sender.py      # Message sending logic
```

## ✅ What's Already Done

1. ✅ Python 3.14 virtual environment created
2. ✅ All packages installed (selenium, openpyxl, pandas)
3. ✅ All source code files created
4. ✅ Comprehensive documentation included

## 🎯 What You Need To Do

### Step 1: Download ChromeDriver (IMPORTANT!)

**⚠️ CRITICAL:** ChromeDriver version must match your Chrome browser version exactly!

1. **Check your Chrome version:**
   - Open Chrome → Menu (⋮) → **About Google Chrome**
   - Note your version number (e.g., 149.0.7827.22)

2. **Download ChromeDriver for your version:**
   
   **For Chrome 149.0.7827.22 (Windows 64-bit):**
   ```
   https://storage.googleapis.com/chrome-for-testing-public/149.0.7827.22/win64/chromedriver-win64.zip
   ```
   
   **For other versions:**
   Replace `149.0.7827.22` with your Chrome version in the URL:
   ```
   https://storage.googleapis.com/chrome-for-testing-public/[YOUR-CHROME-VERSION]/win64/chromedriver-win64.zip
   ```
   
   **Or manually:**
   - Go to: https://googlechromelabs.github.io/chrome-for-testing/
   - Find your Chrome version
   - Download the matching ChromeDriver for your OS
   - Extract the `.zip` file

3. **Place ChromeDriver - Choose one option:**
   
   **Option A: Copy to project folder (Easiest):**
   ```bash
   # Extract chromedriver.exe from the zip
   # Copy it to the project root folder:
   d:\Auto Messeger\chromedriver.exe
   ```
   
   **Option B: Add to System PATH (Recommended for multiple projects):**
   - Extract the `chromedriver.exe` file
   - Add the folder containing it to your Windows PATH environment variable
   - [Windows PATH Setup Guide](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/)

4. **Verify installation:**
   ```bash
   cd "d:\Auto Messeger"
   ".venv\Scripts\python.exe" check_chromedriver.py
   ```
   
   ✅ If successful, you'll see: `ChromeDriver found and working!`

### Step 2: Run the Application

**Windows:**
```bash
cd "d:\Auto Messeger"
".venv\Scripts\python.exe" main.py
```

**macOS/Linux:**
```bash
cd "d:/Auto Messeger"
source .venv/bin/activate
python main.py
```

## 📖 Documentation

| File | Purpose |
|------|---------|
| [QUICKSTART.md](QUICKSTART.md) | 5-minute setup and basic usage |
| [README.md](README.md) | Complete feature documentation |
| [EXAMPLES.md](EXAMPLES.md) | Usage scenarios and workflows |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Problem solving guide |

## 🎮 How To Use

### Option 1: Manual Number Entry
```
Answer "no" to file input
→ Enter number of recipients
→ Enter message
→ Enter phone numbers one by one
→ Scan QR code on WhatsApp Web
→ Messages send automatically!
```

### Option 2: Excel File
```
Answer "yes" to file input
→ Choose "excel"
→ Provide file path
→ Select sheet and column
→ Choose numbers to use
→ Enter message
→ Scan QR code
→ Messages send automatically!
```

### Option 3: CSV File
```
Answer "yes" to file input
→ Choose "csv"
→ Provide file path
→ Confirm column
→ Choose numbers to use
→ Enter message
→ Scan QR code
→ Messages send automatically!
```

## 📱 Phone Number Format

Must use international format without '+':
- India: 919876543210 (for +91 9876543210)
- US: 1XXXXXXXXXX (for +1 XXXXXXXXXX)
- UK: 44XXXXXXXXXX (for +44 XXXXXXXXXX)

Length: 7-15 digits

## 📊 Features Included

✅ **File Support:**
- Excel (.xlsx, .xls)
- CSV (.csv)
- Auto-detect phone number columns
- Select specific sheets/rows
- Handle large contact lists

✅ **WhatsApp Integration:**
- Automatic login via QR code
- Find existing contacts
- Create new chats
- Send messages sequentially
- Success/failure tracking

✅ **User-Friendly:**
- Interactive prompts
- Input validation
- Progress tracking
- Detailed summaries
- Error handling

✅ **Developer-Friendly:**
- Modular code structure
- Well-documented
- Easy to extend
- Clear separation of concerns

## 🔧 System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.14+ (already installed)
- **RAM**: 1GB minimum
- **Browser**: Google Chrome (latest)
- **Internet**: Required for WhatsApp Web

## ⚙️ Customization

### Change message delay:
Edit [src/message_sender.py](src/message_sender.py), line ~90:
```python
time.sleep(3)  # Change 3 to your desired seconds
```

### Increase login timeout:
Edit [src/whatsapp_bot.py](src/whatsapp_bot.py), line ~35:
```python
self.wait = WebDriverWait(self.driver, 20)  # Change 20 to seconds needed
```

### Enable headless mode:
Edit [src/whatsapp_bot.py](src/whatsapp_bot.py), line ~43:
```python
# Uncomment this line:
options.add_argument('--headless')
```

## 🐛 Troubleshooting

Before running, check:
1. ✓ Chrome is installed
2. ✓ ChromeDriver is downloaded
3. ✓ ChromeDriver version matches Chrome version
4. ✓ Python environment activated
5. ✓ Packages installed: `pip list | grep -E "selenium|openpyxl|pandas"`

If issues persist, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## 📝 Files Overview

### Main Entry Point
- [main.py](main.py) - Orchestrates the application

### Source Modules
- [src/user_input.py](src/user_input.py) - Handles all user interactions
- [src/file_handler.py](src/file_handler.py) - Excel/CSV file processing
- [src/whatsapp_bot.py](src/whatsapp_bot.py) - Selenium automation
- [src/message_sender.py](src/message_sender.py) - Message sending logic

### Documentation
- [README.md](README.md) - Full feature documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [EXAMPLES.md](EXAMPLES.md) - Real-world examples
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common issues

### Setup & Configuration
- [requirements.txt](requirements.txt) - Python packages
- [setup.bat](setup.bat) - Windows setup
- [setup.sh](setup.sh) - Unix setup
- [check_chromedriver.py](check_chromedriver.py) - Diagnostics

## ⚡ Quick Commands

```bash
# Verify Python environment
".venv\Scripts\python.exe" --version

# Check installed packages
".venv\Scripts\python.exe" -m pip list

# Verify ChromeDriver
python check_chromedriver.py

# Run the application
".venv\Scripts\python.exe" main.py
```

## 🎯 Next Steps

1. **Download ChromeDriver** → https://chromedriver.chromium.org/downloads
2. **Read QUICKSTART.md** → Get started in 5 minutes
3. **Run main.py** → Start using the tool
4. **Check TROUBLESHOOTING.md** → If you encounter issues

## 📞 Support

- 📖 Read documentation files (README, QUICKSTART, TROUBLESHOOTING)
- 🔧 Run `python check_chromedriver.py` for diagnostics
- 💡 Check examples in [EXAMPLES.md](EXAMPLES.md)

## 📋 Checklist Before First Run

- [ ] ChromeDriver downloaded and in PATH (or project folder)
- [ ] `python check_chromedriver.py` shows success
- [ ] Phone numbers are in correct format (international)
- [ ] Message text prepared
- [ ] WhatsApp logged out so you can login in browser
- [ ] Internet connection stable
- [ ] Chrome browser not open (script will open it)

## 🎉 Ready to Start?

```bash
cd "d:\Auto Messeger"
".venv\Scripts\python.exe" main.py
```

Happy messaging! 🚀
