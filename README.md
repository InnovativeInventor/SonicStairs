## SonicStairs
A musical staircase powered by an Arduino and ultrasonic sensor

## Setting up
Requirements:
- Arduino
- nix-based OS with a USB port (Ubuntu, MacOS, etc.)
- Ultrasonic sensor (tested with HC-SR04, but any NewPing-compatible sensor should work)

Steps:
1. Connect your Arduino to the ultrasonic sensor with the trigger pin connected to pin 7, the echo pin connected to 8, and VCC/ground connected to 5v and GND.
2. Upload `arduino_ultrasound/arduino_ultrasound.ino` to the Arduino
3. Plug in the Arduino and run `staircase.py` with python3.

## Dependencies
Python 3 dependencies (most are installable through pip):
- numpy
- pyserial (not serial!)
- simpleaudio
    - On Debian, make sure to follow the instructions [here](https://simpleaudio.readthedocs.io/en/latest/installation.html#linux-dependencies) to install simpleaudio
    - On Fedora, install:
        - redhat-rpm-config
        - alsa-lib-devel
        - python3-devel
- dataset
- argparse
- datafreeze

Stuff needed for testing and developing:
- Python 3.6
- dummyserial
- pyenv

Arduino dependencies:
- [NewPing](http://simpleaudio.readthedocs.io/en/latest/installation.html#linux-dependencies)

Open up an issue if you find any more that you have to install that I haven't listed here.

# TODO
- Removing testing/old code and get everything demonstration-ready.
- Docker for portability?
