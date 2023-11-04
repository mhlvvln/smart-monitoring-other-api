import os
from json import loads

import requests


def call(phone_number: str):
    url = "https://api.twilio.com/2010-04-01/Accounts/AC58c68c896af3ca2ef876a3c3122dfe37/Calls.json"
    payload = {
        "Url": "http://demo.twilio.com/docs/voice.xml",
        "To": phone_number,
        "From": "+13345649071"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    auth = ("AC58c68c896af3ca2ef876a3c3122dfe37", os.environ['call_token'])
    response = requests.post(url, data=payload, headers=headers, auth=auth, verify=False)
    return loads(response.text)