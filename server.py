from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from main import TwilioNotification

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/notify', methods=['GET', 'POST'])
def send_notifs():
    notif = TwilioNotification().message('notif is sent')
    return str(notif)

@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    resp.message('Reply is sent')
    return str(resp)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True)
