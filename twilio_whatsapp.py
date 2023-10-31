from twilio.rest import Client

def send_whatsapp_message(account_sid, auth_token, from_number, to_number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=f'whatsapp:{from_number}',
        body=message,
        to=f'whatsapp:{to_number}'
    )

    # log the message id
    with open('reports/message_ids.txt', 'a') as f:
        f.write(str(message.sid) + '\n')
