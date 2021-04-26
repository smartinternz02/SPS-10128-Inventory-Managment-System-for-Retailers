import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_login(to_mail):
    message = Mail(from_email='santoshcse97@gmail.com',
                   to_emails=to_mail,
                   subject='SendGrid Twilio Testing Mail',
                   plain_text_content='This is a testing mail please do not reply to it.',
                   html_content='<strong>If you are receiving this then you are hacked.</strong>'
                   )

    try:
        # sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        res = sg.send(message)
        print('code : ', res.status_code)
        print('body : ', res.body)
        print('headers : ', res.headers)
    except Exception as e:
        print('err : ', e)


SENDGRID_API_KEY = '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'
mail = 'santoshcse97@gmail.com'


send_login(mail)
