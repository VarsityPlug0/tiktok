#!/usr/bin/env python3
"""
Simple Gmail SMTP connection test
This will help diagnose the exact authentication issue
"""

import smtplib
from email.mime.text import MIMEText

# Your Gmail credentials
username = "tiktokresetpass.req@gmail.com"
password = "gnon sheo ehxs clgt"

print("🔍 Gmail SMTP Connection Test")
print("=" * 40)
print(f"Username: {username}")
print(f"Password: {password[:4]}...{password[-4:] if len(password) > 8 else '****'}")
print()

try:
    # Step 1: Connect to Gmail SMTP
    print("📡 Step 1: Connecting to Gmail SMTP...")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    print("✅ Connected to Gmail SMTP")
    
    # Step 2: Start TLS encryption
    print("🔒 Step 2: Starting TLS encryption...")
    server.starttls()
    print("✅ TLS encryption started")
    
    # Step 3: Authenticate
    print("🔐 Step 3: Authenticating...")
    server.login(username, password)
    print("✅ Authentication successful!")
    
    # Step 4: Test sending a simple email
    print("📧 Step 4: Testing email send...")
    
    # Create a simple test message
    msg = MIMEText("This is a test email from TikTok Email System")
    msg["From"] = username
    msg["To"] = username  # Send to yourself for testing
    msg["Subject"] = "TikTok Email System Test"
    
    # Send the email
    server.sendmail(username, username, msg.as_string())
    print("✅ Test email sent successfully!")
    
    # Close connection
    server.quit()
    print("\n🎉 All tests passed! Your Gmail configuration is working.")
    
except smtplib.SMTPAuthenticationError as e:
    print(f"❌ Authentication failed: {e}")
    print("\n🔧 Solutions:")
    print("1. Check if 2-Factor Authentication is enabled on your Gmail account")
    print("2. Generate an App Password from Google Account settings")
    print("3. Use the App Password instead of your regular password")
    print("4. Make sure 'Less secure app access' is not blocking the connection")
    
except smtplib.SMTPException as e:
    print(f"❌ SMTP error: {e}")
    
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("\n📚 Next steps:")
print("1. Go to: https://myaccount.google.com/security")
print("2. Check 2-Step Verification status")
print("3. Generate App Password if needed")
print("4. Update smtp.py with the new password")
