# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC82b030b3be5396a2db0df02c21435466"
auth_token = "d455d92b20493cb10e4be55829c02168"
def send_SMS(to,from_,body):
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=to, from_=from_, body=body)
