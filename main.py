"""
WhatsApp Automessenger - Main Entry Point
Automates sending messages to multiple recipients via WhatsApp Web
"""

import sys
from src.user_input import UserInputHandler
from src.file_handler import FileHandler
from src.message_sender import MessageSender


def main():
    """Main function to run the WhatsApp automessenger"""
    print("\n" + "="*60)
    print("  WhatsApp AutoMessenger")
    print("="*60 + "\n")
    
    user_input_handler = UserInputHandler()
    
    # Ask if user has Excel/CSV file
    has_file = user_input_handler.ask_yes_no("Do you have an Excel or CSV file with phone numbers?")
    
    recipients = []
    
    if has_file:
        # File-based approach
        file_handler = FileHandler()
        recipients = file_handler.handle_file_input()
    else:
        # Manual input approach
        recipients = user_input_handler.get_recipients_manual_input()
    
    if not recipients:
        print("\n❌ No recipients found. Exiting...")
        sys.exit(1)
    
    # Get the message to send
    message = user_input_handler.get_message()
    
    # Confirm before proceeding
    print(f"\n📋 Summary:")
    print(f"   Recipients: {len(recipients)}")
    print(f"   Message: {message[:50]}{'...' if len(message) > 50 else ''}")
    
    proceed = user_input_handler.ask_yes_no("\nProceed to send messages?")
    
    if not proceed:
        print("\n❌ Operation cancelled by user.")
        sys.exit(0)
    
    # Send messages
    message_sender = MessageSender()
    message_sender.send_messages(recipients, message)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)
