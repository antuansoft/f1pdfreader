# class TeamStanding

class TeamStanding:

    position:int
    team:str
    points:int    

    def __init__(self, position, team, points):
        
        self.position = position
        self.team = team
        self.points = points

    def __str__(self):
        return (self.position + ":" + self.team + ":" + self.points)