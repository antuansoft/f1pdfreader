


from crawlf1web2022 import Crawlf1web2022
from utils import *
from bs4 import BeautifulSoup

gppath:str= "_bahrein2022"



class Bahrain2022:

    def __init__(self) -> None:
        
        print("Generating Bahrain2022")
        bahrain2022 = Crawlf1web2022(gppath,
                                     "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix",
                                     "https://www.racefans.net/2022/03/20/2022-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/")
        
        bahrain2022.loadUrls()
        bahrain2022.loadWebPages()
        bahrain2022.parseUrls()
        bahrain2022.exportData(gppath)

