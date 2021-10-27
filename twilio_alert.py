from twilio.rest import Client


def twilio(body):
    # enter your account sid, auth token, and phone number from Twilio:
    acct_sid = ''
    auth_token = ''
    twilio_number = ''
    
    # enter number to receive text notification:
    number_to_text = ''
    
    client = Client(acct_sid, auth_token)

    message = client.messages \
        .create(
        body=body,
        from_= twilio_number,
        to= number_to_text
    )

    return


