# class team

class Team:

    def __init__(self, name, car, engine):
        
        self.name = name
        self.car = car
        self.engine = engine

    def __str__(self):
        return (self.name + ":" + self.car + ":" + self.engine)