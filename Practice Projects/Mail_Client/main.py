import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 587)

server.ehlo()
server.starttls()
with open("credentials.txt", 'r') as file:
    sender_email = file.readline()[:-1]
    sender_password = file.readline()[:-1]
    receiver_email = file.readline()

    server.login(sender_email, sender_password)

msg = MIMEMultipart()
msg["From"] = "Rixx"
msg["To"] = receiver_email
msg["Subject"] = "Testing"

with open("message.txt", 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

image_att = "Alibi_L.jpg"
attachment = open(image_att, 'rb')
p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename={image_att}")
msg.attach(p)

text = msg.as_string()
server.sendmail(sender_email, receiver_email, text)