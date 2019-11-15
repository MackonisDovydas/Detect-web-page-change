from twilio.rest import Client
import netrc

HOST = 'Sms_send'
secrets = netrc.netrc()
ACCOUNT_SID, account, AUTH_TOKEN = secrets.authenticators(HOST)

HOST = 'Numbers'
secrets = netrc.netrc()
FIRST_NUMBER, account, SECOND_NUMBER = secrets.authenticators(HOST)

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

numbers_to_message = [FIRST_NUMBER,SECOND_NUMBER]
for number in numbers_to_message:
    message=client.messages.create(
        body = 'Something changed in "PD pasirinkimas"',
        from_ = '+19073187609',
        to = number
    )
    print(message.sid)