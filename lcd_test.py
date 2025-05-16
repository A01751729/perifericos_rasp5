from RPLCD.i2c import CharLCD
from time import sleep

#objeto LCD
lcd=CharLCD(i2c_expander='PCF8574',address=0x27,port=1,cols=16,rows=2,
				charmap='A00',auto_linebreaks=True)

lcd.clear()
lcd.write_string("Hola mundo")
sleep(1)
lcd.clear()
lcd.write_string("maravilloso, ya escribe :)")
