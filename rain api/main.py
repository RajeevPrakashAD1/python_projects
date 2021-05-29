import requests
from twilio.rest import Client
import os

account_sid = 'AC1af442ccdf6292de022ad06e85a44197'
auth_token = 'd8746b90c4e3abd98101afa0303c74b6'


website = "https://api.openweathermap.org/data/2.5/onecall"
apikey  = "8bb8ff531bac8a392ae6091c7393aa27"
parameters = {
    "lat": 25.377120,
    "lon": 85.148557,
    "appid": apikey,
    "exclude":"minutely,daily,current,alerts"}

response = requests.get(website,params=parameters)
response.raise_for_status()
weather_data = response.json()

list_of_hourly_weather = weather_data["hourly"]
for i in range(12):
    hour_weather = list_of_hourly_weather[i]
    id = hour_weather["weather"][0]["id"]
    print(id)
    if id<700:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"bring umberealla   Today may rain.  jan hit me jari Rajeev",
            from_='+13366562476',
            to='+917903578628'
        )



        print(message.status)
        break
    else:
        continue