import urllib
import httplib2
import json
# import send_sms
from send_sms import send_SMS

GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"
BASE_URL = "https://www.googleapis.com"

def translate(text, language="es"):
    # configure url
    translate_url = "/language/translate/v2?"
    text_url = urllib.quote_plus(text)
    url = BASE_URL + translate_url + "key=" + GOOGLE_API_KEY + "&q=" + text_url + "&source=en" + "&target=" + language

    # send http request
    http = httplib2.Http()
    response, body = http.request(url,"GET")
    json_body = json.loads(body)
    return json_body['data']['translations'][0]['translatedText']

def translate_multiple(texts,language="es"):
    result = []
    for text in texts:
        result.append(translate(text,language))
    return result

def send_translated_text(text,to,from_,language="es"):
    translated_text = translate(text,language)
    send_SMS(to, from_, translated_text)


print translate("hello world")
print translate("hello world","de")
print translate_multiple(["hello","world","hello world"])
send_translated_text("hello world","+16178209484","+16174874127")
