


from crawlf1web2023 import Crawlf1web2023
from utils import *
from bs4 import BeautifulSoup

gppath:str= "_bahrein2023"



class Bahrain2023:

    def __init__(self) -> None:
        
        print("Generating Bahrain2023")
        bahrain2023 = Crawlf1web2023(gppath,
                                     "https://fiaresultsandstatistics.motorsportstats.com/results/2023-bahrain-grand-prix",
                                     "view-source:https://www.racefans.net/2023/03/05/2023-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/")
        bahrain2023.parseUrls()
        bahrain2023.exportData(gppath)

