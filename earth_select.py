import pandas as pd
import numpy as np

def file_data():
    data_main = pd.read_csv("Indian_earthquake_data.csv")
    # Check for NaN values and handle them
    data_main = data_main.dropna(subset=['Latitude', 'Longitude', 'Magnitude'])  # Drop rows with NaN in critical columns
    return data_main

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Changed to 6371 for more accurate Earth radius in kilometers
    lat1_rad = np.radians(lat1)
    lat2_rad = np.radians(lat2)
    lon1_rad = np.radians(lon1)
    lon2_rad = np.radians(lon2)
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = np.sin(dlat / 2)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c
    return distance

def QuerySelector(lat, long):
    data_store = file_data()
    data_store['distance_km'] = data_store.apply(lambda row: haversine(lat, long, row['Latitude'], row['Longitude']), axis=1)
    print(data_store['distance_km'])
    within_5km = data_store[data_store['distance_km'] <= 100]
    print(within_5km)
    return within_5km

def avg_mag(query):
    if not query.empty:  # Check if the query DataFrame is not empty
        return float(query['Magnitude'].mean())  # Use column name for clarity
    return float('nan')  # Return NaN if the query is empty

def main(lat,long):
    store = QuerySelector(lat, long)
    average_magnitude = avg_mag(store)
    return average_magnitude


main()