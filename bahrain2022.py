


from crawlf1web2021 import Crawlf1web2021
from utils import *
from bs4 import BeautifulSoup

gppath:str= "_bahrein2022"
## Page URLS and path
main_url = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix"
main_path:str = "2022/index"+gppath+".html"
classification_path:str = "2022/classification"+gppath+".html"
session_path:str = "2022/session"+gppath+".html"
standings_path:str = "2022/standings"+gppath+".html"

##Data Urls
base_url:str = "https://fiaresultsandstatistics.motorsportstats.com"
drivers_url:str = "https://fiaresultsandstatistics.motorsportstats.com/results/2022-bahrain-grand-prix"
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

        self.loadUrls()
        # self.loadData()
    
        # bahrain2022 = Crawlf1web2021(drivers_path,
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

    def loadUrls(self):

        print("loadUrls")
        # html_text: str = requests.get(self.drivers_url).text
        ## Parse urls
        
        ## main URL
        print("Main URL")
        main_html:str=downloadUrl(main_url)
        saveWeb(main_html,main_path)
        soup = BeautifulSoup(main_html, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('a', href=True, class_='uaJW4 kicqf')
        print("links encontrados:" + str(len(links)))
        classification_temp_url:str
        session_facts_temp_url:str
        standings_temp_url:str
        url_counter:int=0
        for link in links:
            print(link.string)
            if ('classification' in link.string.lower()):
                classification_temp_url=base_url + link['href']
                url_counter+=1
            if ('session' in link.string.lower()):
                session_facts_temp_url=base_url + link['href']
                url_counter+=1
            if ('standings' in link.string.lower()):
                standings_temp_url=base_url + link['href']
                url_counter+=1                          

        ## validation
        if (not url_counter==3):
           raise Exception("Main url has not been properly proccessed")

        ## classificaion URL 
        print("Classification URL")
        classification_html:str=downloadUrl(classification_temp_url)
        saveWeb(classification_html,classification_path)
        soup = BeautifulSoup(classification_html, 'html.parser')  
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('a', href=True, class_='uaJW4 _2j84j')
        print("links encontrados:" + str(len(links)))
        first_practice_temp_url:str
        second_practice_temp_url:str
        third_practice_temp_url:str
        q1_temp_url:str
        q2_temp_url:str
        q3_temp_url:str
        starting_grid_temp_url:str
        for link in links:
            print(link.string)
            if ('1' in link.string.lower() and 'practice' in link.string.lower() ):
                first_practice_temp_url=base_url + link['href']
                url_counter+=1
            if ('2' in link.string.lower() and 'practice' in link.string.lower() ):
                second_practice_temp_url=base_url + link['href']
                url_counter+=1
            if ('3' in link.string.lower() and 'practice' in link.string.lower() ):
                third_practice_temp_url=base_url + link['href']
                url_counter+=1
            if ('1' in link.string.lower() and 'qualifying' in link.string.lower() ):
                q1_temp_url=base_url + link['href']
                url_counter+=1
            if ('2' in link.string.lower() and 'qualifying' in link.string.lower() ):
                q2_temp_url=base_url + link['href']
                url_counter+=1                
            if ('3' in link.string.lower() and 'qualifying' in link.string.lower() ):
                q3_temp_url=base_url + link['href']
                url_counter+=1                
            if ('grid' in link.string.lower() ):
                starting_grid_temp_url = base_url + link['href']
                url_counter+=1
        ## validation
        if (not url_counter==10):
           raise Exception("Classification url has not been properly proccessed")


        ## Session Facts URL 
        print("Session Facts URL 1 ")
        session_html:str=downloadUrl(session_facts_temp_url)
        saveWeb(session_html,session_path)
        soup = BeautifulSoup(session_html, 'html.parser')  
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('a', href=True, class_='SaViI')
        print("links encontrados:" + str(len(links)))
        fastest_lap_temp_url:str
        lap_chart_temp_url:str
        lap_times_temp_url:str
        pit_stop_temp_url:str

        for link in links:
            print(link.string)

            if ('fastest' in link.string.lower()):
                fastest_lap_temp_url=base_url + link['href']
                url_counter+=1
            if ('chart' in link.string.lower()):
                lap_chart_temp_url=base_url + link['href']
                url_counter+=1
            if ('times' in link.string.lower()):
                lap_times_temp_url=base_url + link['href']
                url_counter+=1
            if ('pit' in link.string.lower()):
                pit_stop_temp_url=base_url + link['href']
                url_counter+=1

        ## validation
        if (not url_counter==14):
           raise Exception("Session  Fact 1 url has not been properly proccessed")



        ## Session Facts 2 URL 
        print("Session Facts URL 2 ")
        session_html:str=downloadUrl(session_facts_temp_url)
        saveWeb(session_html,session_path)
        soup = BeautifulSoup(session_html, 'html.parser')  
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('a', href=True, class_='uaJW4 _2_7Br')
        print("links encontrados:" + str(len(links)))
        q1_facts_temp_url:str
        q2_facts_temp_url:str
        q3_facts_temp_url:str
        
        for link in links:
            print(link.string)

            if ('1' in link.string.lower() and 'qualifying' in link.string.lower() ):
                q1_facts_temp_url=base_url + link['href']
                url_counter+=1
            if ('2' in link.string.lower() and 'qualifying' in link.string.lower() ):
                q2_facts_temp_url=base_url + link['href']
                url_counter+=1
            if ('3' in link.string.lower() and 'qualifying' in link.string.lower() ):
                q3_facts_temp_url=base_url + link['href']
                url_counter+=1

        ## validation
        if (not url_counter==17):
           raise Exception("Session  Fact 2 url has not been properly proccessed")



        ## Standings URL 
        print("Standings URL")
        session_html:str=downloadUrl(standings_temp_url)
        saveWeb(session_html,session_path)
        soup = BeautifulSoup(session_html, 'html.parser')  
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('a', href=True, class_='uaJW4')
        print("links encontrados:" + str(len(links)))
        driver_standings_temp_url:str
        team_standings_temp_url:str
        for link in links:
            print(link.string)
            if ('driver' in link.string.lower()):
                driver_standings_temp_url=base_url + link['href']
                url_counter+=1
            if ('team' in link.string.lower()):
                team_standings_temp_url=base_url + link['href']
                url_counter+=1

        ## validation
        if (not url_counter==19):
           raise Exception("Standings url has not been properly proccessed")

        ## Set urls
        drivers_url = main_url
        race_classification_url=classification_temp_url
        practice1_url = first_practice_temp_url
        practice2_url = second_practice_temp_url
        practice3_url = third_practice_temp_url
        q1_url = q1_temp_url
        q2_url = q2_temp_url
        q3_url = q3_temp_url
        starting_grid_url = starting_grid_temp_url
        fastest_laps_url = fastest_lap_temp_url
        lapchart_url = lap_chart_temp_url
        laptimes_url = lap_times_temp_url
        pitstops_url = pit_stop_temp_url
        driver_standings_url = driver_standings_temp_url
        team_standings_url = team_standings_temp_url


        print("fin loadUrls")


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