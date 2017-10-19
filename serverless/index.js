'use latest';
import twilio from 'twilio';

module.exports = function(context, callback) {
    // POST a json object with at least the following properties.
    const { to_number, from_number } = context.data;
    console.log(context)
    console.log(callback)
    const { 
        TWILIO_ACCOUNT_SID, 
        TWILIO_AUTH_TOKEN, 
        TWILIO_NUMBER_FROM, 
        TWILIO_NUMBER_TO } = context.secrets;
    const client = new twilio.RestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN);
    
    client.messages.create({
        to: TWILIO_NUMBER_TO,
        from: TWILIO_NUMBER_FROM,
        body: 'manve un vier marv vulvini'
    }, (err, message) => {
        if (err) return callback(err);
        callback(null, message);
        }
    );
}