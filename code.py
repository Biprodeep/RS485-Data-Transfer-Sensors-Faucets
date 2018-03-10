import serial
import time

# Such parameters are required for the sensors so I use them
ser = serial.Serial(     
     port='/dev/ttyUSB0',
     baudrate = 9600,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.EIGHTBITS,
     timeout=1
     )
#i=0
while 1:
      print ser.readline()  # Reading the incoming data
      #ser.write("Ping %s: Hello Arduino! This is Raspberry Pi!\n" % i) # Writing this message to Serial 
      #i=i+1
      ser.write("Hello")
      #S = 'hello'
      #ser.write(bytes(b'hello\n'))

