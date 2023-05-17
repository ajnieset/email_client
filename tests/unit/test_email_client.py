from unittest import TestCase
from email_client import EmailClient


class TestClient(TestCase):
    def test_send(self):
        client = EmailClient()
        resp = client.send()

        assert resp == None