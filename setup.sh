#!/bin/bash
# WhatsApp AutoMessenger - Unix/Linux/Mac Setup Script

echo ""
echo "========================================"
echo "  WhatsApp AutoMessenger Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.14 or higher from https://www.python.org"
    exit 1
fi

echo "Step 1: Installing dependencies..."

# Create virtual environment
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip and install packages
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo ""
echo "========================================"
echo "Setup complete!"
echo "========================================"
echo ""
echo "To run the WhatsApp AutoMessenger:"
echo "  source venv/bin/activate"
echo "  python main.py"
echo ""
