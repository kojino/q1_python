from flask import Flask, request
from twilio import twiml
import os
# from .google_translate_api import GoogleTranslateAPI
import google_translate_api
# import GoogleTranslateAPI
# from twilio_sms_api import TwilioSMSAPI
GOOGLE_TRANSLATE_API_KEY = os.environ.get('GOOGLE_TRANSLATE_API_KEY')
app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    print type(message_body)
    googleApi = google_translate_api.GoogleTranslateAPI(GOOGLE_TRANSLATE_API_KEY)
    translated_message = googleApi.translate(str(message_body), "es")

    resp = twiml.Response()
    resp.message(translated_message)
    return str(resp)

if __name__ == '__main__':
    app.run()
