# from google_translate_api import GoogleTranslateAPI
# from twilio_sms_api import TwilioSMSAPI
import os

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
GOOGLE_TRANSLATE_API_KEY = os.environ.get('GOOGLE_TRANSLATE_API_KEY')

# Main
def main():
    googleApi = GoogleTranslateAPI(GOOGLE_TRANSLATE_API_KEY)
    translated_message = googleApi.translate("This is Nick and Kojin", "th")
    print(translated_message)

    twilioApi = TwilioSMSAPI(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    twilioApi.send("+16174874127", '+16178209484',  translated_message)
    print("text_sent!")
