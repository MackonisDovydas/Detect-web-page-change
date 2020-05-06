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

Template_URL = "https://is.vu.lt/pls/klevas/am$pd_reg_app.show?p_stud_id=219671&p_kalba_name=lt"

f = open("URL.txt", "r")
URL = f.read()
f.close()

f = open ("output1.txt", "r")
Out = f.read()
f.close()

numbers_to_message = [FIRST_NUMBER, SECOND_NUMBER]
for number in numbers_to_message:
    message = client.messages.create(
        body=Out,
        from_='+12565408905',
        to=number
    )
print(message.sid)
