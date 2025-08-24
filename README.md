# TikTok Phishing Simulation

A security awareness training application that simulates a TikTok login page to educate users about phishing attacks.

## ⚠️ Disclaimer

This application is designed for **AUTHORIZED SECURITY AWARENESS TRAINING ONLY**. It should only be used by organizations with proper authorization to conduct phishing simulations. Never use this tool for malicious purposes or without explicit permission.

## 🚀 Features

- **Realistic TikTok Login Interface**: Professional-looking login page that closely resembles the official TikTok login
- **Dual Authentication Methods**: Email/password and phone verification code login options
- **Admin Dashboard**: Real-time monitoring of user interactions and captured data
- **Comprehensive Logging**: Detailed logs for training analysis and reporting
- **Responsive Design**: Works on desktop and mobile devices
- **Security Features**: No actual credential harvesting, safe simulation environment

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: In-memory storage (for demo purposes)
- **Deployment**: Render (cloud platform)

## 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/VarsityPlug0/tiktok.git
   cd tiktok
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - TikTok Login Page: http://localhost:5000/tiktok-login
   - Admin Dashboard: http://localhost:5000/admin

### Production Deployment on Render

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add Render deployment configuration"
   git push origin main
   ```

2. **Deploy on Render**
   - Go to [render.com](https://render.com) and sign up/login
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Select the `tiktok` repository
   - Render will automatically detect the Python environment
   - Click "Create Web Service"

3. **Environment Variables** (Optional)
   - `PORT`: Automatically set by Render
   - `PYTHON_VERSION`: Set to 3.9.16

## 📁 Project Structure

```
tiktok/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment configuration
├── Procfile             # Alternative deployment method
├── static/              # Static assets
│   └── logo.png        # TikTok logo
├── templates/           # HTML templates
│   ├── tiktok_login.html  # Login page
│   └── admin.html         # Admin dashboard
└── README.md            # This file
```

## 🔧 Configuration

### Development Mode
- Debug mode enabled
- Detailed logging
- Auto-reload on code changes

### Production Mode
- Debug mode disabled
- Optimized for performance
- Environment-based port configuration

## 📊 Admin Dashboard Features

- **Real-time Statistics**: Total submissions, email logins, phone logins, codes sent
- **Live Updates**: Auto-refresh every 3 seconds
- **Data Export**: Download submissions as JSON
- **Data Management**: Clear all submissions
- **Detailed Logs**: IP addresses, user agents, timestamps

## 🚨 Security Considerations

- **No Real Data**: All data is stored in memory and not persisted
- **Local Access Only**: Admin dashboard should be restricted in production
- **HTTPS Required**: Always use HTTPS in production environments
- **Access Control**: Implement proper authentication for admin access

## 📝 Usage Guidelines

1. **Training Setup**: Configure the application for your organization's needs
2. **User Education**: Inform participants about the simulation beforehand
3. **Data Analysis**: Use the admin dashboard to analyze user responses
4. **Follow-up Training**: Provide additional security awareness training based on results

## 🤝 Contributing

This project is for educational purposes. If you find bugs or have suggestions for improvements, please create an issue or submit a pull request.

## 📄 License

This project is intended for educational and authorized security training purposes only. Please ensure you have proper authorization before using this tool.

## 🆘 Support

For issues related to:
- **Deployment**: Check Render's documentation
- **Application**: Review the Flask logs
- **Security**: Consult with your organization's security team

## 🔗 Useful Links

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Render Documentation](https://render.com/docs)
- [Phishing Awareness Resources](https://www.phishing.org/)
