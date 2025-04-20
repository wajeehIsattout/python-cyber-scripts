# Email Sender via Zoho SMTP

## Description
This script sends plain-text emails using Zoho's SMTP server. It's designed for simple email automation with login credentials and SMTP authentication.

## Features
- Sends emails using Zoho SMTP
- Error handling for SMTP authentication
- Easy to customize

## Requirements
- Python 3
- Zoho account with an app password
- `smtplib`, `email` (built-in)

## Usage
Update the following fields in the script:
```python
from_email = "your_zoho_email"
app_password = "your_app_password"
to_email = "recipient_email"
subject = "Your subject"
body = "Your message body"
```

Then run:
```bash
python email_sender.py
```

## Disclaimer
Do not misuse this script. Ensure you comply with all email service provider policies.
