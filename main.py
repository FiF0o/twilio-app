import os
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# Your Auth Token from twilio.com/console
auth_token  = os.environ["TWILIO_AUTH_TOKEN"]
from_number = os.environ["TWILIO_NUMBER_FROM"]
to_number = os.environ["TWILIO_NUMBER_TO"]


client = Client(account_sid, auth_token)

message = client.messages.create(
    to=to_number, 
    from_=from_number,
    body="Hello from Python!")

print(message.sid)