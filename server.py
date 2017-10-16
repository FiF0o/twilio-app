from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    resp.message('Reply is sent')
    return str(resp)

if __name__ == 'server':
    app.run(debug=True)
