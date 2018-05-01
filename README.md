## SonicStairs
A musical staircase powered by an Arduino and ultrasonic sensor

## Setting up
Requirements:
- Arduino
- *nix-based OS with a USB port (Ubuntu, MacOS, etc.)
- Ultrasonic sensor (tested with HC-SR04, but any NewPing-compatible sensor works)

Steps:
1. Connect your Arduino to the ultrasonic sensor with the trigger pin connected to pin 7, the echo pin connected to 8, and VCC/ground connected to 5v and GND.
2. Upload `arduino_ultrasound/arduino_ultrasound.ino` to the Arduino
3. Run `staircase.py` with python3.

# TODO
- Removing testing/old code and get everything demonstration-ready.
