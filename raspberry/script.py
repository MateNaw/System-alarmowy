#!/usr/bin/python3
import signal
from time import *
import RPi.GPIO as GPIO
from measurement import Measurement
from device import Device
from network import Network, ws_url
import asyncio
import websockets
from .network import Network, ws_url

def send_data(data):
    print(f"Sending {data}")


def cleanExit():
    GPIO.cleanup()
    print('Exit!')


class Alarm:
    def __init__(self):
        self.alarm = False

    def raise_alarm(self):
        print(f"Alarm")
        self.alarm = True


alarm = Alarm()


def loop(measurement, device, network):
    try:
        live = True
        count = 30
        while live:
            res = device.takeResults()
            measurement.save(**res)

            if res['alarm']:
                alarm.raise_alarm()
                network.send(measurement.get())

            if count:
                count -= 1
            else:
                network.send(measurement.get())
                count = 30
            sleep(1)
    except KeyboardInterrupt:
        cleanExit()

    finally:
        cleanExit()


def main():
    measurement = Measurement()
    device = Device()
    network = Network()

    asyncio.get_event_loop().run_until_complete(network.command_receiver(alarm))
    loop(measurement, device, network)
    cleanExit()


def signal_handler(signal, frame):
    print('Signal exit \n')
    cleanExit()
    raise SystemExit


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    main()

