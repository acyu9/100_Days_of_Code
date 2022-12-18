from twilio.rest import Client

TWILIO_STD = "account_SID"
TWILIO_AUTH_TOKEN = "auth_token"
TWILIO_VIRTUAL_NUMBER = "virtual"
TWILIO_VERIFIED_NUMBER = "verified"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self):
        self.client = Client(TWILIO_STD, TWILIO_AUTH_TOKEN)
    
    def send_sms(self, message):
        message = self.client.messages.create(
            body = message,
            from_ = TWILIO_VIRTUAL_NUMBER,
            to = TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent
        print(message.sid)