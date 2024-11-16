'''
* DATA MONITORING & VISUALIZATION------------------
*  # Devices:
*     -> DHT22 sensor
*     -> ESP32
*  # Technologies:
*     -> Protocol: HTTP
*     -> Platform: ThingSpeak + Google Colab
*  # Activity:
*    -> Data transmission, monitoring and visualization
*       - Single chart on Google Colab
*
*   ANGAZA ELIMU&ALX - IOT SCHOOL: Cohort 1, 2024
* --------------------------------------------------
'''

'''
 Support libraries -------------------------------------------------------------
'''
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#---- ThingSpeak API details
CHANNEL_ID = ""
API_KEY = "" # Read API Key
THINGSPEAK_URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={API_KEY}&results=100"

# ---- Fetch data from ThingSpeak
response = requests.get(THINGSPEAK_URL)
data = response.json()

#---- Parse data
timestamps = [entry['created_at'] for entry in data['feeds']]
temperature = [float(entry['field1']) for entry in data['feeds']]
humidity = [float(entry['field2']) for entry in data['feeds']]

#---- Create DataFrame
df = pd.DataFrame({'Timestamp': timestamps, 'Temperature': temperature, 'Humidity': humidity})
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

#---- Plot data
plt.figure(figsize=(10,5))
plt.plot(df['Timestamp'], df['Temperature'], label='Temperature (°C)')
plt.plot(df['Timestamp'], df['Humidity'], label='Humidity (%)')
plt.xlabel('Timestamp')
plt.ylabel('Values')
plt.title('Temperature and Humidity Monitoring')
plt.legend()
plt.show()