import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

# GPIO Setup
LED_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Callback when a message is received
def on_message(client, userdata, message):
  payload = message.payload.decode()
  print(f"Received messagae: {payload}")
  if payload == "ON":
  GPIO.output(LED_PIN, GPIO.HIGH)
  time.sleep(5)
  elif payload == "OFF":
  GPIO.output(LED_PIN, GPIO.LOW)
  time.sleep(5)

# MQTT Setup
broker_url = "test.mosquitto.org" # Eclipse Mosquitto public broker
broker_port = 1883 # Default unencrypted MQTT port
topic = "test/led_control"
client = mqtt.Client()

client.connect(broker_url, broker_port)
client.subscribe(topic)
client.on_message = on_message

# Start MQTT client loop
client.loop_start()

try:
  while True:
    pass # Keep the script running
  except KeyboardInterrupt:
    print("Experiment stopped")
  finally:
    GPIO.cleanup()
    client.loop_stop()
