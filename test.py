from fakeserial import Serial
ser = Serial('/dev/ttyS1', 19200, timeout=1, data=[3, 0, 1, 4, 7, 16, 31, 64, 127])
line = ser.readline()   # read a '\n' terminated line
print(line )
ser.close()
