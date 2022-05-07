


from crawlf1web2021 import Crawlf1web2021
from utils import *

gppath:str= "_bahrein2021"
drivers_url = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix"
drivers_path:str = "2021/drivers_teams"+gppath+".html"
race_classification_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification"
race_classification_path:str = "2021/race_classification"+gppath+".html"
practice1_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/0c81a6c4-b620-4690-9f0d-8ccf50393875"
practice1_path:str = "2021/practice1"+gppath+".html"
practice2_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/db11f035-2f17-4331-bd0f-ece4f37c7627"
practice2_path:str = "2021/practice2"+gppath+".html"
practice3_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/e15fe67e-e499-4a23-8eb5-6ee38f5759e0"
practice3_path:str = "2021/practice3"+gppath+".html"
q1_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/be8ce756-5e39-41f2-a7f0-e6eb1984dd59"
q1_path:str = "2021/q1"+gppath+".html"
q2_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/920513e4-3cec-48fd-8802-6d0c7f94cd7b"
q2_path:str = "2021/q2"+gppath+".html"
q3_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/8d03296f-d6e0-4f1b-b89a-385d30e04a28"
q3_path:str = "2021/q3"+gppath+".html"


q1_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/be8ce756-5e39-41f2-a7f0-e6eb1984dd59?fact=LapTime"
q1_laptimes_path:str = "2021/q1_laptimes"+gppath+".html"
q2_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/920513e4-3cec-48fd-8802-6d0c7f94cd7b?fact=LapTime"
q2_laptimes_path:str = "2021/q2_laptimes"+gppath+".html"
q3_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/8d03296f-d6e0-4f1b-b89a-385d30e04a28?fact=LapTime"
q3_laptimes_path:str = "2021/q3_laptimes"+gppath+".html"



starting_grid_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/9bb465b8-a1d7-4d67-beaf-c6b7a310d65a"
starting_grid_path:str = "2021/starting_grid"+gppath+".html" 
driver_standings_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/drivers"
driver_standings_path:str = "2021/driver_standings"+gppath+".html"
team_standings_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/teams"
team_standings_path:str = "2021/team_standings"+gppath+".html" 
pitstops_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=PitStop"
pitstops_path:str = "2021/pitstops"+gppath+".html"
fastest_laps_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=FastestLap"
fastest_laps_path:str = "2021/fastest_laps"+gppath+".html"
lapchart_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapChart"
lapchart_path:str = "2021/lapchart"+gppath+".html"
laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapTime"
laptimes_path:str = "2021/laptime"+gppath+".html"
tyres_url:str = "https://www.racefans.net/2021/03/29/2021-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/"
tyres_path:str = "2021/tyres"+gppath+".html"

class Bahrain2021:

    def __init__(self) -> None:
        
        print("Bahrain2021")

        self.loadData()
    
        bahrain2021 = Crawlf1web2021(drivers_path,
                                        race_classification_path,
                                        practice1_path,
                                        practice2_path,
                                        practice3_path,
                                        q1_path,
                                        q2_path,
                                        q3_path,
                                        q1_laptimes_path,
                                        q2_laptimes_path,
                                        q3_laptimes_path,
                                        starting_grid_path,
                                        driver_standings_path,
                                        team_standings_path,
                                        pitstops_path,
                                        fastest_laps_path,
                                        lapchart_path,
                                        laptimes_path,
                                        tyres_path
                                        )
        bahrain2021.load()

    def loadData(self):

        drivers_html:str=downloadUrl(drivers_url)
        saveWeb(drivers_html,drivers_path)

        race_classification_html:str=downloadUrl(race_classification_url)
        saveWeb(race_classification_html,race_classification_path)

        practice1_html:str=downloadUrl(practice1_url)
        saveWeb(practice1_html,practice1_path)

        practice2_html:str=downloadUrl(practice2_url)
        saveWeb(practice2_html,practice2_path)

        practice3_html:str=downloadUrl(practice3_url)
        saveWeb(practice3_html,practice3_path)    

        q1_html:str=downloadUrl(q1_url)
        saveWeb(q1_html,q1_path)

        q2_html:str=downloadUrl(q2_url)
        saveWeb(q2_html,q2_path)

        q3_html:str=downloadUrl(q3_url)
        saveWeb(q3_html,q3_path)

        q1_laptimes_html:str=downloadUrl(q1_laptimes_url)
        saveWeb(q1_laptimes_html,q1_laptimes_path)

        q2_laptimes_html:str=downloadUrl(q2_laptimes_url)
        saveWeb(q2_laptimes_html,q2_laptimes_path)

        q3_laptimes_html:str=downloadUrl(q3_laptimes_url)
        saveWeb(q3_laptimes_html,q3_laptimes_path)

        starting_grid_html:str=downloadUrl(starting_grid_url)
        saveWeb(starting_grid_html,starting_grid_path)

        driver_standings_html:str=downloadUrl(driver_standings_url)
        saveWeb(driver_standings_html,driver_standings_path)

        team_standings_html:str=downloadUrl(team_standings_url)
        saveWeb(team_standings_html,team_standings_path)

        pitstops_html:str=downloadUrl(pitstops_url)
        saveWeb(pitstops_html,pitstops_path)

        fastest_laps_html:str=downloadUrl(fastest_laps_url)
        saveWeb(fastest_laps_html,fastest_laps_path)

        lapchart_html:str=downloadUrl(lapchart_url)
        saveWeb(lapchart_html,lapchart_path)

        laptimes_html:str=downloadUrl(laptimes_url)
        saveWeb(laptimes_html,laptimes_path)

        tyres_html:str=downloadUrl(tyres_url)
        saveWeb(tyres_html,tyres_path)