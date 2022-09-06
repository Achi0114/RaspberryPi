import max30100

import GY906 
from time import time, sleep
from urllib.request import urlopen
import sys
import urllib


mx30 = max30100.MAX30100()
mx30.enable_spo2()
sensor = GY906.GY906()
write_key = "OV3PDVG90LV06799"

def read_sensor():
    mx30.read_sensor()
    mx30.ir, mx30.red
    temperature = sensor.get_obj_temp()
    hb = int(mx30.ir/100)
    spo2 = int((mx30.red/100)-3)
    #print("mx30.ir = ", hb)
    #print("mx30.red = ", spo2)
    send_data_thingSpeak(temperature, hb, spo2)

def send_data_thingSpeak(temperature, hb, spo2):
    params = urllib.urlencode({'field1':hb, 'field2':temperature, 'field3':spo2})
    headers = {"Content-typZZe":"application/x-www-form-urlencoded", "accept":"text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com")
    try:
        conn.request('GET','/update',params,headers)
        res = conn.getresponse()
        print(res.status, res.reason)
        print(response.read())
        conn.close()
    except:
        print('con fail')
    


if __name__ == "__main__":
    while True:
        read_sensor()
    