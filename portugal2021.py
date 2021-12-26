


from crawlf1web2021 import Crawlf1web2021
from utils import *

gppath:str= "_portugal2021"
drivers_url = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix"
drivers_path:str = "2021/drivers_teams"+gppath+".html"
race_classification_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/classification"
race_classification_path:str = "2021/race_classification"+gppath+".html"
practice1_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/classification/e2933e4a-afeb-429a-8237-17a8ced6326a"
practice1_path:str = "2021/practice1_"+gppath+".html"
practice2_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/classification/65c1fb1f-966d-4209-a242-439b4c24b4b2"
practice2_path:str = "2021/practice2_"+gppath+".html"
practice3_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/classification/b4675f66-d4b8-4c63-8ad2-a9efdabf6599"
practice3_path:str = "2021/practice3_"+gppath+".html"
q1_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/classification/c54392ea-d198-4a57-a3f6-189f5024a5cb"
q1_path:str = "2021/q1_"+gppath+".html"
q2_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/classification/e3a085d2-3e4b-47b4-bb30-669f881170e8"
q2_path:str = "2021/q2_"+gppath+".html"
q3_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/classification/723231ad-bfcb-4b91-a5fa-ee887906be2e"
q3_path:str = "2021/q3_"+gppath+".html"
q1_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/session-facts/c54392ea-d198-4a57-a3f6-189f5024a5cb?fact=LapTime"
q1_laptimes_path:str = "2021/q1_laptimes_"+gppath+".html"
q2_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/session-facts/e3a085d2-3e4b-47b4-bb30-669f881170e8?fact=LapTime"
q2_laptimes_path:str = "2021/q2_laptimes_"+gppath+".html"
q3_laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/session-facts/723231ad-bfcb-4b91-a5fa-ee887906be2e?fact=LapTime"
q3_laptimes_path:str = "2021/q3_laptimes_"+gppath+".html"
starting_grid_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/classification/9062af11-7507-4e20-be50-88dd9ea43c2f"
starting_grid_path:str = "2021/starting_grid_"+gppath+".html" 
driver_standings_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/standings"
driver_standings_path:str = "2021/driver_standings_"+gppath+".html"
team_standings_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/standings/teams"
team_standings_path:str = "2021/team_standings_"+gppath+".html" 
pitstops_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/session-facts/5248260a-4e86-4292-893e-df63559d67d3?fact=PitStop"
pitstops_path:str = "2021/pitstops_"+gppath+".html"
fastest_laps_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/session-facts/5248260a-4e86-4292-893e-df63559d67d3?fact=FastestLap"
fastest_laps_path:str = "2021/fastest_laps_"+gppath+".html"
lapchart_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/session-facts/5248260a-4e86-4292-893e-df63559d67d3?fact=LapChart"
lapchart_path:str = "2021/lapchart_"+gppath+".html"
laptimes_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-portuguese-grand-prix/session-facts/5248260a-4e86-4292-893e-df63559d67d3?fact=LapTime"
laptimes_path:str = "2021/laptime_"+gppath+".html"
tyres_url:str = "https://www.racefans.net/2021/05/02/2021-portuguese-grand-prix-interactive-data-lap-charts-times-and-tyres/"
tyres_path:str = "2021/tyres_"+gppath+".html"

class Portugal2021:

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