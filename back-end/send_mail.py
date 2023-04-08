from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib,ssl
from email.mime.base import MIMEBase
from email import encoders

def send(mail):
    try:
        s = smtplib.SMTP('smtp.office365.com', 587)
    except Exception as e:
        s = smtplib.SMTP_SSL('smtp.office365.com', 465)
    s.ehlo()
    s.starttls()
    s.login("your_outlook_mail", "your_password")
    msg = MIMEMultipart()
    msg['From']='your_outlook_mail'
    msg['To']=mail
    msg['Subject']="Your Request for YouTube Channel Data"
    msg.attach(MIMEText("Greetings\n This is the report for the YouTube channel you have searched for.\n\n\n Regards,\nHARIKRISHNA R",'plain'))
    pdfname = 'output.pdf'
    binary_pdf = open('./Program outputs/'+pdfname, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((binary_pdf).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    msg.attach(payload)
    s.send_message(msg)


