import os
from twilio.rest import Client
import json


def load_env_vars():
    # Your Account SID from twilio.com/console
    twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    # Your Auth Token from twilio.com/console
    twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    twilio_from_number = os.environ["TWILIO_NUMBER_FROM"]
    return (twilio_account_sid, twilio_auth_token, twilio_from_number)

def get_users():
    # class to add/remove users
    users = []
    with open('config/users.json') as usersFile:
        users = json.load(usersFile)

    myself = os.environ.get('TWILIO_NUMBER_TO')
    # to remove later as this is
    users.append({'phone_number': myself, 'name': 'Me'})
    return users


class MessageClient(object):
    def __init__(self):
        (twilio_account_sid,
         twilio_auth_token,
         twilio_from_number) = load_env_vars()

        self.twilio_account_sid = twilio_account_sid
        self.twilio_auth_token = twilio_auth_token
        self.twilio_from_number = twilio_from_number

        self.twilio_client = Client(
            twilio_account_sid, twilio_auth_token)
           
    def send_msg(self, body, to):
        self.twilio_client.messages.create(
            to=to,
            from_=self.twilio_from_number,
            body=body)

        print 'msg: %s' % body


class TwilioNotification(object):
    def __init__(self):
        self.user_list = get_users()
        self.client = MessageClient()
        self.user_list = get_users()
    
    def message(self, message_to_send):
        for user in self.user_list:
            self.client.send_msg(str(message_to_send), user['phone_number'])


# init!
if __name__ == '__main__':
    NOTIFICATIONS = TwilioNotification().message('Hello!')
