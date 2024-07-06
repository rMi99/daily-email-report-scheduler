import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_report(email_details):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = email_details['smtp_username']
    msg['To'] = email_details['to_email']
    msg['Subject'] = email_details['subject']
    msg.attach(MIMEText(email_details['body'], 'plain'))
    
    # Send the email
    try:
        server = smtplib.SMTP(email_details['smtp_server'], email_details['smtp_port'])
        server.starttls()
        server.login(email_details['smtp_username'], email_details['smtp_password'])
        server.sendmail(email_details['smtp_username'], email_details['to_email'], msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def schedule_email(email_details):
    # Schedule the email to be sent daily at a specific time
    schedule.every().day.at("08:00").do(send_email_report, email_details)

    # Start the scheduler
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    import threading
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
