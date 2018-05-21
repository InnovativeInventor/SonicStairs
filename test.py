from tests.fakeserial import Serial
ser = Serial('/dev/ttyS1', 19200, timeout=1)
for i in range(100):
      # try:
      digit = ser.readline().decode('utf-8', errors='ignore')   # read a '\n' terminated line
      print(digit)
ser.close()
