from gpizero import Buzzer
import max30100
import GY906
from ime import time,sleep
from urllb.request import urlopen
import sys

WRITE_API = "OV3PDVG90LV06799" # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)

buzzer = Buzzer(26)

mx30 = max30100.max30100()
sensor = GY906.GY906()
mx30.enable_spo2

SensorPrevSec = 0
SensorInterval = 2 # 2 seconds
ThingSpeakPrevSec = 0
ThingSpeakInterval = 20 # 20 seconds

try:
    while True:
         
            mx30.read_sensor()

	    mx30.ir, mx30.red

	    temperature = sensor.get_obj_temp()
	    hb = int(mx30.ir/100)
	    spo2 = int(mx30.red/100)
            spo2 = spo2-3:
	    print("Pulse:",hb);
	    print("SPO2:",spo2);
	    print("Temp:",temperature);
        
        if time() – ThingSpeakPrevSec > ThingSpeakInterval:
            ThingSpeakPrevSec = time()
            
            thingspeakHttp = BASE_URL + "&field1&field2&field3={:.2f}".format(hb, temperature,spo2)
            print(thingspeakHttp)
            
            conn = urlopen(thingspeakHttp)
            print("Response: {}".format(conn.read()))
            conn.close()
            
            buzzer.beep(0.05, 0.05, 1)
            sleep(1)
            
except KeyboardInterrupt:
    conn.close()
