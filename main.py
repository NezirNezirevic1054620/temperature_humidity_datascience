from sense_hat import SenseHat
import requests
import time

# ThingSpeak API endpoint and API key
WRITE_API_KEY = 'XVNEO552DCOSJOW9'
WRITE_API_ENDPOINT = 'https://api.thingspeak.com/update'

TEMPERATURE_FIELD_NUMBER = 1
HUMIDITY_FIELD_NUMBER = 2

# Initialize SenseHAT
sense = SenseHat()

# Main loop
while True:
    # Read temperature and humidity from SenseHAT
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()

    # Print temperature and humidity to console
    print('Temperature: {:.2f} C'.format(temperature))
    print('Humidity: {:.2f} %'.format(humidity))

    # Post temperature and humidity to ThingSpeak channel
    payload = {'api_key': WRITE_API_KEY, 'field{}'.format(TEMPERATURE_FIELD_NUMBER): temperature, 'field{}'.format(HUMIDITY_FIELD_NUMBER): humidity}
    response = requests.post(WRITE_API_ENDPOINT, data=payload)

    # Wait for 15 seconds before taking the next measurement
    time.sleep(15)
