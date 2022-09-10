# class lapchart

import json


class LapChart:

    def __init__(self, lap):
        
        self.lap = lap
        self.cars = []

    def __str__(self):
        return (self.lap + ":" + str(self.cars))
    
    def toJson(self)-> str:
        lapchart_str: str = ""
        lapchart_str += "\""+ self.lap +"\":"
        lapchart_str +=json.dumps(self.cars)
        return lapchart_str
