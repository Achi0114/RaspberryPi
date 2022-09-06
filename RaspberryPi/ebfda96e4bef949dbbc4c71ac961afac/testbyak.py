
import time
import max30100
import GY906 
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import thingspeak
import time
import max30100
lcd = LCD()
mx30 = max30100.MAX30100()
sensor = GY906.GY906()
mx30.enable_spo2()

write_key = "OV3PDVG90LV06799"
mx30 = max30100.MAX30100()

def measure(channel):
    mx30.read_sensor()
    
    mx30.ir, mx30.red
    
    temperature = sensor.get_obj_temp()
    hb = int(mx30.ir/100)
    spo2 = int(mx30.red/100)
    spo2 = spo2-3;
    if mx30.ir != mx30.buffer_ir :
        print("HB:",hb);
    if mx30.red != mx30.buffer_red :
        print("SPO2:",spo2);
        print("Temp:",temperature);
        lcd.text("HB:"+str(hb)+ " " + "SPO2:"+str(spo2),1)
        lcd.text("Temp:"+str(temperature),2)
        response = channel.update({'field1':hb, 'field2' : spo2})
    time.sleep(3)
    
if __name__== "__main__":
    channel = thingspeak.Channel(1844411, write_key)
    while True:
        measure(channel)
        time.sleep(3)

