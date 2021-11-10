


from crawlf1web2021 import Crawlf1web2021
from utils import *

drivers_bahrein2021_url = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix"
drivers_bahrein2021_path:str = "2021/drivers_teams_bahrein2021.html"
race_classification_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification"
race_classification_bahrein2021_path:str = "2021/race_classification_bahrein2021.html"
starting_grid_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/9bb465b8-a1d7-4d67-beaf-c6b7a310d65a"
starting_grid_bahrein2021_path:str = "2021/starting_grid_bahrein2021.html" 


def main():
    print("main")

    drivers_html:str=downloadUrl(drivers_bahrein2021_url)
    saveWeb(drivers_html,drivers_bahrein2021_path)
    
    race_classification_html:str=downloadUrl(race_classification_bahrein2021_url)
    saveWeb(race_classification_html,race_classification_bahrein2021_path)
    
    starting_grid_html:str=downloadUrl(starting_grid_bahrein2021_url)
    saveWeb(starting_grid_html,starting_grid_bahrein2021_path)

    bahrain2021 = Crawlf1web2021(drivers_bahrein2021_path,
                                 race_classification_bahrein2021_path,
                                 starting_grid_bahrein2021_path,
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/drivers",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/teams",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=PitStop",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=FastestLap",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapChart",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapTime",
                                 "https://www.racefans.net/2021/03/29/2021-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/"
                                 )
    bahrain2021.load()
    
if __name__ == "__main__":
    main()