# class GpInf

class GpInfo:

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