


from crawlf1web2021 import Crawlf1web2021
from utils import *

drivers_bahrein2021_url = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix"
drivers_bahrein2021_path:str = "2021/drivers_teams_bahrein2021.html"
race_classification_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification"
race_classification_bahrein2021_path:str = "2021/race_classification_bahrein2021.html"
q1_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/be8ce756-5e39-41f2-a7f0-e6eb1984dd59"
q1_bahrein2021_path:str = "2021/q1_bahrein2021.html"
q2_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/920513e4-3cec-48fd-8802-6d0c7f94cd7b"
q2_bahrein2021_path:str = "2021/q2_bahrein2021.html"
q3_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/8d03296f-d6e0-4f1b-b89a-385d30e04a28"
q3_bahrein2021_path:str = "2021/q3_bahrein2021.html"
starting_grid_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/9bb465b8-a1d7-4d67-beaf-c6b7a310d65a"
starting_grid_bahrein2021_path:str = "2021/starting_grid_bahrein2021.html" 
driver_standings_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/drivers"
driver_standings_bahrein2021_path:str = "2021/driver_standings_bahrein2021.html"
team_standings_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/teams"
team_standings_bahrein2021_path:str = "2021/team_standings_bahrein2021.html" 
pitstops_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=PitStop"
pitstops_bahrein2021_path:str = "2021/pitstops_bahrein2021.html"
fastest_laps_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=FastestLap"
fastest_laps_bahrein2021_path:str = "2021/fastest_laps_bahrein2021.html"
lapchart_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapChart"
lapchart_bahrein2021_path:str = "2021/lapchart_bahrein2021.html"
laptimes_bahrein2021_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapTime"
laptimes_bahrein2021_path:str = "2021/laptime_bahrein2021.html"
tyres_bahrein2021_url:str = "https://www.racefans.net/2021/03/29/2021-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/"
tyres_bahrein2021_path:str = "2021/tyres_bahrein2021.html"
def main():
    print("main")

    # drivers_html:str=downloadUrl(drivers_bahrein2021_url)
    # saveWeb(drivers_html,drivers_bahrein2021_path)
    
    # race_classification_html:str=downloadUrl(race_classification_bahrein2021_url)
    # saveWeb(race_classification_html,race_classification_bahrein2021_path)

    # q1_html:str=downloadUrl(q1_bahrein2021_url)
    # saveWeb(q1_html,q1_bahrein2021_path)

    # q2_html:str=downloadUrl(q2_bahrein2021_url)
    # saveWeb(q2_html,q2_bahrein2021_path)
    
    # q3_html:str=downloadUrl(q3_bahrein2021_url)
    # saveWeb(q3_html,q3_bahrein2021_path)

    # starting_grid_html:str=downloadUrl(starting_grid_bahrein2021_url)
    # saveWeb(starting_grid_html,starting_grid_bahrein2021_path)

    # driver_standings_html:str=downloadUrl(driver_standings_bahrein2021_url)
    # saveWeb(driver_standings_html,driver_standings_bahrein2021_path)

    # team_standings_html:str=downloadUrl(team_standings_bahrein2021_url)
    # saveWeb(team_standings_html,team_standings_bahrein2021_path)

    # pitstops_html:str=downloadUrl(pitstops_bahrein2021_url)
    # saveWeb(pitstops_html,pitstops_bahrein2021_path)

    # fastest_laps_html:str=downloadUrl(fastest_laps_bahrein2021_url)
    # saveWeb(fastest_laps_html,fastest_laps_bahrein2021_path)

    # lapchart_html:str=downloadUrl(lapchart_bahrein2021_url)
    # saveWeb(lapchart_html,lapchart_bahrein2021_path)

    # laptimes_html:str=downloadUrl(laptimes_bahrein2021_url)
    # saveWeb(laptimes_html,laptimes_bahrein2021_path)

    # tyres_html:str=downloadUrl(tyres_bahrein2021_url)
    # saveWeb(tyres_html,tyres_bahrein2021_path)

    bahrain2021 = Crawlf1web2021(drivers_bahrein2021_path,
                                 race_classification_bahrein2021_path,
                                 q1_bahrein2021_path,
                                 q2_bahrein2021_path,
                                 q3_bahrein2021_path,
                                 starting_grid_bahrein2021_path,
                                 driver_standings_bahrein2021_path,
                                 team_standings_bahrein2021_path,
                                 pitstops_bahrein2021_path,
                                 fastest_laps_bahrein2021_path,
                                 lapchart_bahrein2021_path,
                                 laptimes_bahrein2021_path,
                                 tyres_bahrein2021_path
                                 )
    bahrain2021.load()
    
if __name__ == "__main__":
    main()