import adafruit_dht
import board
import requests
import time

sensor = adafruit_dht.DHT11(board.D4)
pin = 4

channel_id = 'put_your_own_channel_id'
write_key = 'put_your_own_write_api_key'
thing_speak_url = f'https://api.thingspeak.com/update?api_key={write_key}'

while True:
  try:
  # Print the values to the serial port
  temperature_c = sensor.temperature
  temperature_f = temperature_c * (9 / 5) + 32
  humidity = sensor.humidity
  
  except RuntimeError as error:
    print(error.args[0])
    time.sleep(2.0)
    continue
    
  except Exception as error:
    sensor.exit()
    raise error

  if humidity is not None and temperature_c is not None and temperature_f is not None:
    print("Temp={0:0.1f}C, Temp={1:0.1f}F, Humidity={2:0.1f}%".format(temperature_c,
    temperature_f, humidity))
    
    # Send data to ThingSpeak
    response = requests.get(thing_speak_url, params={'field1': temperature_c, 'field2': humidity,
    'field3':temperature_f})
    
    print('Data sent to ThingSpeak:', response.status_code)
    
  else:
    print('Failed to retrieve data from the sensor')
    time.sleep(10)

