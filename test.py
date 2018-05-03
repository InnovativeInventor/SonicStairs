import os
import pty
import serial

master, slave = pty.openpty()
ser_name = os.ttyname(slave)

ser = serial.Serial(ser_name)

# To Write to the device
ser.write(b'Your text')

# To read from the device
os.read(master,1000)

print(master)
print(ser.port)
print(slave)
