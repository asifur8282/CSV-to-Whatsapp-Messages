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
    
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def initialize_driver(self):
        """Initialize Selenium WebDriver for Chrome"""
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
            self.driver.get("https://web.whatsapp.com")
            print("✅ WhatsApp Web opened")
            return True
        except Exception as e:
            print(f"❌ Failed to open WhatsApp Web: {str(e)}")
            return False
    
    def wait_for_login(self, timeout: int = 300):
        """
        Wait for user to login to WhatsApp Web
        
        Args:
            timeout: Timeout in seconds (default 5 minutes)
            
        Returns:
            bool: True if login successful, False otherwise
        """
        print(f"\n⏳ Waiting for you to login (timeout: {timeout}s)...")
        print("   👉 Scan the QR code with your phone or login with your credentials")
        
        try:
            # Wait for the main chat list to appear (indicates successful login)
            self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@data-testid='chat-list']"))
            )
            print("✅ Login successful!")
            return True
        except TimeoutException:
            print("❌ Login timeout. Please login manually and try again.")
            return False
    
    def search_contact(self, phone_number: str) -> bool:
        """
        Search for a contact by phone number
        
        Args:
            phone_number: The phone number to search
            
        Returns:
            bool: True if contact found, False otherwise
        """
        try:
            # Click on the search box
            search_box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search or start new chat']"))
            )
            search_box.click()
            search_box.clear()
            
            # Type phone number
            search_box.send_keys(phone_number)
            
            # Wait for search results
            time.sleep(1)
            
            # Check if any result appears
            try:
                result = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//div[@role='option']")),
                    timeout=5
                )
                result.click()
                print(f"✅ Contact found for {phone_number}")
                return True
            except TimeoutException:
                print(f"⚠️  No existing contact found for {phone_number}. Creating new chat...")
                # If no result, try to start a new chat with the number
                return self._create_new_chat(phone_number)
        
        except Exception as e:
            print(f"❌ Error searching contact: {str(e)}")
            return False
    
    def _create_new_chat(self, phone_number: str) -> bool:
        """
        Create a new chat with a phone number
        
        Args:
            phone_number: The phone number
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Press Enter to create new chat with the number
            search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Search or start new chat']")
            search_box.send_keys(Keys.ENTER)
            
            time.sleep(2)
            
            # Check if chat window opened
            try:
                self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//div[@role='region'][@aria-label]")),
                    timeout=5
                )
                print(f"✅ New chat created for {phone_number}")
                return True
            except TimeoutException:
                print(f"❌ Failed to create new chat for {phone_number}")
                return False
        
        except Exception as e:
            print(f"❌ Error creating new chat: {str(e)}")
            return False
    
    def send_message(self, message: str) -> bool:
        """
        Send a message to the current chat
        
        Args:
            message: The message to send
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Find the message input box
            message_box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'][@contenteditable='true']")),
                timeout=10
            )
            
            # Click on message box
            message_box.click()
            
            # Type message (handle multi-line messages)
            for line in message.split('\n'):
                message_box.send_keys(line)
                message_box.send_keys(Keys.SHIFT, Keys.ENTER)
            
            # Find and click send button
            send_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Send']")),
                timeout=5
            )
            send_button.click()
            
            time.sleep(1)
            print(f"✅ Message sent")
            return True
        
        except TimeoutException:
            print("❌ Timeout: Could not find message input or send button")
            return False
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
