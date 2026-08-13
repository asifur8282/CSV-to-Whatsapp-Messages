"""
Message Sender Module
Orchestrates the message sending process
"""

import time
import sys
from src.whatsapp_bot import WhatsAppBot


class MessageSender:
    """Handles the message sending process"""
    
    def __init__(self):
        self.bot = WhatsAppBot()
        self.successful_sends = 0
        self.failed_sends = 0
    
    def send_messages(self, recipients: list, message: str, min_delay: int = 5, max_delay: int = 20) -> None:
        """
        Send messages to multiple recipients.

        Args:
            recipients: List of phone numbers
            message: The message to send
            min_delay: Minimum delay between sends in seconds
            max_delay: Maximum delay between sends in seconds
        """
        # Reset counters for the current batch
        self.successful_sends = 0
        self.failed_sends = 0

        # Initialize bot
        if not self.bot.initialize_driver():
            print("\n❌ Failed to initialize bot. Exiting...")
            return
        
        try:
            # Open WhatsApp Web
            if not self.bot.open_whatsapp_web():
                print("\n❌ Failed to open WhatsApp Web. Exiting...")
                return
            
            # Wait for login
            if not self.bot.wait_for_login():
                print("\n❌ Login failed. Exiting...")
                return
            
            # Give user time to prepare
            print("\n⏳ Preparing to send messages...")
            time.sleep(2)
            
            total = len(recipients)
            
            # Send messages to each recipient
            import random
            for index, recipient in enumerate(recipients, 1):
                print(f"\n{'='*60}")
                print(f"📨 Sending to recipient {index}/{total}: {recipient}")
                print(f"{'='*60}")
                
                if self._send_to_recipient(recipient, message):
                    self.successful_sends += 1
                else:
                    self.failed_sends += 1
                
                # Wait between messages to avoid rate limiting
                if index < total:
                    delay = random.randint(max(0, min_delay), max(0, max_delay))
                    print(f"⏳ Waiting for {delay} seconds before the next message to mimic human behavior...")
                    time.sleep(delay)
            
            # Print summary
            self._print_summary(total)
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Operation interrupted by user")
            self._print_summary(len(recipients))
        
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}")
            self._print_summary(len(recipients))
            
    def close(self) -> None:
        """Close the browser session"""
        self.bot.close_driver()
    
    def _send_to_recipient(self, phone_number: str, message: str) -> bool:
        """
        Send message to a single recipient
        
        Args:
            phone_number: Recipient's phone number
            message: The message to send
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Search for contact
            if not self.bot.search_contact(phone_number):
                print(f"❌ Failed to find/create chat for {phone_number}")
                return False
            
            # Wait for chat to load
            time.sleep(2)
            
            # Send message
            if not self.bot.send_message(message):
                print(f"❌ Failed to send message to {phone_number}")
                return False
            
            return True
        
        except Exception as e:
            print(f"❌ Error sending to {phone_number}: {str(e)}")
            return False
    
    def _print_summary(self, total: int) -> None:
        """
        Print summary of message sending
        
        Args:
            total: Total number of recipients
        """
        print(f"\n{'='*60}")
        print(f"  📊 MESSAGING SUMMARY")
        print(f"{'='*60}")
        print(f"✅ Successful: {self.successful_sends}/{total}")
        print(f"❌ Failed: {self.failed_sends}/{total}")
        
        if self.successful_sends == total:
            print(f"\n🎉 All messages sent successfully!")
        elif self.successful_sends > 0:
            print(f"\n⚠️  {self.successful_sends} messages sent, {self.failed_sends} failed")
        else:
            print(f"\n❌ No messages were sent successfully")
        
        print(f"{'='*60}\n")
