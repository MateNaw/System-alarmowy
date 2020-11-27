#!/usr/bin/python3
import signal
from time import *
import board
import digitalio
import busio
import RPi.GPIO as GPIO

import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from measurement import Measurement
from raspberry.device import Device


def send_data(data):
    print(f"Sending {data}")
def raise_alarm():
    print(f"Alarm")


def cleanExit():
    GPIO.cleanup()
    print('Exit!')


def loop(measurement, device):
    try:
        live = True
        count = 30
        while live:
            res = device.takeResults()
            measurement.save(**res)

            if res['alarm']:
                raise_alarm()

            if count:
                count -= 1
            else:
                send_data(measurement.get())
                count = 30
            sleep(1)
    except KeyboardInterrupt:
        cleanExit()

    finally:
        cleanExit()


def main():
    measurement = Measurement()
    device = Device()
    loop(measurement, device)
    cleanExit()


def signal_handler(signal, frame):
    print('Signal exit \n')
    cleanExit()
    raise SystemExit


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    main()

