# class drivers

class Driver:

    def __init__(self, number, name, country, team, car, engine):
        self.name = name
        self.country = country
        self.team = team
        self.number = number
        self.car = car
        self.engine = engine

    def __str__(self):
        return (self.name + ":" + self.country + ":" + self.team)