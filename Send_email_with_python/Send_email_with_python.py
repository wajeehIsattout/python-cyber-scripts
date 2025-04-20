import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_via_zoho(to_email, subject, body, from_email, app_password):
    try:
        # Set up Zoho Mail SMTP server details (we are using zoho but you can use any other service you want)
        smtp_server = "smtp.zoho.com"
        smtp_port = 587

        # Create the email headers and content
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(from_email, app_password)  # Login using app password

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

        # Close the connection
        server.quit()
    except smtplib.SMTPAuthenticationError as e:
        print("Failed to authenticate with the SMTP server. Check your email or app password.")
        print(f"Error: {e}")
    except Exception as e:
        print("An error occurred while sending the email.")
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your Zoho email address and app password 
    from_email = "hacker@zohomail.com"
    app_password = "python"

    # Replace with recipient's email, subject, and body
    to_email = "hacker@zohomail.com"
    subject = "Test Email from Zoho"
    body = "Hello, this is a test email sent using Zoho SMTP."

    send_email_via_zoho(to_email, subject, body, from_email, app_password)
