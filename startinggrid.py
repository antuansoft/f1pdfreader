import json

class StartingGrid:

    def __init__(self, position, number, driver,
                 nationality, scuderia, laps,
                 time, gap2leader, interval2next,
                 kph, besttime, bestlap):
        
        self.position = position
        self.number = number
        self.driver = driver
        self.nationality = nationality
        self.scuderia = scuderia
        self.laps = laps
        self.gap2leader = gap2leader
        self.time = time
        self.interval2next = interval2next
        self.kph = kph
        self.besttime = besttime
        self.bestlap = bestlap

    def __str__(self):
        return (self.position +":" +self.number + ":" + self.driver + 
                ":" + self.nationality + ":" +  self.scuderia + ":" + 
                self.laps + ":" + self.time + ":" + self.gap2leader + 
                ":" + self.interval2next + ":" + self.kph + ":" + 
                self.besttime + ":" + self.bestlap)

    def toJson(self):
       return json.dumps(self.__dict__)