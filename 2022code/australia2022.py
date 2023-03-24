


from crawlf1web2022 import Crawlf1web2022
from utils import *

gppath:str= "_australia2022"


class Australia2022:

    def __init__(self) -> None:
        
        print("Generating Australia2022")
        australia022 = Crawlf1web2022(gppath,
                                     "https://fiaresultsandstatistics.motorsportstats.com/results/2022-australian-grand-prix",
                                     "https://www.racefans.net/2022/04/10/2022-australian-grand-prix-interactive-data-lap-charts-times-and-tyres/")
        
        australia022.loadUrls()
        australia022.loadWebPages()
        australia022.parseUrls()
        australia022.exportData(gppath)

