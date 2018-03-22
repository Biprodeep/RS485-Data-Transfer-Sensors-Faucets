import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
client= ModbusClient(method = "rtu", port="/dev/ttyAMA0",stopbits = 1, bytesize = 8, parity = 'E', baudrate= 9600)
while True:
    #data = client.read_input_registers(0x00, 4, unit=1)
    #print data.registers
    response = client.read_holding_registers(0x00,4,unit=1)
    print response.registers
