import requests
token = "Basic ********"
apId = ""
oneURL = "https://onesignal.com/api/v1/players/csv_export?app_id="+apId
PARAMS = {
"Authorization": token,
"extra_fields":"location",
}

data = [
    {
        "extra_fields": ["country","notification_types","external_user_id", "location", "rooted", "ip", "country", "web_auth", "web_p256"]
        
    },
]

r = requests.post(url = oneURL, json = data, headers= PARAMS) 
  

a = r.json()

