# Python code to illustrate Sending mail with attachments 
# from your Gmail account 
# Credits - all documents/scripts I could find online.

# libraries to be imported 

import smtplib, os 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "sender's mail"
toaddr = "reciever's mail"

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject 
msg['Subject'] = "Testing multiple attachments"

# string to store the body of the mail 
body = "Body_of_the_mail"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 

attachments = ["list containing address of all attachemts to be sent"]
for f in attachments:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(f,"rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)
    
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, "your_password") 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 


