# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
import twilio.twiml
import httplib2
import urllib
import json
import base64
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

# Twilio Constants
class TwilioSMSAPI:

	def __init__(self, account_sid, auth_token):
		self.account_sid = account_sid
		self.auth_token = auth_token

	def send(self, from_, to, text):
	    client = TwilioRestClient(self.account_sid, self.auth_token)
	    message = client.messages.create(to=to, from_=from_, body=text)

def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
