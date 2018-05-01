#!/usr/bin/env python3

# Made by Innovative Inventor at https://github.com/innovativeinventor.
# If you like this code, star it on GitHub!
# Contributions are always welcome.

# MIT License
# Copyright (c) 2018 InnovativeInventor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import serial
import wave
import simpleaudio as sa
import numpy # Maybe get rid of this
import argparse
import time

def main():
	global arduino
	# try:
	# 	arduino = Serial("/dev/ttyUSB0",9600)
	# 	arduino.open()
	#
	# except: #SerialException
	# 	print("Arduino not detected, please connect it to this computer")
	# 	exit(1)

	try:
		while True:
			distance_array = []

			for i in range(5):
				distance = int(numpy.round(decode(),-1))
				if not distance == 0:
					distance_array.append(distance)

			avg_distance = max(set(distance_array), key=distance_array.count)

			# avg_distance = decode()

			print(avg_distance)

			try:
				prev_obj = music(avg_distance,prev_obj)
			except:
				prev_obj = music(avg_distance)

	except KeyboardInterrupt:
		arduino.close() # Should close the serial port (hopefully)

def connect_serial():
	global args
	port = args.port

	try:
		arduino = serial.Serial(port,9600)
		# arduino.open()
		# arduino = serial.Serial(port,9600)

	except:
		try:
			arduino.close()
			arduino = serial.Serial(port,9600)
		except:
			print("Please plug in the Arduino and specify the correct serial port.")
			exit(1)

	return arduino

def decode():
	global arduino

	# try:
	# 	arduino.open()
	#
	# except:
	# 	arduino.close()
	# 	arduino.open()

	arduino.reset_input_buffer()

	serial = arduino.readline()
	read_serial= serial.decode('utf-8', errors='ignore')
	# arduino.close()

	try:
		measurement = int(read_serial.rstrip())
	except ValueError:
		measurement = decode()

	if measurement == 0:
		measurement = decode()

	return measurement

def music(avg_distance, prev_obj=0):
	nearest_ten = numpy.round(avg_distance,-1)
	wav_file = str(nearest_ten) + ".0.wav" # Example: 10.0.wav or 20.0.wav

	# Just for testing purposes
	if nearest_ten<120:
		try:
			wave_obj = sa.WaveObject.from_wave_file(wav_file)

			# Stops playing music right before music is played again
			if not prev_obj==0:
				prev_obj.stop()

			play_obj = wave_obj.play()
			time.sleep(0.5)
		    # wave_obj = sa.WaveObject.from_wave_file("test.wav")

		except FileNotFoundError:
		    print("Error: Music not found")
		return play_obj

def arguments():
	parser = argparse.ArgumentParser(description='A program to generate music from a ultrasonic sensor')
	parser.add_argument("--port", "-p", type=str, default="/dev/ttyUSB0", help="Specifies serial port to use (default = /dev/ttyUSB0)")
	args = parser.parse_args()
	return args

if __name__ == "__main__":
	args = arguments()
	arduino = connect_serial()
	main()
