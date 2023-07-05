import sendgrid
from sendgrid.helpers.mail import Email, To, Content, Mail

from email_client import EmailClient

class SendgridClient(EmailClient):
    def __init__(self, api_key: str, domain: str = "example.com"):
        self.client = sendgrid.SendGridAPIClient(api_key=api_key)
        self.domain = domain

    def send(self, to_email: str):
        from_email = Email("test@example.com")
        to_email = To(to_email)
        subject = "Sending with SendGrid is Fun"
        content = Content("text/plain", "and easy to do anywhere, even with Python")
        mail = Mail(from_email, to_email, subject, content)
        return self.client.client.mail.send.post(request_body=mail.get())
