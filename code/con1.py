import serial
#import sqlite3
import RPi.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(14,GPIO.IN)
#GPIO.setup(15,GPIO.OUT)
ser=serial.Serial()
ser.baudrate=9600
ser.port='/dev/ttyAMA0' 
ser.timeout=1
ser.close()
ser.open()
print ser.read(10000)
try:
 	while True:
           # GPIO.output(7,1) 
            #time.sleep(.5)
            #val=raw_input("enter something:") #send some value to ARDUINO
            #ser.write(val)
            #time.sleep(.5)
   		#GPIO.output(15,0) 
   		#time.sleep(.5)
   		#f=ser.read(ser.inWaiting())
		#print f
		line = ser.read(800)
		print line
except KeyboardInterrupt:
  	GPIO.cleanup()
GPIO.cleanup()
ser.close()


