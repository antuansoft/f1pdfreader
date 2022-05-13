


from crawlf1web2021 import Crawlf1web2021
from utils import *

gppath:str= "_xxxxx"
drivers_url = ""
drivers_path:str = "2022/drivers_teams"+gppath+".html"
race_classification_url:str = ""
race_classification_path:str = "2022/race_classification"+gppath+".html"
practice1_url:str = ""
practice1_path:str = "2022/practice1_"+gppath+".html"
practice2_url:str = ""
practice2_path:str = "2022/practice2_"+gppath+".html"
practice3_url:str = ""
practice3_path:str = "2022/practice3_"+gppath+".html"
q1_url:str = ""
q1_path:str = "2022/q1_"+gppath+".html"
q2_url:str = ""
q2_path:str = "2022/q2_"+gppath+".html"
q3_url:str = ""
q3_path:str = "2022/q3_"+gppath+".html"


q1_laptimes_url:str = ""
q1_laptimes_path:str = "2022/q1_laptimes_"+gppath+".html"
q2_laptimes_url:str = ""
q2_laptimes_path:str = "2022/q2_laptimes_"+gppath+".html"
q3_laptimes_url:str = ""
q3_laptimes_path:str = "2022/q3_laptimes_"+gppath+".html"



starting_grid_url:str = ""
starting_grid_path:str = "2022/starting_grid_"+gppath+".html" 
driver_standings_url:str = ""
driver_standings_path:str = "2022/driver_standings_"+gppath+".html"
team_standings_url:str = ""
team_standings_path:str = "2022/team_standings_"+gppath+".html" 
pitstops_url:str = ""
pitstops_path:str = "2022/pitstops_"+gppath+".html"
fastest_laps_url:str = ""
fastest_laps_path:str = "2022/fastest_laps_"+gppath+".html"
lapchart_url:str = ""
lapchart_path:str = "2022/lapchart_"+gppath+".html"
laptimes_url:str = ""
laptimes_path:str = "2022/laptime_"+gppath+".html"
tyres_url:str = ""
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