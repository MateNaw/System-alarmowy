

class Measurement(object):
    def __init__(self):
        self.alarm = False
        self.temp = 0
        self.gas1 = 0
        self.gas2 = 0
        self.move = 0
        self.window1 = False
        self.window2 = False

    def save(self, alarm, temp, gas1, gas2, move, window1, window2):
        self.alarm = alarm
        self.temp = temp
        self.gas1 = gas1
        self.gas2 = gas2
        self.move = move
        self.window1 = window1
        self.window2 = window2

    def get(self):
        return {'alarm': self.alarm,
        'temp': self.temp ,
        'gas1': self.gas1 ,
        'gas2': self.gas2 ,
        'move': self.move ,
        'window1': self.window1 ,
        'window2': self.window2}
