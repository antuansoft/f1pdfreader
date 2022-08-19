


from crawlf1web2021 import Crawlf1web2021
from utils import *

gppath:str= "_bahrein2022"
drivers_url = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix"
drivers_path:str = "2022/drivers_teams"+gppath+".html"
race_classification_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/classification"
race_classification_path:str = "2022/race_classification"+gppath+".html"
practice1_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/classification/1a5e9872-0314-4288-ba70-0fe30f94b806"
practice1_path:str = "2022/practice1_"+gppath+".html"
practice2_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/classification/a90abd96-71eb-4d4a-8911-005545579b60"
practice2_path:str = "2022/practice2_"+gppath+".html"
practice3_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/classification/a9bf96d8-93f2-4160-8cfc-46b8f65c0f1f"
practice3_path:str = "2022/practice3_"+gppath+".html"
q1_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/classification/3fa83017-e860-4a5f-9c4c-b857de8361e7"
q1_path:str = "2022/q1_"+gppath+".html"
q2_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/classification/c86e4197-ca19-42bc-a6fd-52da399d7d05"
q2_path:str = "2022/q2_"+gppath+".html"
q3_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/classification/0e46aeb3-a362-422a-a78e-e0ea3eb6fe81"
q3_path:str = "2022/q3_"+gppath+".html"
q1_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/session-facts/3fa83017-e860-4a5f-9c4c-b857de8361e7?fact=LapTime"
q1_laptimes_path:str = "2022/q1_laptimes_"+gppath+".html"
q2_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/session-facts/c86e4197-ca19-42bc-a6fd-52da399d7d05?fact=LapTime"
q2_laptimes_path:str = "2022/q2_laptimes_"+gppath+".html"
q3_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/session-facts/0e46aeb3-a362-422a-a78e-e0ea3eb6fe81?fact=LapTime"
q3_laptimes_path:str = "2022/q3_laptimes_"+gppath+".html"



starting_grid_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/classification/c4582d96-7ea6-438f-bd48-c86f47bf22dd"
starting_grid_path:str = "2022/starting_grid_"+gppath+".html" 
driver_standings_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/standings/drivers"
driver_standings_path:str = "2022/driver_standings_"+gppath+".html"
team_standings_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/standings/teams"
team_standings_path:str = "2022/team_standings_"+gppath+".html" 
pitstops_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/session-facts/746ced1c-2648-44e8-9042-e9f4544c152f?fact=PitStop"
pitstops_path:str = "2022/pitstops_"+gppath+".html"
fastest_laps_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/session-facts"
fastest_laps_path:str = "2022/fastest_laps_"+gppath+".html"
lapchart_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/session-facts/746ced1c-2648-44e8-9042-e9f4544c152f?fact=LapChart"
lapchart_path:str = "2022/lapchart_"+gppath+".html"
laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix/session-facts/746ced1c-2648-44e8-9042-e9f4544c152f?fact=LapTime"
laptimes_path:str = "2022/laptime_"+gppath+".html"
tyres_url:str = "https://www.racefans.net/2022/03/20/2022-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/"
tyres_path:str = "2022/tyres_"+gppath+".html"

class Bahrain2022:

    def __init__(self) -> None:
        
        print("Bahrain2022")

        self.loadData()
    
        bahrain2022 = Crawlf1web2021(drivers_path,
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
        bahrain2022.load()
        bahrain2022.exportData(gppath)

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