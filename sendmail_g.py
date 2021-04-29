from smtplib import SMTP

email = 'sk189436234@gmail.com'
password = ''

from_mail = email

def sendmail(subject, message, to_mail):
    s = SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email, password)
    message = f'Subject : {subject} \n\n {message}'
    s.sendmail(from_mail, to_mail, message)
    s.quit()

