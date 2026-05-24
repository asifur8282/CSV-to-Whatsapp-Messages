# Troubleshooting Guide - WhatsApp AutoMessenger

## Common Issues and Solutions

### 1. ChromeDriver Issues

**Problem**: `ChromeDriver not found in PATH` or `SessionNotCreatedException`

**Solutions**:
- Download ChromeDriver matching your Chrome version: https://chromedriver.chromium.org/downloads
- Check your Chrome version: Chrome Menu > Settings > About Chrome
- Add ChromeDriver to PATH or place it in the project directory
- Make sure ChromeDriver is executable (on macOS/Linux): `chmod +x chromedriver`

**Check your setup**:
```bash
python check_chromedriver.py
```

---

### 2. Login Issues

**Problem**: QR code not appearing or login timeout

**Solutions**:
- Make sure browser window stays open during login
- Ensure your internet connection is stable
- Try waiting longer - some networks are slow
- Restart WhatsApp on your phone
- Try logging out and logging back in on WhatsApp Web manually first
- Increase timeout in `src/whatsapp_bot.py` (line: `self.wait = WebDriverWait(self.driver, 20)`)

**Debug**: Open browser manually at https://web.whatsapp.com to test login

---

### 3. Message Not Sending

**Problem**: Messages fail to send to specific numbers

**Solutions**:
- Verify phone number format (must be valid international format)
- Check if the number is blocked or restricted on WhatsApp
- Ensure the number has an active WhatsApp account
- Try sending a manual message first to test
- Check if you have message restrictions enabled on the contact

**Common phone formats**:
- India: 91XXXXXXXXXX
- US: 1XXXXXXXXXX
- UK: 44XXXXXXXXXX

---

### 4. File Reading Issues

**Problem**: Excel/CSV file not found or not read correctly

**Solutions**:
- Use absolute path or full path to file
- Ensure file is not open in another application
- Check file format is correct (.xlsx, .xls, or .csv)
- Verify column header contains one of: "Number", "Phone", "Mobile", "Contact"
- Ensure phone numbers are in cells, not in comments or notes
- For CSV files, use comma separator (not semicolon)

**Test**: Open file manually and verify:
- Column headers are correct
- Phone numbers start from row 2
- No empty cells in the middle

---

### 5. Python Environment Issues

**Problem**: `ModuleNotFoundError` or package not found

**Solutions**:
- Ensure virtual environment is activated
- Reinstall packages: `pip install -r requirements.txt`
- Update pip: `python -m pip install --upgrade pip`
- Check Python version: `python --version` (must be 3.14+)

**Verify environment**:
```bash
"path/to/.venv/Scripts/python.exe" -c "import selenium; print(selenium.__version__)"
```

---

### 6. Contact Search Issues

**Problem**: Script can't find contacts or create new chats

**Solutions**:
- Ensure you're logged in to WhatsApp Web
- Check if phone number format is correct
- Some regions may require specific format adjustments
- Try searching manually on WhatsApp Web first
- Clear browser cache if issues persist

---

### 7. Rate Limiting

**Problem**: Messages send to first few contacts but then fail

**Solutions**:
- WhatsApp has rate limits to prevent spam
- Increase delay between messages in `src/message_sender.py`:
  ```python
  time.sleep(3)  # Change 3 to higher value like 5 or 10
  ```
- Send to fewer recipients in a single session
- Wait a few hours before sending another batch

---

### 8. Browser Crashes or Freezes

**Problem**: Chrome browser crashes or becomes unresponsive

**Solutions**:
- Update Chrome to the latest version
- Update ChromeDriver to match Chrome version
- Disable extensions that might interfere: add to options in `whatsapp_bot.py`
  ```python
  options.add_argument('--disable-extensions')
  ```
- Run without headless mode for debugging (currently disabled by default)
- Clear browser cache: `rm -rf ~/.wdm/*` (macOS/Linux) or clear manually on Windows

---

### 9. WhatsApp Web Not Loading

**Problem**: WhatsApp Web takes too long to load or shows blank page

**Solutions**:
- Check internet connection
- Try accessing https://web.whatsapp.com manually in Chrome
- Clear browser cookies and cache
- Try in a different browser if available
- Disable VPN if using one (WhatsApp may block)

---

### 10. Excel Sheet Not Found

**Problem**: Script can't find or list Excel sheets

**Solutions**:
- Ensure file is a valid Excel file (.xlsx or .xls)
- The file should not be corrupted
- Try opening in Excel to verify
- Use `.xlsx` format (newer) instead of `.xls` if possible
- Rebuild the Excel file if it's very old or complex

---

## Debug Mode

To enable more detailed logging, modify `src/whatsapp_bot.py`:

```python
# Add at the beginning of __init__
import logging
logging.basicConfig(level=logging.DEBUG)
```

Or run with Python verbose mode:
```bash
python -v main.py
```

---

## Performance Tips

1. **Message sending is slow?**
   - Reduce delay in `message_sender.py`
   - Use headless mode (uncomment in `whatsapp_bot.py`)

2. **Too many failures?**
   - Increase waits/timeouts
   - Reduce batch size
   - Validate phone numbers before running

3. **Browser resources high?**
   - Run in headless mode
   - Close other browser windows
   - Restart between batches

---

## Getting Help

If you encounter issues:

1. Check this troubleshooting guide first
2. Review the error message carefully
3. Check Chrome and ChromeDriver versions match
4. Try running `check_chromedriver.py` for diagnostics
5. Test components individually:
   - Test file reading separately
   - Test WhatsApp Web login manually
   - Test message sending on one contact manually

---

## Reporting Issues

When reporting issues, include:
- Error message (full text)
- Your OS and Python version
- Chrome version
- Steps to reproduce
- What you were trying to do
- Any recent changes to system or dependencies
