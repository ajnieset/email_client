from providers.sendgrid import SendgridClient
class EmailClientFactory:
    def createClient(self, client_type: str, api_token: str, domain: str = 'example.com'):
        if client_type.lower() == 'sendgrid':
            return SendgridClient(api_token, domain)
