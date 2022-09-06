import time
import max30100
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()
mx30 = max30100.MAX30100()
mx30.enable_spo2()
while 1:
    mx30.read_sensor()
    mx30.ir, mx30.red
    hb = int (mx30.ir/100)
    spo2 = int(mx30.red/100)
    spo2 =spo2-3;
    if mx30.ir != mx30.buffer_ir :
        print("HB:",hb);
    
    if mx30.red != mx30.buffer_red :
        print("SPO2:",spo2);
        lcd.text("HB :"+str(hb), 1)
        lcd.text("SPO2 :"+str(spo2), 2)
    time.sleep(1)#delay spo2
