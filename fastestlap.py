# class fasttestlap

class FastestLap:

    def __init__(self, position, number, driver, team, time,lap, gap):
        self.position = position
        self.number = number
        self.driver = driver
        self.team = team
        self.time = time
        self.lap = lap
        self.gap = gap

    def __str__(self):
        return (self.position + ":" + self.number + ":" + self.team + ":" + self.time+ ":" + 
                self.lap+ ":" + self.gap)