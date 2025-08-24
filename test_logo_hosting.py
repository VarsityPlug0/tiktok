#!/usr/bin/env python3
"""
Test script for TikTok logo hosting
This script verifies that the logo is being served correctly
"""

import requests
import os

def test_logo_hosting():
    """Test if the TikTok logo is being hosted correctly"""
    
    base_url = "http://localhost:5000"
    logo_url = f"{base_url}/tiktok-logo"
    
    print("🔍 Testing TikTok Logo Hosting")
    print("=" * 40)
    print(f"Base URL: {base_url}")
    print(f"Logo URL: {logo_url}")
    print()
    
    try:
        # Test if Flask app is running
        print("📡 Testing Flask app connection...")
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            print("✅ Flask app is running")
        else:
            print(f"⚠️  Flask app responded with status: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Flask app is not running")
        print("   Start it with: python app.py")
        return False
    except Exception as e:
        print(f"❌ Error connecting to Flask app: {e}")
        return False
    
    try:
        # Test logo endpoint
        print("\n🖼️  Testing logo endpoint...")
        response = requests.get(logo_url, timeout=5)
        
        if response.status_code == 200:
            print("✅ Logo endpoint is working")
            print(f"   Content-Type: {response.headers.get('Content-Type', 'Unknown')}")
            print(f"   Content-Length: {response.headers.get('Content-Length', 'Unknown')} bytes")
            
            # Check if it's actually an image
            if 'image' in response.headers.get('Content-Type', ''):
                print("✅ Response is an image file")
            else:
                print("⚠️  Response might not be an image file")
                
        else:
            print(f"❌ Logo endpoint failed with status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing logo endpoint: {e}")
        return False
    
    # Check if logo file exists
    print("\n📁 Checking logo file...")
    logo_path = "static/logo.png"
    if os.path.exists(logo_path):
        file_size = os.path.getsize(logo_path)
        print(f"✅ Logo file exists: {logo_path}")
        print(f"   File size: {file_size} bytes")
    else:
        print(f"❌ Logo file not found: {logo_path}")
        return False
    
    print("\n🎉 Logo hosting test completed successfully!")
    print("\n📧 Next steps:")
    print("1. Check your email for the TikTok emails with the hosted logo")
    print("2. The logo should now appear as an image instead of text")
    print("3. When deploying, update BASE_URL in smtp.py to your domain")
    
    return True

if __name__ == "__main__":
    test_logo_hosting()
