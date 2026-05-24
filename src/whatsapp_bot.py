"""
WhatsApp Bot Module
Handles WhatsApp Web automation using Selenium
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException
)


class WhatsAppBot:
    """Handles WhatsApp Web automation"""
    
    # Class-level list of XPaths for various elements to ensure robustness
    SEARCH_BOX_XPATHS = [
        "//div[@contenteditable='true'][@data-tab='3']",
        "//div[@data-testid='chat-list-search']",
        "//div[@data-testid='chat-list-search-input']",
        "//div[@id='side']//div[@role='textbox']",
        "//input[@placeholder='Search or start new chat']",
        "//div[@id='side']//div[@contenteditable='true']"
    ]
    
    SEARCH_RESULT_XPATHS = [
        "//div[@role='option']",
        "//div[@data-testid='search-results-list']//div[@role='row']",
        "//div[@id='side']//div[@role='row']",
        "//div[@data-testid='chat-list']//div[@role='row']",
        "//div[contains(@class, 'matched-text')]"
    ]
    
    MESSAGE_BOX_XPATHS = [
        "//div[@contenteditable='true'][@data-tab='10']",
        "//div[@data-testid='conversation-compose-box-input']",
        "//div[@id='main']//div[@role='textbox'][@contenteditable='true']",
        "//footer//div[@role='textbox'][@contenteditable='true']",
        "//div[@role='textbox'][@contenteditable='true']"
    ]
    
    SEND_BUTTON_XPATHS = [
        "//button[@aria-label='Send']",
        "//span[@data-testid='send']",
        "//button[@data-testid='compose-btn-send']",
        "//span[@data-icon='send']/parent::button",
        "//button[contains(@class, 'send')]"
    ]

    def __init__(self):
        self.driver = None
        self.wait = None
    
    def initialize_driver(self):
        """Initialize Selenium WebDriver for Chrome"""
        if self.driver is not None:
            return True
        options = webdriver.ChromeOptions()
        # Uncomment the line below to run in headless mode
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--start-maximized')
        
        try:
            self.driver = webdriver.Chrome(options=options)
            self.wait = WebDriverWait(self.driver, 20)
            print("✅ Chrome driver initialized successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to initialize Chrome driver: {str(e)}")
            print("   Make sure ChromeDriver is installed and in PATH")
            return False
    
    def open_whatsapp_web(self):
        """Open WhatsApp Web"""
        try:
            if self.driver and "web.whatsapp.com" in self.driver.current_url:
                return True
            self.driver.get("https://web.whatsapp.com")
            print("✅ WhatsApp Web opened")
            return True
        except Exception as e:
            print(f"❌ Failed to open WhatsApp Web: {str(e)}")
            return False
    
    def wait_for_login(self, timeout: int = 1000):
        """
        Wait for user to login to WhatsApp Web
        
        Args:
            timeout: Timeout in seconds (default 1000 seconds)
            
        Returns:
            bool: True if login successful, False otherwise
        """
        # Quick check if already logged in
        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-testid='chat-list'] | //div[@id='pane-side'] | //div[@role='grid']"))
            )
            print("✅ Already logged in!")
            return True
        except:
            pass

        print(f"\n⏳ Waiting for you to login (timeout: {timeout}s)...")
        print("   👉 Scan the QR code with your phone or login with your credentials")
        
        try:
            # Wait for the main chat list or sidebar to appear (indicates successful login) using actual timeout
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-testid='chat-list'] | //div[@id='pane-side'] | //div[@role='grid']"))
            )
            print("✅ Login successful!")
            return True
        except TimeoutException:
            print("❌ Login timeout. Please login manually and try again.")
            return False
            
    def _find_element_by_multiple_xpaths(self, xpath_list: list, timeout: int = 10):
        """
        Try to find an element using a list of alternative XPaths
        
        Args:
            xpath_list: List of XPath strings
            timeout: Timeout in seconds
            
        Returns:
            WebElement: The first found element
            
        Raises:
            NoSuchElementException: If none of the XPaths match
        """
        last_exception = None
        for xpath in xpath_list:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                # Wait up to 2 seconds until element is visible/clickable
                WebDriverWait(self.driver, 2).until(
                    EC.visibility_of(element)
                )
                return element
            except Exception as e:
                last_exception = e
                continue
        
        raise NoSuchElementException(f"None of the XPaths matched: {xpath_list}") from last_exception

    def _handle_invalid_number_modal(self) -> bool:
        """
        Check if invalid number modal is present, dismiss it, and return True if it was present
        """
        modal_xpaths = [
            "//div[contains(text(), 'Phone number shared via url is invalid')]",
            "//div[contains(text(), 'invalid')]",
            "//div[contains(text(), 'incorrect')]"
        ]
        for xpath in modal_xpaths:
            try:
                # Use a very short timeout here to avoid blocking
                modal = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                print("⚠️  Invalid phone number modal detected.")
                # Try to dismiss it by finding the button with "OK"
                try:
                    ok_button = WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'OK')] | //div[@role='button'][contains(., 'OK')] | //button[contains(., 'Ok')] | //div[@role='button'][contains(., 'Ok')]"))
                    )
                    ok_button.click()
                    print("✅ Dismissed the invalid number modal")
                except:
                    # Fallback: Send Escape key to body to dismiss
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
                    print("✅ Sent ESCAPE key to dismiss modal")
                return True
            except:
                continue
        return False

    def search_contact(self, phone_number: str) -> bool:
        """
        Open a chat with a phone number (bypasses UI search and uses direct navigation for 100% reliability)
        
        Args:
            phone_number: The phone number to search
            
        Returns:
            bool: True if chat loaded successfully, False otherwise
        """
        return self._create_new_chat(phone_number)
    
    def _create_new_chat(self, phone_number: str) -> bool:
        """
        Create/open a chat with a phone number using direct URL navigation
        
        Args:
            phone_number: The phone number
            
        Returns:
            bool: True if chat loaded successfully, False otherwise
        """
        try:
            print(f"🔗 Navigating directly to chat for {phone_number}...")
            url = f"https://web.whatsapp.com/send?phone={phone_number}"
            self.driver.get(url)
            
            # Let's wait for either the compose box OR the invalid number modal
            start_time = time.time()
            timeout = 25 # WhatsApp Web direct link can take some time to load
            
            while time.time() - start_time < timeout:
                # Check invalid number modal
                if self._handle_invalid_number_modal():
                    print(f"❌ Phone number {phone_number} is invalid or direct chat not allowed by WhatsApp.")
                    return False
                
                # Check if compose box is present
                try:
                    self._find_element_by_multiple_xpaths(self.MESSAGE_BOX_XPATHS, timeout=1)
                    print(f"✅ Chat loaded successfully via direct link for {phone_number}")
                    return True
                except:
                    pass
                
                time.sleep(1)
            
            print(f"❌ Timeout waiting for chat page to load for {phone_number}")
            return False
            
        except Exception as e:
            print(f"❌ Error during direct chat navigation: {str(e)}")
            return False
    
    def send_message(self, message: str) -> bool:
        """
        Send a message to the current chat
        
        Args:
            message: The message to send
            
        Returns:
            bool: True if successful, False otherwise
        """
        import random
        try:
            # Find the message input box
            message_box = self._find_element_by_multiple_xpaths(self.MESSAGE_BOX_XPATHS, timeout=10)
            
            # Click on message box
            message_box.click()
            
            # Clear it if there is any pre-existing text
            message_box.send_keys(Keys.CONTROL + "a")
            message_box.send_keys(Keys.BACKSPACE)
            
            # Type message simulating human speed character by character
            print("⌨️  Simulating human typing...")
            for char in message:
                if char == '\n':
                    message_box.send_keys(Keys.SHIFT, Keys.ENTER)
                else:
                    message_box.send_keys(char)
                # Sleep a tiny random duration between 0.02 and 0.08 seconds per character
                time.sleep(random.uniform(0.02, 0.08))
            
            # Random short pause after typing completes
            time.sleep(random.uniform(0.5, 1.2))
            
            # Try to send by clicking the send button or pressing ENTER
            try:
                # Find and click send button
                send_button = self._find_element_by_multiple_xpaths(self.SEND_BUTTON_XPATHS, timeout=5)
                send_button.click()
            except Exception:
                # Fallback: send Enter key
                print("⚠️  Send button not found or not clickable, trying Enter key...")
                message_box.send_keys(Keys.ENTER)
            
            time.sleep(1)
            print(f"✅ Message sent")
            return True
        
        except Exception as e:
            print(f"❌ Error sending message: {str(e)}")
            return False
    
    def close_driver(self):
        """Close the WebDriver"""
        if self.driver:
            self.driver.quit()
            print("✅ Browser closed")
    
    def get_last_message_from_contact(self) -> str:
        """
        Get the last message from the current contact
        
        Returns:
            str: The last message text or None
        """
        try:
            # Find the last message in chat
            messages = self.driver.find_elements(By.XPATH, "//div[@role='region']//div[contains(@class, 'message')]")
            
            if messages:
                last_message = messages[-1].text
                return last_message
            
            return None
        except:
            return None
