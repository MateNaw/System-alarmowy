import random

import board
import digitalio
import busio
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp


class Device(object):

    def __init__(self):
        print("Hello blinka!")
        self.pin = digitalio.DigitalInOut(board.D4)
        print("Digital IO ok!")
        self.i2c = busio.I2C(board.SCL, board.SDA)
        print("I2C ok!")
        self.spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
        print("SPI ok!")
        print("done!")
        # BCM mode
        GPIO.setmode(GPIO.BCM)
        self.PIR_PIN = 4
        self.WINDOW1 = 5
        self.WINDOW2 = 6
        self.ALARM = 19
        self.RESET = 20

        GPIO.setup(self.PIR_PIN, GPIO.IN)
        GPIO.setup(self.WINDOW1, GPIO.IN)
        GPIO.setup(self.WINDOW2, GPIO.IN)
        GPIO.setup(self.RESET, GPIO.IN)
        GPIO.setup(self.ALARM, GPIO.OUT)
        cs = digitalio.DigitalInOut(board.CE1)
        self.mcp = MCP.MCP3008(self.spi, cs)
        self.chan1 = AnalogIn(self.mcp, MCP.P0)
        self.chan2 = AnalogIn(self.mcp, MCP.P1)
        self.chan8 = AnalogIn(self.mcp, MCP.P7)
        self.MAX_GAS1 = 40000
        self.MAX_GAS2 = 45000
        self.alarm = False

        if not 0x18 in self.i2c.scan():
            print("Didn't find MCP9808")
            raise SystemExit

    def meas_temp(self):
        self.i2c.writeto(0x18, bytes([0x05]), stop=False)
        result = bytearray(2)
        self.i2c.readfrom_into(0x18, result)
        return temp_c(result)

    def takeResults(self):
        gas1 = self.chan1.value
        gas2 = self.chan2.value
        gas1 = 25000+random.randint(-10000, 10000)
        gas2 = 25000+ random.randint(-10000, 10000)
        pot = self.chan8.value

        move = GPIO.input(self.PIR_PIN)
        wind1 = GPIO.input(self.WINDOW1)
        wind2 = GPIO.input(self.WINDOW2)
        reset = GPIO.input(self.RESET)
        temp = self.meas_temp()
        print(f"temp: {temp}")

        window1 = False if wind1 else True
        window2 = False if wind2 else True
        print(f"window1: {window1} window2: {window2} move: {move}")
        if not reset:
            gas1+=15000
            gas2+=15000

        alarm = self.alarm
        if window2 or window1 or move:
            alarm = True
        if gas1 > self.MAX_GAS1 or gas2 > self.MAX_GAS2:
            alarm = True

        if reset:
            alarm = False

        print(f"==============anlog gas1: {gas1} analog gas2: {gas2} pot {pot}")
        GPIO.output(self.ALARM, alarm)

        return {
            'alarm': alarm,
            'temp': temp,
            'gas1': gas1,
            'gas2': gas2,
            'move': move,
            'window1': window1,
            'window2': window2
        }


