#importing required modules and classes

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders

# credentials to access server using smtp
apple_mail = "mail"
apple_pass = "pass"

#function to attach files
def attach_file(filename):
    part_file = open(filename,'rb')
    part = MIMEBase('application','octect-stream')
    part.set_payload(open(filename,"rb").open())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= "%s"' % os.path.basename(filename))
    part_file.close()
    return part

#fuction to embedded image body 
def attach_image(imagename,image_cid):
    image_file = open(imagename, 'rb')
    # create the attached file part which is a MIMEBase object.
    image_part = MIMEImage(image_file.read(), name='image_name')
    image_part.add_header('Content-ID', '<'+str(image_cid)+'>')  
    image_part.add_header("Content-Disposition", "in-line", filename='%s' % os.path.basename(imagename))
    image_part.add_header('X-Attachment-Id', 'str(%s)' % image_cid)
    image_file.close()
    return image_part   

#function to send secure mail using smtp, input msg, email, password, reciever's mail, mail server and port
def send_mail(msg, user_mail, user_pass, to_list,mail_server,mail_server_port):
    mailServer = smtplib.SMTP(mail_server,port=mail_server_port)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    try:
        mailServer.login(user_mail,user_pass)
        mailServer.sendmail(user_mail, to_list, msg.as_string())
        mailServer.sendmail(user_mail,to_list,'Imbedded Image Job successfull')
    except:
        mailServer.sendmail(user_mail,to_list,'Imbedded Image Job Failed')
    finally:
        mailServer.quit()


# create the message content object which is a plain text data.
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

# create plain MIMEText object
msg_content = MIMEText(text, 'plain', 'utf-8')

# define image_cid's for image placement in html
image_cid = 1

# define image_files
imagename = []

# define to_list - recievers mail address
to_list = []

#create the message content object which has html data
email_content = 'Content of the html object <br/> <img src="cid:1"><br/>'
msg_html_content = MIMEText(email_content, 'html', 'utf-8')

# create the MIMEMultipart object which contains both email content and attached files.
msg = MIMEMultipart("alternative")
msg['From'] = apple_mail
msg['To'] = apple_mail
msg['Subject'] = Header("Mail Subject", 'utf-8').encode()

# attach objects to the email.
msg.attach(msg_content)
msg.attach(attach_image("image_address",image_cid))
msg.attach(msg_html_content)
msg.attach(attach_file("image_address"))
# send the mail 
send_mail(msg, apple_mail,apple_pass, apple_mail,"smtp.gmail.com",587)

#job done
