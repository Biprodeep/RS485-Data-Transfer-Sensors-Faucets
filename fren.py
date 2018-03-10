#!/usr/bin/env python

import subprocess
import time
import RPi.GPIO as GPIO
import urllib
import httplib
import minimalmodbus
import time
import serial

#diagnostic
#print(minimalmodbus._getDiagnosticString())
instrument = minimalmodbus.Instrument('/dev/serial0',1) #port name , slave address(in decimal)
instrument.serial.baudrate 					= 9600
instrument.serial.bytesize 					= 8
instrument.serial.parity 					= serial.PARITY_NONE
instrument.serial.stopbits 					= 1
instrument.serial.timeout 					= 1                		# secondes
instrument.mode							= minimalmodbus.MODE_RTU 	# rtu ou ascii // MODE_ASCII ou MODE_RTU
instrument.debug 						= False
instrument.serial.xonxoff					= True
instrument.serial.rtscts					= False
instrument.serial.dsrdtr					= False
#minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL	= True
##
instrument2 = minimalmodbus.Instrument('/dev/serial0',2) #port name , slave address(in decimal)
instrument2.serial.baudrate 					= 9600
instrument2.serial.bytesize 					= 8
instrument2.serial.parity 					= serial.PARITY_NONE
instrument2.serial.stopbits 					= 1
instrument2.serial.timeout 					= 1                		# secondes
instrument2.mode						= minimalmodbus.MODE_RTU 	# rtu ou ascii // MODE_ASCII ou MODE_RTU
instrument2.debug 						= False
instrument2.serial.xonxoff					= True
instrument2.serial.rtscts					= False
instrument2.serial.dsrdtr					= False
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL			= True
## read temperature
temperature=instrument.read_register(0,1)#register number, number of decimals
print ("temp1:",temperature)

temperature2=instrument2.read_register(0,1)#register number, number of decimals
print ("temp2:",temperature2)




