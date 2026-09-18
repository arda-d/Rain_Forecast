import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

# Load from ".env"
load_dotenv()

# Get API and personal informations from ".env"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

twilio_number = os.getenv("TWILIO_NUMBER")
my_number = os.getenv("MY_PHONE_NUMBER")

#Set Params
weather_params = {
    "lat": 41.042381,
    "lon": 28.912149,
    "appid": api_key,
    "cnt": 4
}

will_rain = False

#Threw API a request and convert the data into json
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

#Check if there is raining 12 hours ahead
for hour_data in data["list"]:
    condition_id = hour_data["weather"][0]["id"]
    if int(condition_id) < 700:
        will_rain = True
#If there is, sent SMS
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's raining today!",
        from_=twilio_number,
        to=my_number
    )
    print(message.status)
