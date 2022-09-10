# class drivers

import yaml
import json

class Driver:

    path : str = "2022export/drivers"
    def __init__(self, number, name, country, team, car, engine):
        self.name = name
        self.country = country
        self.team = team
        self.number = number
        self.car = car
        self.engine = engine

    def __str__(self):
        return (self.name + ":" + self.country + ":" + self.team)

    def toYml(self, gppath):
       
       with open(self.path + gppath +".yml", 'w') as file:
        documents = yaml.dump(self,file)
       print(documents)      

    def toJson(self,gppath)-> str:
       print(json.dumps(self.__dict__))
       return json.dumps(self.__dict__)