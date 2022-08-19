# class GpInfo
from ast import Str
import yaml

class GpInfo:

    path : str = "2022export/gpinfo"
    def __init__(self, gp, circuit, date, round, totalCircuits ):
        
        self.gp = gp
        self.date = date
        self.circuit = circuit
        self.round = round
        self.totalCircuits = totalCircuits
      

    def __str__(self):
        return (self.gp + ":" + self.date + ":" + self.circuit + ":" + self.round  +
                " of " + str(self.totalCircuits)
                )

    def toFile(self, gppath):
       
       with open(self.path + gppath +".yml", 'w') as file:
        documents = yaml.dump(self,file)
       print(documents)      
