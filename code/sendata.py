import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)
i=0
# Send
while True:
	ser.write("Ping %s: Hello Arduino! This is Raspberry Pi!\n" % i)
	i=i+1
	time.sleep(1)


