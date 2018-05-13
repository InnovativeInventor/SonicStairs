from SonicStairs.staircase import decode
from SonicStairs.tests.fakeserial import Serial
import secrets

def test_decode():
    write_num = int(secrets.randbelow(120)+1)
    arduino = Serial('/dev/ttyS1', 38400, timeout=1, data = str(str(write_num)+'\n')) # .encode('utf-8'))
    measurement = decode(arduino)
    assert measurement == write_num
    return measurement
