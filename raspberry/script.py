#!/usr/bin/python3
import signal
from time import *
import RPi.GPIO as GPIO
from measurement import Measurement
from device import Device
import asyncio
import websockets
import requests
import json
import copy

def send_data(data):
    url = "http://127.0.0.1:8000/measurements"
    data1 = {'alarm': data['alarm'],
            'temperature': data['temp'],
            'gas': data['gas1'] ,
            'windows': data['window1'],
             'location': 1
             }
    data2 = {'alarm': data['alarm'],
            'temperature': data['temp'] ,
            'gas': data['gas2'] ,
            'windows': data['window2'],
            'location': 2
             }

    print(f"Sending {data}")
    try:
        res1 = requests.post(url, json.dumps(data1))
        print(data1)
        print(res1)
        res2 = requests.post(url, json.dumps(data2))
        print(res2)
    except requests.exceptions.RequestException as e:
        print(e)
    except Exception as o:
        print(o)


def cleanExit():
    GPIO.cleanup()
    print('Exit!')

class Alarm:
    def __init__(self):
        self.alarm = False

    def raise_alarm(self):
        print(f"Alarm")
        self.alarm = True


class Network:
    pass

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
                # network.send(measurement.get())
                send_data(measurement.get())

            if count:
                count -= 1
            else:
                # network.send(measurement.get())
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
    network = Network()

    # asyncio.get_event_loop().run_until_complete(command_receiver())

    # asyncio.get_event_loop().run_until_complete(network.command_receiver(alarm))
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

