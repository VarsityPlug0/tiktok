import requests
import json

def send_real_email():
    """Send a real email using the custom email sender"""
    print("📧 Sending Real Email...")
    
    # You need to fill in your REAL credentials here
    email_data = {
        "template": "tiktok_security",  # or "tiktok_verification" or "custom"
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "sender_email": "YOUR_EMAIL@gmail.com",  # 👈 CHANGE THIS to your real Gmail
        "sender_password": "YOUR_APP_PASSWORD",  # 👈 CHANGE THIS to your Gmail App Password
        "recipient_email": "recipient@example.com",  # 👈 CHANGE THIS to recipient
        "subject": "TikTok: Security Alert - New Device Login Detected",
        "username": "User",  # 👈 CHANGE THIS to recipient's name
        "custom_message": "This is a test email from your TikTok email system!"
    }
    
    print("⚠️  IMPORTANT: Edit this script with your REAL credentials before running!")
    print(f"   Current sender: {email_data['sender_email']}")
    print(f"   Current recipient: {email_data['recipient_email']}")
    print(f"   Current subject: {email_data['subject']}")
    
    # Ask for confirmation
    confirm = input("\n❓ Do you want to proceed with sending this email? (yes/no): ")
    if confirm.lower() != 'yes':
        print("❌ Email sending cancelled.")
        return
    
    try:
        print("\n📤 Sending email...")
        response = requests.post(
            'http://localhost:5000/send-custom-email',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(email_data)
        )
        
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Email sent successfully!")
            print(f"   Message: {data.get('message', 'No message')}")
        elif response.status_code == 400:
            data = response.json()
            print(f"   ❌ Validation error: {data.get('message', 'No message')}")
        elif response.status_code == 500:
            data = response.json()
            print(f"   ❌ Server error: {data.get('message', 'No message')}")
            print("   💡 This usually means SMTP credentials are incorrect")
        else:
            print(f"   ❌ Unexpected status: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    print("🚀 TikTok Email System - Send Real Email")
    print("=" * 50)
    print("⚠️  BEFORE RUNNING:")
    print("   1. Edit this script with your REAL Gmail credentials")
    print("   2. Make sure you have a Gmail App Password (not regular password)")
    print("   3. Ensure the Flask app is running")
    print("=" * 50)
    
    send_real_email()
