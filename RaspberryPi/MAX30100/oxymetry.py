
import time
import max30100
import GY906 
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()
mx30 = max30100.MAX30100()
sensor = GY906.GY906()
mx30.set_mode(max30100.MODE_SPO2)

mx30.set_interrupt(max30100.INTERUPFIFO)
from gpiozero import Button
interrupt = Buton(16)
interrupt.when_activated = mx30.read_sensor

mx30.buffer_red

while Ture:
    print(mx30.buffer_red[-10])
    
    