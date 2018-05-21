# Modified by Innovative Inventor from http://www.science.smith.edu/dftwiki/index.php/PySerial_Simulator
# D. Thiebaut
# A very crude simulator for PySerial assuming it
# is emulating an Arduino.
import collections
import sys
import itertools

# a Serial class emulator
class Serial:

    ## init(): the constructor.  Many of the arguments have default values
    # and can be skipped when calling the constructor.
    def __init__( self, port='/dev/tty3', baudrate = 38400, timeout=1,
                  bytesize = 8, parity = 'N', stopbits = 1, xonxoff=0,
                  rtscts = 0, data = None, groups = 5):
        self.name     = port
        self.port     = port
        self.timeout  = timeout
        self.parity   = parity
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits
        self.xonxoff  = xonxoff
        self.rtscts   = rtscts
        self.groups   = groups
        self._isOpen  = True
        self._receivedData = ""

        self.q, self.r, self.t, self.k, self.n, self.l = 1, 0, 1, 1, 3, 3 # test

        if isinstance(data, str) or isinstance(data, int):
            self._data = str(data)
        else:
            self._data = data


    ## isOpen()
    # returns True if the port to the Arduino is open.  False otherwise
    def isOpen( self ):
        return self._isOpen

    ## open()
    # opens the port
    def open( self ):
        self._isOpen = True

    ## close()
    # closes the port
    def close( self ):
        self._isOpen = False

    ## write()
    # writes a string of characters to the Arduino
    def write( self, string ):
        # print( 'Arduino got: "' + string + '"' ) # debug
        self._receivedData += string

    ## read()
    # reads n characters from the fake Arduino. Actually n characters
    # are read from the string _data and returned to the caller.
    def read( self, n=1 ):
        s = self._data[0:n]
        self._data = self._data[n:]
        #print( "read: now self._data = ", self._data )
        return s

    ## readline()
    # reads characters from the fake Arduino until a \n is found.
    def readline(self):
        if not self._data:
            digit = str(self.pi_generator())
            return digit.encode('utf-8')
        elif not isinstance(self._data, str) or isinstance(self._data, int):
            if len(self._data) is not 0:
                return_data = str(self._data[0])
                del self._data[0]
            else:
                raise EOFError("End of input list")
                exit(1)
            # print(self._data) # debug
            return return_data.encode('utf-8')
        else:
            returnIndex = self._data.index("\n")
            # returnIndex = self._data.index(str("\n").encode('utf-8'))
            if returnIndex != -1:
                s = self._data[0:returnIndex+1]
                self._data = self._data[returnIndex+1:]
                return s.rstrip().encode('utf-8')
            else:
                return ""

    def reset_input_buffer():
        pass

    def pi_generator(self): # techincally not a generator
        group = ""
        for i in range(self.groups):
            group+=str(next(self.pi_gibbons()))

        return group

    def pi_gibbons(self, base=10):
        """Gibbons spigot generator of digits of pi in given base."""
        while True:
            if 4 * self.q + self.r - self.t < self.n * self.t:
                digit = self.n
                self.q, self.r, self.t, self.k, self.n, self.l = (base * self.q, base * (self.r - self.n * self.t), self.t, self.k,
                                    (base * (3 * self.q + self.r)) // self.t - base * self.n, self.l)
                yield digit
            else:
                self.q, self.r, self.t, self.k, self.n, self.l = (self.q * self.k, (2 * self.q + self.r) * self.l, self.t * self.l, self.k + 1,
                                    (self.q * (7 * self.k + 2) + self.r * self.l) // (self.t * self.l), self.l + 2)


        # while True:
        #     if 4 * q + r - t < n * t:
        #         yield n
        #         q, r, t, k, n, l = (base * q, base * (r - n * t), t, k,
        #                             (base * (3 * q + r)) // t - base * n, l)
        #     else:
        #         q, r, t, k, n, l = (q * k, (2 * q + r) * l, t * l, k + 1,
        #                             (q * (7 * k + 2) + r * l) // (t * l), l + 2)

    ## __str__()
    # returns a string representation of the serial class
    def __str__( self ):
        return  "Serial<id=0xa81c10, open=%s>( port='%s', baudrate=%d," \
               % ( str(self.isOpen), self.port, self.baudrate ) \
               + " bytesize=%d, parity='%s', stopbits=%d, xonxoff=%d, rtscts=%d)"\
               % ( self.bytesize, self.parity, self.stopbits, self.xonxoff,
                   self.rtscts )
