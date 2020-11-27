#!/usr/bin/python3
import signal
from time import *
import RPi.GPIO as GPIO
from measurement import Measurement
from device import Device


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

