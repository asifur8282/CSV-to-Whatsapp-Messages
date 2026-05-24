"""
User Input Handler Module
Handles all user interactions and input validation
"""

import re


class UserInputHandler:
    """Handles user input for the WhatsApp automessenger"""
    
    @staticmethod
    def ask_yes_no(question: str) -> bool:
        """
        Ask user a yes/no question
        
        Args:
            question: The question to ask the user
            
        Returns:
            bool: True for yes, False for no
        """
        while True:
            response = input(f"\n❓ {question} (yes/no): ").strip().lower()
            if response in ['yes', 'y']:
                return True
            elif response in ['no', 'n']:
                return False
            else:
                print("   ⚠️  Please enter 'yes' or 'no'")
    
    @staticmethod
    def get_recipients_manual_input() -> list:
        """
        Get recipients manually from user input
        
        Returns:
            list: List of phone numbers
        """
        print("\n📱 Manual Number Entry Mode")
        
        while True:
            try:
                count = int(input("\n❓ How many users do you want to send messages to? "))
                if count < 1:
                    print("   ⚠️  Please enter a number greater than 0")
                    continue
                break
            except ValueError:
                print("   ⚠️  Please enter a valid number")
        
        recipients = []
        print(f"\n📝 Enter phone numbers (including country code, e.g., 919876543210):\n")
        
        for i in range(1, count + 1):
            while True:
                number = input(f"   Enter recipient {i}'s number: ").strip()
                
                # Validate phone number (basic validation)
                if UserInputHandler._validate_phone_number(number):
                    recipients.append(number)
                    break
                else:
                    print(f"   ⚠️  Invalid number format. Please use format like 919876543210")
        
        print(f"\n✅ Collected {len(recipients)} phone numbers")
        return recipients
    
    @staticmethod
    def _validate_phone_number(number: str) -> bool:
        """
        Validate phone number format
        
        Args:
            number: The phone number to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Remove any spaces or hyphens
        cleaned = number.replace(" ", "").replace("-", "")
        
        # Check if it's numeric and has reasonable length (7-15 digits)
        return bool(re.match(r"^\d{7,15}$", cleaned))
    
    @staticmethod
    def get_message() -> str:
        """
        Get the message to send from user input
        
        Returns:
            str: The message to send
        """
        while True:
            message = input("\n✍️  Enter the message you want to send: ").strip()
            if len(message) < 1:
                print("   ⚠️  Message cannot be empty")
                continue
            if len(message) > 4096:
                print("   ⚠️  Message is too long (max 4096 characters)")
                continue
            break
        
        return message
    
    @staticmethod
    def get_integer_input(prompt: str, min_value: int = 1, max_value: int = None) -> int:
        """
        Get integer input from user with validation
        
        Args:
            prompt: The prompt to display
            min_value: Minimum allowed value
            max_value: Maximum allowed value (None for no limit)
            
        Returns:
            int: The validated integer
        """
        while True:
            try:
                value = int(input(f"\n❓ {prompt}: ").strip())
                if value < min_value:
                    print(f"   ⚠️  Please enter a number >= {min_value}")
                    continue
                if max_value is not None and value > max_value:
                    print(f"   ⚠️  Please enter a number <= {max_value}")
                    continue
                return value
            except ValueError:
                print("   ⚠️  Please enter a valid number")
