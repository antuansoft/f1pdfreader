# class lapchart

import json
from tokenize import Number


class LapChart:

    def __init__(self, lap):
        
        self.lap = lap
        self.cars = []

    def __str__(self):
        return (self.lap + ":" + str(self.cars))
    
    def toJson(self)-> str:
        lapchart_str: str = ""
        lapchart_str += "\""+ self.changeLapToNumber(self.lap) +"\":"
        lapchart_str +=json.dumps(self.cars)
        return lapchart_str


    def changeLapToNumber(self,text)->str:
        if (text == "Grid"):
            return "0"
        elif (text.find("Lap") > -1 ):
            return text[4:]
        else:
            return text
