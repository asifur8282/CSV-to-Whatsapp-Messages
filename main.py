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
    message_sender = MessageSender()
    
    try:
        while True:
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
                print("\n❌ No recipients found.")
                if not user_input_handler.ask_yes_no("Do you want to try sending messages again?"):
                    break
                continue
            
            # Anti-spam safety warning for large batches
            if len(recipients) > 30:
                print(f"\n⚠️ WARNING: You are attempting to send messages to {len(recipients)} recipients in a single session.")
                print("   Sending to more than 30 numbers significantly increases the risk of being banned by WhatsApp.")
                proceed_anyway = user_input_handler.ask_yes_no("Are you sure you want to proceed with this many recipients?")
                if not proceed_anyway:
                    limit_30 = user_input_handler.ask_yes_no("Would you like to automatically limit the batch to the first 30 recipients?")
                    if limit_30:
                        recipients = recipients[:30]
                        print(f"✅ Batch limited to the first {len(recipients)} recipients.")
                    else:
                        print("❌ Operation cancelled. Returning to input menu...")
                        continue

            # Get the message to send
            message = user_input_handler.get_message()
            
            # Confirm before proceeding
            print(f"\n📋 Summary:")
            print(f"   Recipients: {len(recipients)}")
            print(f"   Message: {message[:50]}{'...' if len(message) > 50 else ''}")
            
            proceed = user_input_handler.ask_yes_no("\nProceed to send messages?")
            
            if proceed:
                # Send messages
                message_sender.send_messages(recipients, message)
            else:
                print("\n❌ Operation cancelled by user.")
            
            # Ask if they want to send more messages
            send_more = user_input_handler.ask_yes_no("\nDo you want to send another batch of messages?")
            if not send_more:
                break
                
    finally:
        # Close browser session at the very end
        message_sender.close()
        print("\n👋 Thank you for using WhatsApp AutoMessenger!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)
