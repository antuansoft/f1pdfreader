# class PitStop

class PitStop:

    def __init__(self, number, driver, team, lap, stop, time, timeTotal):
        
        self.number = number
        self.driver = driver
        self.team = team
        self.lap = lap
        self.stop = stop
        self.time = time
        self.timeTotal = timeTotal

    def __str__(self):
        return (self.number + ":" + self.driver + ":" + 
                self.team  + ":" + self.lap + ":" + 
                self.stop  + ":" + self.time  + ":" + 
                self.timeTotal)