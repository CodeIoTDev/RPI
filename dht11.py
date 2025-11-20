import time
import board
import adafruit_dht
sensor = adafruit_dht.DHT11(board.D4) 

while True:
  try:
    t_c = sensor.temperature
    t_f = t_c * (9 / 5) + 32
    h = sensor.humidity
    print(“Temp(C) = ”,t_c , “Temp(F)= ”,t_f, “ Humidity = ”,h)
  
  except RuntimeError as error:
    print(error.args[0])
    time.sleep(2.0)
    Continue
    
  except Exception as error:
    sensor.exit()
    raise error
    
  time.sleep(3.0)
