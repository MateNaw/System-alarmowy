#!/usr/bin/python3
 	
from time import *
import board
import digitalio
import busio
import RPi.GPIO as GPIO
 
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

try:
    while(True):
        val = GPIO.input(PIR_PIN)
        if val:
            print("!!!!wykryto ruch     !!!")
        else:
            print("nie wykryto ruchu")
        sleep(0.2)

finally:
    GPIO.cleanup()
        
        


