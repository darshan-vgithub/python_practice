from twilio.rest import Client

# Twilio credentials
account_sid = 'AC5b42698430cc32bd335f87938cdf8f6f'  # Replace with your Twilio SID
auth_token = 'ae4f6487b489db49f75f247d7cd1ca69'    # Replace with your Twilio Auth Token
client = Client(account_sid, auth_token)

# Send WhatsApp message
message = client.messages.create(
    from_='whatsapp:+14155238886',         # Twilio Sandbox WhatsApp Number
    body='Hello! This is a WhatsApp message sent using Python Twilio API!',
    to='whatsapp:+919886849137'          
)

print('Message SID:', message.sid)
