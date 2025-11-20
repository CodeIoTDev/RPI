#LED

import RPi.GPIO as GPIO
import time
import requests

channel_id = 'put_your_own'
read_key = 'put_your_own_read_api_key'
thing_speak_url =f'put_your_own_read_api_url'


GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

try:
  while True:
    response = requests.get(thing_speak_url)
    data = response.json()
    
    latest_entry = data['feeds'][0]
    label_value = int(latest_entry['field1'])
  
    if label_value == 1:
      GPIO.output(LED_PIN, GPIO.HIGH)
    else:
      GPIO.output(LED_PIN, GPIO.LOW)
    
    time.sleep(1)
    
except KeyboardInterrupt:
  GPIO.cleanup()







# Tower Pro SG90

import RPi.GPIO as GPIO
import time
import requests

# ThingSpeak channel and API details
channel_id = 'put_your_own'
read_key = 'put_your_own'
thing_speak_url = f'put_your_own'

# Setup GPIO pin for the servo motor
SERVO_PIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set up PWM for servo control
servo = GPIO.PWM(SERVO_PIN, 50) # 50Hz frequency
servo.start(0) # Start PWM with 0% duty cycle

def set_servo_angle(angle):
  duty = angle / 18 + 2 # Convert angle to duty cycle
  GPIO.output(SERVO_PIN, True)
  servo.ChangeDutyCycle(duty)
  time.sleep(0.5)
  GPIO.output(SERVO_PIN, False)
  servo.ChangeDutyCycle(0)

try:
  while True:
    response = requests.get(thing_speak_url)
    data = response.json()
    latest_entry = data['feeds'][0]
    label_value = int(latest_entry['field1'])
    
    if label_value == 1:
      set_servo_angle(90) # Move the servo to 90 degrees
    else:
      set_servo_angle(0) # Move the servo to 0 degrees
    
    time.sleep(1)
  
  except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
