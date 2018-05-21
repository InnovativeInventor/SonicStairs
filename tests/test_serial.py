# # from dummyserial import Serial as FakeSerial
# # import dummyserial
#
# import sys
# import os
# import secrets
# import pty
# import SonicStairs.fakeserial
# from SonicStairs.staircase import connect_serial
# from SonicStairs.staircase import decode
# import time
# import mock
#
# # def test_serial():
# #     from serial import Serial
# #
# #     # Opening up the master and slave serial ports
# #     ports = ()
# #     ports = os.openpty()
# #
# #     test_name = os.ttyname(ports[0])
# #     arduino_name = os.ttyname(ports[1])
# #
# #     print()
# #     print(test_name)
# #     print(arduino_name)
# #
# #     # Seting up the serial ports
# #     test_ser = Serial(test_name, timeout=1)
# #
# #     # test_ser.write(bytes('30', 'utf8'))
# #     write_bytes = "30\n".encode()
# #     test_ser.write(write_bytes)
# #
# #
# #     simulated_arduino = connect_serial(arduino_name, bdrate='')
# #
# #
# #     # simulated_arduino.write(30)
# #     print(1)
# #     simulated_arduino.write(write_bytes)
# #     print(2)
# #     parse = simulated_arduino.readline()
# #     print(3)
# #
# #     simulated_arduino.close()
# #     test_ser.close()
# #
# #     read_serial= parse.decode('utf-8', errors='ignore')
# #     print(read_serial)
# #
# #     test_ser.close()
# #     arduino.close()
# #
# #     assert read_serial == 30
# #
# #
#
# # serial_port = str("/dev/" + secrets.token_hex(5))
# # write_num = str(secrets.randbelow(120))
# # write_num_b = write_num.encode('utf-8')
# #
# # read_num = str(secrets.randbelow(120))
# # read_num_b = read_num.encode('utf-8')
# # ds_instance = dummyserial.Serial(
# #     port=serial_port,
# #     baudrate=9600,
# #     ds_responses={write_num_b: read_num_b}
# # )
# #
# # def test_serial_dummy():
# #     # Serial = FakeSerial.read
# #
# #     ds_instance.write(write_num_b)
# #
# #     parse = test_connect_serial(serial_port, ds_instance)
# #
# #     read_serial= parse.decode('utf-8', errors='ignore')
# #     print(read_serial)
# #
# #     simulated_arduino.close()
# #     ds_instance.close()
# #     assert read_serial == read_num
# #
# # @mock.patch('Serial()', side_effect=ds_instance.read())
# # def test_connect_serial(serial_port, ds_instance):
# #     simulated_arduino = connect_serial(serial_port)+'\n')
# #     parse = simulated_arduino.readline()
#
# @mock.patch('Serial()', side_effect=SonicStairs.fakeserial.Serial())
# def test_serial_dummy():
#     parse = connect_serial('/dev/ttyS1', 38400)
#
#     read_serial= parse.decode('utf-8', errors='ignore')
#     print(read_serial)
#
#     simulated_arduino.close()
#     ds_instance.close()
#     assert read_serial == read_num
