# TikTok Email System

This system allows you to send professional TikTok-style security notification emails that closely resemble the official TikTok security alerts you've seen.

## 🎯 Features

### Email Templates
- **Security Alert**: New device login detected notification
- **Verification Required**: Account verification needed notification

### Design Features
- **Dark Theme**: Matches TikTok's modern aesthetic
- **TikTok Branding**: Uses official TikTok colors (cyan/red gradient)
- **Responsive Design**: Optimized for both desktop and mobile
- **Professional Styling**: Clean, modern interface with proper typography

## 🚀 Quick Start

### 1. Test the Email System
```bash
# Run the test script to send sample emails
python test_tiktok_emails.py
```

### 2. Use the Web Interface
1. Start your Flask app: `python app.py`
2. Visit: `http://localhost:5000/email-tester`
3. Fill in the form and send emails

### 3. Use the API Directly
```python
from smtp import send_tiktok_security_alert, send_tiktok_verification_required

# Send security alert
send_tiktok_security_alert(
    recipient_email="user@example.com",
    alert_type="new_device",
    username="username"
)

# Send verification email
send_tiktok_verification_required(
    recipient_email="user@example.com",
    username="username"
)
```

## 📧 Email Types

### Security Alert Email
- **Subject**: "TikTok: Security Alert - New Device Login Detected"
- **Content**: 
  - Device information (randomized)
  - Location (randomized)
  - Timestamp
  - Security recommendations
  - TikTok branding

### Verification Required Email
- **Subject**: "TikTok: Account Verification Required - Immediate Action Needed"
- **Content**:
  - Urgent banner
  - Verification button
  - Security notice
  - High-priority styling

## 🔧 Configuration

### SMTP Settings
The system uses Gmail SMTP. Update these in `smtp.py`:

```python
smtp_server = "smtp.gmail.com"
port = 587
username = "your-email@gmail.com"
password = "your-app-password"  # Use App Password if 2FA enabled
```

### Gmail Setup
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
3. Use the generated password in the script

## 🌐 Web Interface

### Email Tester Page
- **URL**: `/email-tester`
- **Features**:
  - Visual email type selection
  - Form for recipient details
  - Real-time email preview
  - Success/error feedback
  - Mobile-responsive design

### API Endpoint
- **URL**: `/send-tiktok-email`
- **Method**: POST
- **Body**:
  ```json
  {
    "email": "recipient@example.com",
    "type": "security_alert",
    "username": "tiktok_username"
  }
  ```

## 📱 Email Design Details

### Color Scheme
- **Primary**: TikTok cyan (#00f2ea)
- **Secondary**: TikTok red (#ff0050)
- **Background**: Dark theme (#121212, #1e1e1e)
- **Text**: White (#ffffff) and light gray (#e0e0e0)

### Typography
- **Font**: System fonts (Apple, Windows, Android)
- **Sizes**: Responsive from 14px to 48px
- **Weights**: Regular (400) and Semi-bold (600)

### Layout
- **Container**: 600px max-width, centered
- **Spacing**: Consistent 20px-40px margins
- **Borders**: 8px-16px radius for modern look
- **Shadows**: Subtle depth with rgba shadows

## 🧪 Testing

### Test Script
The `test_tiktok_emails.py` script provides:
- Automated email sending
- Success/failure reporting
- Feature demonstration
- Configuration validation

### Sample Output
```
🎵 TikTok Email System Test
========================================

📧 Test 1: Sending TikTok Security Alert...
   - Type: New device login detected
   - Includes: Device info, location, timestamp
   - Style: Dark theme with TikTok branding
   ✅ Security alert sent successfully!

📧 Test 2: Sending TikTok Verification Email...
   - Type: Account verification required
   - Includes: Urgent banner, verification button
   - Style: High-priority design with red accents
   ✅ Verification email sent successfully!

========================================
📊 Test Results Summary:
   Security Alert: ✅ PASS
   Verification Email: ✅ PASS

🎉 All tests passed! TikTok emails are working correctly.
```

## 🔒 Security Features

### Randomization
- **Devices**: Random selection from popular devices
- **Locations**: Random South African provinces
- **Timestamps**: Current time in SAST format

### Professional Appearance
- **Branding**: Authentic TikTok visual identity
- **Content**: Realistic security notification text
- **Layout**: Professional email design standards

## 📁 File Structure

```
TikTok/
├── smtp.py                    # Main email functionality
├── test_tiktok_emails.py     # Test script
├── app.py                    # Flask web application
├── templates/
│   └── tiktok_email_tester.html  # Web interface
└── TIKTOK_EMAIL_README.md    # This file
```

## 🚨 Troubleshooting

### Common Issues

1. **SMTP Authentication Error**
   - Verify Gmail credentials
   - Check if 2FA is enabled
   - Use App Password, not regular password

2. **Email Not Sending**
   - Check internet connection
   - Verify SMTP server settings
   - Check Gmail account status

3. **Template Rendering Issues**
   - Ensure all template files exist
   - Check Flask app configuration
   - Verify route definitions

### Debug Mode
Enable debug logging in `app.py`:
```python
app.run(host='0.0.0.0', port=port, debug=True)
```

## 📞 Support

For issues or questions:
1. Check the logs in your Flask application
2. Verify SMTP configuration
3. Test with the provided test script
4. Review the web interface for visual feedback

## 🔄 Updates

The system is designed to be easily extensible:
- Add new email templates in `smtp.py`
- Modify styling in the HTML templates
- Update the web interface in `tiktok_email_tester.html`
- Extend the Flask API in `app.py`

---

**Note**: This system is designed for legitimate security awareness and testing purposes. Always ensure compliance with applicable laws and regulations when sending emails.
