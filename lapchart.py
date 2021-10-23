# class lapchart

class LapChart:

    def __init__(self, lap):
        
        self.lap = lap
        self.cars = []

    def __str__(self):
        return (self.lap + ":" + str(self.cars))