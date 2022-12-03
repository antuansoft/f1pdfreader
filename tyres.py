# class Strint

import json


class Stint:

    def __init__(self, driver, tyre, laps, stintNum):
        
        self.driver = driver
        self.tyre = tyre
        self.laps = laps
        self.stintNum = stintNum

    def __str__(self):
        return (self.driver + ":" + str(self.tyre) + ":" + str(self.laps) + ":" + str(self.stintNum))

    def toJson(self):
       return json.dumps(self.__dict__)