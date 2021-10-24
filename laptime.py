# class LapTime

class LapTime:

    def __init__(self, name:str, number:str, lap:int, time:int):
        
        self.name = name
        self.number = number
        self.lap = lap
        self.time = time

    def __str__(self):
        return (self.name + ":" + str(self.number) + ":" + str(self.lap) + ":" + str(self.time))