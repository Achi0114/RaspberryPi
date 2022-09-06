from subprocess import check_output
from time import sleep
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27, auto_linebreaks=False)
lcd.clear()
def get_ip():
    cmd = "hostname -I | cut -d\' \' -f1"
    return check_output(cmd, shell=True).decode("utf-8").strip()
while True:
    lcd_line_1 =  get_ip()
    
    lcd.home()
    lcd.write_string(f'{lcd_line_1}')
    sleep(10)
