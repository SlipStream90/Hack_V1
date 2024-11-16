import requests
import datetime
import json
import csv
from flask import flash

api_key = "D5FAPVXX5KEXSZHWHVFQ6YHHT"
city = "Patiala"
start_date = "2024-11-8"
end_date = "2024-11-15"
BaseUrl = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/38.9697,-77.385?key={api_key}"
def get_weather(lat,lon):
    BaseUrl = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}?key={api_key}"
    Response = requests.get(BaseUrl)
    if Response.status_code == 200:
        data = Response.json()
        return data
    else:
        flash("Invalid Location","Error")

