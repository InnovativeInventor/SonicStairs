import serial
import sys
import os
import pty
from SonicStairs.staircase import connect_serial

def test_serial():
    # Opening up the master and slave serial ports
    ports = ()
    ports = pty.openpty()
    print(ports[1])

    test_name = os.ttyname(ports[0])
    arduino_name = os.ttyname(ports[1])

    # Seting up the serial ports
    test_ser = serial.Serial(test_name,9600)
    arduino = serial.Serial(arduino_name,9600,timeout=1)

    print(arduino.port)
    simulated_arduino = connect_serial(arduino.port)
    test_ser.write(bytes('30', 'utf8'))
    parse = simulated_arduino.read(1)
    # read_serial= parse.decode('utf-8', errors='ignore')
    # print(read_serial)
    #
    # test_ser.close()
    # arduino.close()

    assert read_serial == 30
