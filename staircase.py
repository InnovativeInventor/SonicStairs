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

from serial import Serial
import wave
import simpleaudio as sa
import numpy # Maybe get rid of this
import argparse
import time
import dataset
import datafreeze
from os import environ
from statistics import median
import ast

## Todo:
# Remove args.avg


def main(args, arduino):

	db = dataset.connect()
	table = db['logs']

	try:
		while True:
			(sensor, avg_distance) = sonic_averages(args, arduino)

			# Really hacky solution, needs to change
			try:
				prev_obj = music(sensor,args,avg_distance,prev_obj)
			except:
				prev_obj = music(sensor,args,avg_distance)

			table.insert(dict(time=int(time.time()), sensor = sensor, value=avg_distance))
			datafreeze.freeze(db['logs'].all(), format='csv', filename='logs.csv')


	except KeyboardInterrupt: # Closes the port and updates the database if there is a keyboard interrupt
		if args.save:
			datafreeze.freeze(db['logs'].all(), format='csv', filename='logs.csv')

		arduino.close() # Should close the serial port (hopefully)

def connect_serial(port='/dev/ttyUSB0', bdrate = 9600):

	try:
		arduino = Serial(port,bdrate)
		# arduino.open()
		# arduino = serial.Serial(port,9600)

	except:
		try:
			arduino = Serial(port)

		except:
			try:
				arduino.close()
				arduino = Serial(port,bdrate)
			except:
				print("Please plug in the Arduino and specify the correct serial port.")
				exit(1)

	return arduino

def sonic_averages(args,arduino): # Averages distances
	distance_array = []

	(sensor, distance) = decode(arduino)

	output = [sensor]
	if distance == 0:
		(sensor, distance) = sonic_averages(args,arduino)

	rounded_distance = int(numpy.round(distance,-1))

	output.append(rounded_distance)

	if args.verbose:
		print(str(sensor) + "," + str(rounded_distance))

	return output

def decode(arduino):

	# try:
	# 	arduino.open()
	#
	# except:
	# 	arduino.close()
	# 	arduino.open()

	arduino.reset_input_buffer

	serial = arduino.readline()
	read_serial= serial.decode('utf-8', errors='ignore')
	# arduino.close()

	try:
		measurement = ast.literal_eval(read_serial.rstrip())
	except ValueError:
		measurement = decode(arduino)

	if measurement == 0:
		measurement = decode(arduino)

	return measurement

def music(sensor, args, avg_distance, prev_obj=0):

	note_length = args.width/args.keywidth
	note = int(sensor)+round(int(avg_distance)/note_length)
	wav_file = str(note) + ".wav" # Example: 1.wav or 2.wav

	if args.verbose:
		print("File looking for:" + wav_file)
		
	# Just for testing purposes
	if True:
		try:
			wave_obj = sa.WaveObject.from_wave_file(wav_file)

			# Stops playing music right before music is played again
			if not prev_obj==0:
				prev_obj.stop()

			play_obj = wave_obj.play()
			time.sleep(0.5)
		    # wave_obj = sa.WaveObject.from_wave_file("test.wav")
			return play_obj

		except FileNotFoundError:
			print("Error: Music file " + wav_file +" not found")
			return prev_obj


def arguments():
	parser = argparse.ArgumentParser(description='A program to generate music from a ultrasonic sensor')
	parser.add_argument("--port", "-p", type=str, default="/dev/ttyUSB0", help="Specifies serial port to use (default = /dev/ttyUSB0)")
	parser.add_argument("--avg", "-a", type=int, default=5, help="Specifies amount of readings to average (default = 5)")
	parser.add_argument("--save", "-s", help="Exports logs to logs.csv when finished", action='store_true')
	parser.add_argument("--verbose", "-v", help="Verbose option", action='store_true')
	parser.add_argument("--keywidth", "-kw", type=int, default=2, help="Specifies key width of staircase (default = 2)")
	parser.add_argument("--keyheight", "-kh", type=int, default=5, help="Specifies key height of staircase (default = 5)")
	parser.add_argument("--width", "-w", type=int, default=400, help="Specifies width of staircase in cm")
	parser.add_argument("--scale", "-sc", type=int, default=7, help="Specifies scale length")
	args = parser.parse_args()
	return args

if __name__ == "__main__":
	args = arguments()
	arduino = connect_serial()
	main(args, arduino)
