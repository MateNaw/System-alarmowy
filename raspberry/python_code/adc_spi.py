#!/usr/bin/python3
from time import *
import board
import digitalio
import busio
import RPi.GPIO as GPIO

import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
 
print("Hello blinka!")
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")
print("done!")

#BCM mode
GPIO.setmode(GPIO.BCM)
PIR_PIN = 4

GPIO.setup(PIR_PIN, GPIO.IN)

cs = digitalio.DigitalInOut(board.CE0)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

try:
    while(True):
        analog_raw = chan.value
        analog_vol = chan.voltage
        print(f"anlog value: {analog_raw} analog voltage: {analog_vol}")
        val = GPIO.input(PIR_PIN)
        if val:
            print("!!!!wykryto ruch     !!!")
        else:
            print("nie wykryto ruchu")
        sleep(0.2)

finally:
    GPIO.cleanup()
        
        


