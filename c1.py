import serial
import RPi.GPIO as GPIO
import time

port = serial.Serial("/dev/ttyAMA0", baudrate =9600, timeout = 1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

while True:
	rcv =port.readline()
	port.write(rcv)

port.close()
