# class DriverStanding

class DriverStanding:

    position:int
    driver:str
    points:int    

    def __init__(self, position, driver, points):
        
        self.position = position
        self.driver = driver
        self.points = points

    def __str__(self):
        return (self.position + ":" + self.driver + ":" + self.points)