


from crawlf1web2021 import Crawlf1web2021
from crawlf1web2021b import Crawlf1web2021b
from utils import *

gppath:str= "_british"
drivers_url = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix"
drivers_path:str = "2021/drivers_teams"+gppath+".html"
race_classification_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/classification"
race_classification_path:str = "2021/race_classification"+gppath+".html"
practice1_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/classification/4435adc1-2226-4eab-841f-db6a5cca6d76"
practice1_path:str = "2021/practice1_"+gppath+".html"
practice2_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/classification/46907f58-0999-4e16-8c81-ff45976a9a1e"
practice2_path:str = "2021/practice2_"+gppath+".html"
sprint_grid_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/classification/29f9bd35-a37e-48aa-a394-6a2c2bef428d"
sprint_grid_path:str = "2021/sprint_grid_"+gppath+".html"
sprint_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/classification/b4bb5e7a-af5f-4ed9-a6da-c78a94019e51"
sprint_path:str = "2021/sprint_"+gppath+".html"
q1_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/classification/77d9815a-fe39-43a7-a72e-fffc9726d8a0"
q1_path:str = "2021/q1_"+gppath+".html"
q2_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/classification/cf47396b-3a64-40dc-bdd7-7388a4724c0d"
q2_path:str = "2021/q2_"+gppath+".html"
q3_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/classification/e3f9c820-c7e8-461a-9f19-3590adc17af2"
q3_path:str = "2021/q3_"+gppath+".html"


q1_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/session-facts/77d9815a-fe39-43a7-a72e-fffc9726d8a0?fact=LapTime"
q1_laptimes_path:str = "2021/q1_laptimes_"+gppath+".html"
q2_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/session-facts/cf47396b-3a64-40dc-bdd7-7388a4724c0d?fact=LapTime"
q2_laptimes_path:str = "2021/q2_laptimes_"+gppath+".html"
q3_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/session-facts/e3f9c820-c7e8-461a-9f19-3590adc17af2?fact=LapTime"
q3_laptimes_path:str = "2021/q3_laptimes_"+gppath+".html"



starting_grid_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/classification/87404136-48e7-4d2b-b4d1-bbc407cfe6ee"
starting_grid_path:str = "2021/starting_grid_"+gppath+".html" 
driver_standings_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/standings/drivers"
driver_standings_path:str = "2021/driver_standings_"+gppath+".html"
team_standings_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/standings/teams"
team_standings_path:str = "2021/team_standings_"+gppath+".html" 
pitstops_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/session-facts/396869f2-d8c8-43a7-90f2-7ffbd4afcecf?fact=PitStop"
pitstops_path:str = "2021/pitstops_"+gppath+".html"
fastest_laps_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/session-facts/396869f2-d8c8-43a7-90f2-7ffbd4afcecf?fact=FastestLap"
fastest_laps_path:str = "2021/fastest_laps_"+gppath+".html"
lapchart_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/session-facts/396869f2-d8c8-43a7-90f2-7ffbd4afcecf?fact=LapChart"
lapchart_path:str = "2021/lapchart_"+gppath+".html"
laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-british-grand-prix/session-facts/396869f2-d8c8-43a7-90f2-7ffbd4afcecf?fact=LapTime"
laptimes_path:str = "2021/laptime_"+gppath+".html"
tyres_url:str = "https://www.racefans.net/2021/07/18/2021-british-grand-prix-interactive-data-lap-charts-times-and-tyres/"
tyres_path:str = "2021/tyres_"+gppath+".html"

class British2021:

    def __init__(self) -> None:
        
        print("British2021")

        self.loadData()
    
        bahrain2021 = Crawlf1web2021b(drivers_path,
                                        race_classification_path,
                                        practice1_path,
                                        practice2_path,
                                        sprint_grid_path,
                                        sprint_path,
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

        sprint_grid_html:str=downloadUrl(sprint_grid_url)
        saveWeb(sprint_grid_html,sprint_grid_path)    

        sprint_html:str=downloadUrl(sprint_url)
        saveWeb(sprint_html,sprint_path)    


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