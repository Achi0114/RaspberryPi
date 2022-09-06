from gpiozero import Buzzer
import max30100
from time import time, sleep
from urllib.request import urlopen
import sys

WRITE_API = "OV3PDVG90LV06799" # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)

buzzer = Buzzer(26)

mx30 = max30100.MAX30100()

SensorPrevSec = 0
SensorInterval = 2 # 2 seconds
ThingSpeakPrevSec = 0
ThingSpeakInterval = 20 # 20 seconds

try:
    while True:
        
        if time() - SensorPrevSec > SensorInterval:
            SensorPrevSec = time()
            
            
            hb = int(mx30.ir/100)
            spo2 = int(mx30.red/100)
            print(" HB = {:.2f}%/t SPO2 = {:.2f}C".format(hb,spo2))
        
        if time() - ThingSpeakPrevSec > ThingSpeakInterval:
            ThingSpeakPrevSec = time()
            
            thingspeakHttp = BASE_URL + "&field1={:.2f}&field2={:.2f}".format(hb,spo2)
            print(thingspeakHttp)
            
            conn = urlopen(thingspeakHttp)
            print("Response: {}".format(conn.read()))
            conn.close()
            
            buzzer.beep(0.05, 0.05, 1)
            sleep(1)
            
except KeyboardInterrupt:
    conn.close()