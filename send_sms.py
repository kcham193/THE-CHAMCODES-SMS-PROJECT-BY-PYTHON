from twilio.rest import Client

# Twilio Account SID and Auth Token
account_sid = 'XXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXX'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# List of phone numbers to send SMS to
phone_numbers = [
    '+25568.....',  # Add the phone numbers you want to send SMS to
    '+25561.....',
    '+25567.....',
    '+25562.....',
]

# Message to send
message = "Hello, this is CHAMBULILO , I welcome you to my chamcode sms program , get ready to see more updates. Thank you"

# Send SMS to each phone number
for number in phone_numbers:
    try:
        message = client.messages.create(
            to=number,
            from_="+.........",  # Your Twilio phone number
            body=message
        )
        print(f"Message sent to {number} with SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS to {number}: {str(e)}")
