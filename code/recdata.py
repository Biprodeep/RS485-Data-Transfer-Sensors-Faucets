import serial
serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
#serialport.write("My string output to serial port")
response = serial.readline()
print response
