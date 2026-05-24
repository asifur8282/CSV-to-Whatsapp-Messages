"""
Example usage scenarios for WhatsApp AutoMessenger
"""

# Example 1: Manual number entry
# When running the script:
# - Select: no (for file input)
# - Enter: 2 (number of recipients)
# - Enter message: "Hello! This is an automated message."
# - Enter number 1: 919876543210
# - Enter number 2: 919876543211
# - Scan QR code to login
# - Script sends messages automatically

# Example 2: Using Excel file
# File: recipients.xlsx
# Sheet: "Contacts"
# Column: A (Number)
# Contents:
# A1: Number      B1: Name
# A2: 919876543210  B2: John
# A3: 919876543211  B3: Jane
# A4: 919876543212  B4: Bob
#
# When running the script:
# - Select: yes (for file input)
# - Select: excel
# - Path: C:\Users\User\Documents\recipients.xlsx
# - Select sheet: Contacts
# - Confirm column: A (Number)
# - Use all numbers: yes
# - Enter message: "Hello! This is an automated message."
# - Scan QR code to login
# - Script sends to all 3 numbers


# Example 3: Using CSV file
# File: recipients.csv
# Contents:
# Number,Name
# 919876543210,John
# 919876543211,Jane
# 919876543212,Bob
# 919876543213,Alice
#
# When running the script:
# - Select: yes (for file input)
# - Select: csv
# - Path: C:\Users\User\Documents\recipients.csv
# - Confirm column: Number
# - Use all numbers: no
# - Limit to row: 3
# - Enter message: "Limited message to first 3 recipients"
# - Scan QR code to login
# - Script sends to first 3 numbers only


# Program Flow Diagram:
#
#  START
#    |
#    v
# Do you have Excel/CSV?
#    |
#    +---> YES ---> Select file type (Excel/CSV)
#    |                     |
#    |                     v
#    |              Choose file path
#    |                     |
#    |                     v
#    |              List sheets (if Excel)
#    |                     |
#    |                     v
#    |              Find/Confirm phone column
#    |                     |
#    |                     v
#    |              Use all numbers or limit?
#    |                     |
#    |                     v
#    |              Extract phone numbers
#    |                     |
#    +---> NO ----> Ask: How many recipients?
#                         |
#                         v
#                   Manually enter numbers
#                         |
#                         v
#            (Merge both paths here)
#                         |
#                         v
#                  Ask for message
#                         |
#                         v
#               Show summary & confirm
#                         |
#                         v
#             Initialize Selenium WebDriver
#                         |
#                         v
#             Open WhatsApp Web
#                         |
#                         v
#            Wait for user to login (QR code)
#                         |
#                         v
#           For each recipient:
#           - Search/create chat
#           - Send message
#           - Wait 3 seconds
#                         |
#                         v
#               Print success summary
#                         |
#                         v
#                        END
