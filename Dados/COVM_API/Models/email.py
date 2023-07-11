from typing import Any, overload
import smtplib
from email.message import EmailMessage
from dataaccess.db import *
from Models.baseClass import *

class Email(BaseClass):
    assunto  = ''
    body     = ''
    to       = '' 
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds)  
        self.assunto   = ''
        self.body      = ''  
        self.body      = ''  
    
def sendEmail(email: Email):
    assunto = email.assunto
    body = email.body
    to = email.to
    email_address = 'eric.hausman.m@gmail.com'
    email_password = 'xdwbsvcwrqrpnufo'

    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = email_address
    msg['To'] = to
    password = email_password
    msg.add_header('Content-type', 'text/html')
    msg.set_content(body)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    return {"msg":"Email enviado"}