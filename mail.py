import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email(to_address, subject, body):
    from_address ="your_email@example.com"
    password = "your_password"
    message = MIMEMultipart()
    message["From"] = from_address
    message["To"] = to_address
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    session = smtplib.SMTP("smtp.gmail.com", 587)  
    session.starttls()  
    session.login(from_address, password)  
    text = message.as_string()
    session.sendmail(from_address, to_address, text)
    session.quit()
    print(f"Mail sent to {to_address}.")
