


from crawlf1web2022 import Crawlf1web2022
from utils import *

gppath:str= "_arabia2022"


class Arabia2022:

    def __init__(self) -> None:
        
        print("Generating _arabia2022")
        arabia2022 = Crawlf1web2022(gppath,
                                     "https://fiaresultsandstatistics.motorsportstats.com/results/2022-saudi-arabian-grand-prix",
                                     "https://www.racefans.net/2022/03/28/2022-saudi-arabian-grand-prix-interactive-data-lap-charts-times-and-tyres/")
        
        arabia2022.loadUrls()
        arabia2022.loadWebPages()
        arabia2022.parseUrls()
        arabia2022.exportData(gppath)

