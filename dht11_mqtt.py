import time
import board
import adafruit_dht
import paho.mqtt.client as mqtt

# -----------------------------
# MQTT Setup
# -----------------------------
broker_url = "test.mosquitto.org"
broker_port = 1883
topic = "test/dht11_data"

client = mqtt.Client()

print("Connecting to MQTT Broker...")
client.connect(broker_url, broker_port)
client.loop_start()
print("Connected!")

# -----------------------------
# DHT11 Sensor Setup
# -----------------------------
sensor = adafruit_dht.DHT11(board.D4)   # GPIO4 (Pin 7)

# -----------------------------
# Main Loop
# -----------------------------
while True:
    try:
        temp_c = sensor.temperature
        hum = sensor.humidity

        if temp_c is not None and hum is not None:
            temp_f = temp_c * 9/5 + 32
            message = f"Temperature(C): {temp_c}, Temperature(F): {temp_f:.1f}, Humidity: {hum}"

            print("Publishing:", message)
            client.publish(topic, message)

        else:
            print("Sensor read failed")

    except RuntimeError as e:
        print("DHT11 Reading Error:", e.args[0])
        time.sleep(2)

    except Exception as e:
        sensor.exit()
        print("Critical error:", e)
        break

    time.sleep(3)
