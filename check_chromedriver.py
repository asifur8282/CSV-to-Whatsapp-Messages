"""
ChromeDriver Setup Helper
Helps users set up ChromeDriver for Selenium
"""

import subprocess
import sys
import os
from pathlib import Path


def get_chrome_version():
    """Get installed Chrome browser version"""
    try:
        # Windows
        if sys.platform == "win32":
            result = subprocess.run(
                r"reg query HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon /v version",
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                version = result.stdout.split()[-1]
                return version
        
        # macOS
        elif sys.platform == "darwin":
            result = subprocess.run(
                ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return result.stdout.split()[-1]
        
        # Linux
        else:
            result = subprocess.run(
                ["google-chrome", "--version"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return result.stdout.split()[-1]
    except:
        pass
    
    return None


def check_chromedriver():
    """Check if ChromeDriver is available"""
    try:
        result = subprocess.run(
            ["chromedriver", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    
    return None


def main():
    """Main function"""
    print("\n" + "="*60)
    print("  ChromeDriver Setup Helper")
    print("="*60 + "\n")
    
    # Check Chrome version
    chrome_version = get_chrome_version()
    if chrome_version:
        major_version = chrome_version.split('.')[0]
        print(f"✅ Chrome browser found (version: {chrome_version})")
        print(f"   Download ChromeDriver version {major_version} from:")
        print(f"   https://chromedriver.chromium.org/downloads")
    else:
        print("⚠️  Chrome browser not found")
        print("   Please install Google Chrome from https://www.google.com/chrome/")
    
    # Check ChromeDriver
    chromedriver_version = check_chromedriver()
    if chromedriver_version:
        print(f"\n✅ ChromeDriver found: {chromedriver_version}")
    else:
        print("\n❌ ChromeDriver not found in PATH")
        print("   Download ChromeDriver from: https://chromedriver.chromium.org/downloads")
        print("   Add it to your PATH or place it in this directory")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
