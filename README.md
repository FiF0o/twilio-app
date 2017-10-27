# QUICK PYTHON APP USING API MESSAGING FROM TWILIO<br><br>


## Pre-requisites
-----------------


### Deps
install deps: `pip install -r requirements.txt`.

### Twilio configuration
Add your own `account_sid`, `auth_token`, `from` (given by twilio when creating a phone number for your servie), `to` numbers to your environment after your registered for a Twilio account.<br>
It can be found in your [console](https://www.twilio.com/console.<br>
your `to` phone number (used to create a twilio account) must be [verified](https://www.twilio.com/console/phone-numbers/incoming).<br>

### Environment
Create your own virtual environment: `virtualenv .venv`.<br>
Activate your environment: `source .venv/bin/activate`.<br>
Add your environment variables to a `.env` file.<br>
Source environment variables for your project before running it: `source .env` or use `autoenv`.<br>


## Running the project
----------------------

### Twilio Messaging configuration
Run webserver with [Twilio SMS Webhook](https://www.twilio.com/console/phone-numbers/).<br>
If you don't want to host your webserver you can use ngrok locally to add your webhook endpoint to the Messaging service `/sms` route on the webserver `PORT:5000`.<br>

### Available commands

Use the `Makefile` to `serve` and run your project.

### Javascript and serverless endpoint
`./serverless` directory holds a script using [webtask.io](https://webtask.io/) using Twilio API.<br>
Alternatively, you can use [stdlib](https://stdlib.com/).<br><br>

After `cd` the directory, you can install the deps `npm i`, and run the npm `deploy` task to update your script on webtask.io.<br>
You will need to provide a `.secrets` file with your API variables: `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_NUMBER_FROM`, `TWILIO_NUMBER_TO` or source them in your environment.