from SonicStairs.staircase import sonic_averages
# import test_decode
from SonicStairs.fakeserial import Serial
import secrets
import numpy
import random

class Args:
    def __init__():
        self._verbose = False

    def verbose(self):
        return self._verbose

def test_sonicavg():

    rand_rounds = secrets.randbelow(19)+1
    input_array = []

    for i in range(rand_rounds):
        input_array.append(int(numpy.round(random.gauss(60, 2.5),0)))

    correct_median = int(numpy.median(input_array))

    write_num = int(secrets.randbelow(120))
    arduino = Serial('/dev/ttyS1', 38400, timeout=1, data = input_array)

    tested_median = sonic_averages(Args, arduino, avg=len(input_array))


    assert abs(int(tested_median) - int(correct_median)) <= 2
