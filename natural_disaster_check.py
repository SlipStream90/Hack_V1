import requests
from datetime import datetime

# Define the coordinates and parameters
latitude = 30.3295605
longitude = 76.4127819
radius_km = 100  # Radius in kilometers
start_time = "2024-11-14"
end_time = "2024-11-15"

# Define the URL for the API request
url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&latitude={latitude}&longitude={longitude}&maxradiuskm={radius_km}&starttime={start_time}&endtime={end_time}"

# Send the request
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()

    if 'features' in data and data['features']:
        for earthquake in data['features']:
            properties = earthquake['properties']
            time = datetime.utcfromtimestamp(properties['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Magnitude: {properties['mag']}")
            print(f"Place: {properties['place']}")
            print(f"Time: {time}")
            print(f"Status: {properties['status']}")
            print("-" * 40)
    else:
        print("No earthquakes found in the specified region and time frame.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")

except ValueError as e:
    print(f"Error processing JSON data: {e}")
