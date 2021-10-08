# class drivers

class Driver:

    def __init__(self, name, country, team):
        self.name = name
        self.country = country
        self.team = team

    def __str__(self):
        return (self.name + ":" + self.country + ":" + self.team)