


from crawlf1web2022 import Crawlf1web2022
from utils import *
from bs4 import BeautifulSoup

gppath:str= ""



class Bahrain2022:

    def __init__(self) -> None:
        
        print("Bahrain2022")

        # self.loadUrls()
        # self.loadData()
        bahrain2022 = Crawlf1web2022("_bahrein2022",
                                     "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix",
                                     "https://www.racefans.net/2022/03/20/2022-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/")
        
        bahrain2022.loadUrls()
        bahrain2022.loadWebPages()
        bahrain2022.parseUrls()
        bahrain2022.exportData("_bahrein2022")
        # bahrain2022 = Crawlf1web2022(drivers_path,
        #                                 race_classification_path,
        #                                 practice1_path,
        #                                 practice2_path,
        #                                 practice3_path,
        #                                 q1_path,
        #                                 q2_path,
        #                                 q3_path,
        #                                 q1_laptimes_path,
        #                                 q2_laptimes_path,
        #                                 q3_laptimes_path,
        #                                 starting_grid_path,
        #                                 driver_standings_path,
        #                                 team_standings_path,
        #                                 pitstops_path,
        #                                 fastest_laps_path,
        #                                 lapchart_path,
        #                                 laptimes_path,
        #                                 tyres_path
        #                                 )
        # bahrain2022.load()
        # bahrain2022.export2Json(gppath)


