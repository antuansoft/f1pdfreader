from typing import Any, List, Type
import requests
import json
from bs4 import BeautifulSoup
from bs4.element import Script
from driverStanding import DriverStanding
from fastestlap import FastestLap
from gpInfo import GpInfo
from lapchart import LapChart
from laptime import LapTime
from pitStop import PitStop
from raceresult import RaceResult
from startinggrid import StartingGrid
from teamStanding import TeamStanding
from tyres import Stint
from utils import *
from driver import *
from team import *

gppath:str= ""
## Page URLS and path
main_url:str = ""
main_path:str = ""
tyres_url:str = ""
tyres_path:str = ""
classification_path:str = ""
session_path:str = ""
standings_path:str = ""
q1_facts_path_str = ""
q2_facts_path_str = ""
q3_facts_path_str = ""

##Data Urls
base_url:str = "https://fiaresultsandstatistics.motorsportstats.com"
drivers_url:str = ""
# drivers_path:str = "2022/drivers_teams"+gppath+".html"
race_classification_url:str = ""
race_classification_path:str = ""
practice1_url:str = ""
practice1_path:str = ""
practice2_url:str = ""
practice2_path:str = ""
practice3_url:str = ""
practice3_path:str = ""
q1_url:str = ""
q1_path:str = ""
q2_url:str = ""
q2_path:str = ""
q3_url:str = ""
q3_path:str = ""
q1_laptimes_url:str = ""
q1_laptimes_path:str = ""
q2_laptimes_url:str = ""
q2_laptimes_path:str = ""
q3_laptimes_url:str = ""
q3_laptimes_path:str = ""

starting_grid_url:str = ""
starting_grid_path:str = ""
driver_standings_url:str = ""
driver_standings_path:str = ""
team_standings_url:str = ""
team_standings_path:str = ""
pitstops_url:str = ""
pitstops_path:str = ""
fastest_laps_url:str = ""
fastest_laps_path:str = ""
lapchart_url:str = ""
lapchart_path:str = ""
laptimes_url:str = ""
laptimes_path:str = ""


class Crawlf1web2022:

    gpInfo: GpInfo = None
    drivers:dict = dict() 
    teams:dict = dict() 
    raceResuts = []
    practice1:list = []
    practice2:list = []
    practice3:list = []
    q1:list=[]
    q2:list=[]
    q3:list=[]
    startingGrids = []
    driverStandings = []
    teamStandings = []
    pitStops:dict = dict()
    fastestLaps = []
    lapCharts = []
    lapTimes:dict = dict()
    lapTimesq1:dict = dict()
    lapTimesq2:dict = dict()
    lapTimesq3:dict = dict()
    tyres:dict = dict()

    def __init__(self, gppath, mainGpUrl,tyresGpUrl):
        self.gppath = gppath
        self.main_url = mainGpUrl
        self.tyres_url = tyresGpUrl

        self.main_path = "2022/index"+gppath+".html"
        self.tyres_path = "2022/tyres_"+gppath+".html"
        self.classification_path = "2022/classification"+gppath+".html"
        self.session_path = "2022/session"+gppath+".html"
        self.standings_path = "2022/standings"+gppath+".html"
        self.q1_facts_path_str = "2022/q1_facts"+gppath+".html"
        self.q2_facts_path_str = "2022/q2_facts"+gppath+".html"
        self.q3_facts_path_str = "2022/q3_facts"+gppath+".html"

        self.drivers_path = "2022/drivers_teams"+gppath+".html"
        self.race_classification_path = "2022/race_classification"+gppath+".html"
        self.practice1_path= "2022/practice1_"+gppath+".html"
        self.practice2_path= "2022/practice2_"+gppath+".html"
        self.practice3_path = "2022/practice3_"+gppath+".html"
        
        self.q1_path:str = "2022/q1_"+gppath+".html"
        
        self.q2_path:str = "2022/q2_"+gppath+".html"
        
        self.q3_path:str = "2022/q3_"+gppath+".html"
        self.q1_laptimes_path:str = "2022/q1_laptimes_"+gppath+".html"
        self.q2_laptimes_path:str = "2022/q2_laptimes_"+gppath+".html"
        self.q3_laptimes_path:str = "2022/q3_laptimes_"+gppath+".html"

        self.starting_grid_path:str = "2022/starting_grid_"+gppath+".html" 
        self.driver_standings_path:str = "2022/driver_standings_"+gppath+".html"
        self.team_standings_path:str = "2022/team_standings_"+gppath+".html" 
        self.pitstops_path:str = "2022/pitstops_"+gppath+".html"
        self.fastest_laps_path:str = "2022/fastest_laps_"+gppath+".html"
        self.lapchart_path:str = "2022/lapchart_"+gppath+".html"
        self.laptimes_path:str = "2022/laptime_"+gppath+".html"        

        print(mainGpUrl)
        print(self.main_path)
        print(self.main_url)
    
    def loadUrls(self):

        print("loadUrls")
        # html_text: str = requests.get(self.drivers_url).text
        ## Parse urls
        
        ## main URL
        print("Main URL:"+ self.main_url)
        main_html:str=downloadUrl(self.main_url)
        saveWeb(main_html,self.main_path)
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
        saveWeb(classification_html,self.classification_path)
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
        saveWeb(session_html,self.session_path)
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
        saveWeb(session_html,self.session_path)
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

        #QX_Facts Urls
        q1_laptimes_temp_url:str = None
        q2_laptimes_temp_url:str = None
        q3_laptimes_temp_url:str = None
        q_facts = [q1_facts_temp_url,q2_facts_temp_url,q3_facts_temp_url]
        q_paths = [self.q1_facts_path_str,self.q2_facts_path_str,self.q3_facts_path_str]
        q_laptimes = []
        index:int = 0
        for q_fact in q_facts:
            q_html:str=downloadUrl(q_fact)
            saveWeb(q_html,q_paths[index])
            soup = BeautifulSoup(q_html, 'html.parser')  
            print("parseado:"+ soup.title.string)
            print("---------------------")            
            links:list = soup.find_all('a', href=True, class_='SaViI')
            print("links encontrados:" + str(len(links)))
            for link in links:
                print(link.string)
                if ('times' in link.string.lower()):
                    q_laptimes.append(base_url + link['href'])
                    print(q_laptimes[index])
                    url_counter+=1
            index+=1

        q1_laptimes_temp_url = q_laptimes[0]
        q2_laptimes_temp_url = q_laptimes[1]
        q3_laptimes_temp_url = q_laptimes[2]
        

        ## validation
        if (not url_counter==20):
            raise Exception("Qx Facts url has not been properly proccessed")

        # Standings URL 
        print("Standings URL")
        session_html:str=downloadUrl(standings_temp_url)
        saveWeb(session_html,self.session_path)
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
        if (not url_counter==22):
            raise Exception("Standings url has not been properly proccessed")

        ## Set urls
        self.drivers_url = self.main_url
        self.race_classification_url=classification_temp_url
        self.practice1_url = first_practice_temp_url
        self.practice2_url = second_practice_temp_url
        self.practice3_url = third_practice_temp_url
        self.q1_url = q1_temp_url
        self.q2_url = q2_temp_url
        self.q3_url = q3_temp_url
        self.starting_grid_url = starting_grid_temp_url
        self.fastest_laps_url = fastest_lap_temp_url
        self.lapchart_url = lap_chart_temp_url
        self.laptimes_url = lap_times_temp_url
        self.pitstops_url = pit_stop_temp_url
        self.q1_laptimes_url = q1_laptimes_temp_url
        self.q2_laptimes_url = q2_laptimes_temp_url
        self.q3_laptimes_url = q3_laptimes_temp_url
        self.driver_standings_url = driver_standings_temp_url
        self.team_standings_url = team_standings_temp_url

        print(self.main_path)
        print(self.main_url)
        print(self.drivers_url)
        print(main_url)
        print("fin loadUrls")

    def loadWebPages(self):

        drivers_html:str=downloadUrl(self.drivers_url)
        saveWeb(drivers_html,self.drivers_path)

        race_classification_html:str=downloadUrl(self.race_classification_url)
        saveWeb(race_classification_html,self.race_classification_path)

        practice1_html:str=downloadUrl(self.practice1_url)
        saveWeb(practice1_html,self.practice1_path)

        practice2_html:str=downloadUrl(self.practice2_url)
        saveWeb(practice2_html,self.practice2_path)

        practice3_html:str=downloadUrl(self.practice3_url)
        saveWeb(practice3_html,self.practice3_path)    

        q1_html:str=downloadUrl(self.q1_url)
        saveWeb(q1_html,self.q1_path)

        q2_html:str=downloadUrl(self.q2_url)
        saveWeb(q2_html,self.q2_path)

        q3_html:str=downloadUrl(self.q3_url)
        saveWeb(q3_html,self.q3_path)

        q1_laptimes_html:str=downloadUrl(self.q1_laptimes_url)
        saveWeb(q1_laptimes_html,self.q1_laptimes_path)

        q2_laptimes_html:str=downloadUrl(self.q2_laptimes_url)
        saveWeb(q2_laptimes_html,self.q2_laptimes_path)

        q3_laptimes_html:str=downloadUrl(self.q3_laptimes_url)
        saveWeb(q3_laptimes_html,self.q3_laptimes_path)

        starting_grid_html:str=downloadUrl(self.starting_grid_url)
        saveWeb(starting_grid_html,self.starting_grid_path)

        driver_standings_html:str=downloadUrl(self.driver_standings_url)
        saveWeb(driver_standings_html,self.driver_standings_path)

        team_standings_html:str=downloadUrl(self.team_standings_url)
        saveWeb(team_standings_html,self.team_standings_path)

        pitstops_html:str=downloadUrl(self.pitstops_url)
        saveWeb(pitstops_html,self.pitstops_path)

        fastest_laps_html:str=downloadUrl(self.fastest_laps_url)
        saveWeb(fastest_laps_html,self.fastest_laps_path)

        lapchart_html:str=downloadUrl(self.lapchart_url)
        saveWeb(lapchart_html,self.lapchart_path)

        laptimes_html:str=downloadUrl(self.laptimes_url)
        saveWeb(laptimes_html,self.laptimes_path)

        tyres_html:str=downloadUrl(tyres_url)
        saveWeb(tyres_html,self.tyres_path)

    def parseUrls(self):
        self.parseInfo()
        self.parseDrivers()
        self.parseRaceClassification()
        self.parseGrid("Practice 1",self.practice1_path,self.practice1)
        self.parseGrid("Practice 2",self.practice2_path,self.practice2)
        self.parseGrid("Practice 3",self.practice3_path,self.practice3)
        self.parseGrid("Q1",self.q1_path,self.q1)
        self.parseGrid("Q2",self.q2_path,self.q2)
        self.parseGrid("Q3",self.q3_path,self.q3)
        self.parseLapTimes("Q1",self.q1_laptimes_path,self.lapTimesq1)
        self.parseLapTimes("Q2",self.q2_laptimes_path,self.lapTimesq2)
        self.parseLapTimes("Q3",self.q3_laptimes_path,self.lapTimesq3)
        self.parseGrid("Starting Grid",self.starting_grid_path,self.startingGrids)
        self.parseDriverStandings()
        self.parseTeamsStandings()
        self.parsePitStop()
        self.parseFastestLaps()
        self.parseLapChart()
        self.parseLapTimes("Race",self.laptimes_path,self.lapTimes)
        self.parseTyres()

    def exportData(self,gppath):
        print("Export data")
        self.export2Json(gppath)

    def parseTyres(self):
        print("start  Tyres")
        # html_text: str = requests.get(self.tyres_url).text
        html_text: str = readFile(self.tyres_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('table',class_='thin')
        print("links encontrados:" + str(len(links)))
        value_to_find: str = "Stint"
        for link in links:
            valueStr: str = str(link.thead)
            # print(valueStr)
            maxStints:int = valueStr.count("Stint")
            if (valueStr.find(value_to_find)>-1):
                trs: list = link.tbody.find_all('tr')
                for tr in trs:
                    stints: list = tr.find_all('td')
                    index:int = 0
                    nomDriver:int
                    stint: Stint
                    stintsArr = []
                    for stnt in stints:
                        data:str = stnt.string
                        key:int
                        if(index==0):
                            nomDriver = data
                            key=getdriverId(nomDriver,self.drivers)
                            print("piloto:"+nomDriver)
                            print("key:"+key)
                        elif (index>0):
                            stint:Stint = Stint(None, "",0,0)
                            stint.driver = nomDriver
                            if (data):
                                tyre = data.split()
                                stint.tyre = tyre[0]
                                stint.laps = normalize_number(tyre[1])                                
                            stint.stintNum = index
                            stintsArr.append(stint)
                            # print(stint)
                            # print(stintsArr)
                        index = index + 1
                        # print(stint.string,end=' ')
                        # print(index)
                    self.tyres[key]=stintsArr
                    # print()
                for key in self.tyres.keys():
                    stints = self.tyres[key]
                    # print(stints)
                    for stint in stints:
                        print(stint)
        print("end tyres")

    def parseLapTimesOrig(self):
        print("start  Lap Chart")
        # html_text: str = requests.get(self.lap_times_url).text
        html_text: str = readFile(self.lap_times_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        lap_links:list = soup.find_all('script')
        print("links encontrados:" + str(len(lap_links)))
        value_to_find: str = "window.App="
        data: str
        json_data: Any
        pilots: list
        for link in lap_links:
            valueStr: str = str(link.string)
            if (valueStr.find(value_to_find)==0):
                data = link.string
                data = data[len(value_to_find):]
                json_data = json.loads(data)
                pilots = json_data["state"]['session']['stats']['data']
                laps: list
                for pilot in pilots:
                    number:int=pilot['carNumber']
                    driver:str=pilot['driver']['name']
                    # print(number+"-"+driver)
                    laps = pilot['laps']
                    pilotLapTimes = []
                    lapTime:LapTime
                    for lap in laps:
                        lnumber:int = lap['lap']
                        ltime: int =lap['time']
                        lapTime = LapTime(driver, number, lnumber,ltime)
                        pilotLapTimes.append(lapTime)
                        # print(str(lapNumber)+":"+str(lapTime))
                    # print(number)
                    self.lapTimes[number] = pilotLapTimes
        for pilot in self.lapTimes.keys():
            print(pilot)
            for lt in self.lapTimes[pilot]:
                print(lt)
        print("end  Lap Times")

    def parseLapChart(self):
        print("start  Lap Chart")
        # html_text: str = requests.get(self.lap_chart_url).text
        html_text: str = readFile(self.lapchart_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        lap_links:list = soup.find_all('td',class_='_2sWDi')
        print("links encontrados:" + str(len(lap_links)))
        positions:list = soup.find_all('div',class_='_1BvfV')
        print("links encontrados:" + str(len(positions)))
        lap: str = ""
        number: str = ""
        lap_index:int = 0
        for i in range(len(lap_links)):
            # print()
            lapChart:LapChart = None
            for j in range(20):
                if (j==0):
                    lap = getString(lap_links[lap_index].string)
                    lapChart = LapChart(lap)
                    # print(lap+":", end='')
                number = getString(positions[i+(j*len(lap_links))].string)
                lapChart.cars.append(number)
                # print(number, end=',')
                # if (j==20):
                #    print()
            lap_index= lap_index +1
            self.lapCharts.append(lapChart)
        # print()
        for lc in self.lapCharts:
            print(lc)
        print("end  Lap Chart")

    def parseFastestLaps(self):
        print("start  Fastest Laps")
        # html_text: str = requests.get(self.fastest_laps_url).text
        html_text: str = readFile(self.fastest_laps_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('td')
        print("links encontrados:" + str(len(links)))
        i:int = 1
        rowCount:int = 1
        position:str = "" 
        number:str = ""
        driver:str = ""
        team:str = ""
        time:str = ""
        lap:str = ""
        gap:str = ""
        fastestLap: FastestLap
        for link in links:
            if (rowCount == 1):
                position = getString(link.string)
            elif (rowCount == 2):
                number = getString(link.string)
            elif (rowCount == 3):
                driver = getString(link.string)
            elif (rowCount == 4):
                team = getString(link.string)
            elif (rowCount == 5):
                time = getString(link.string)            
            elif (rowCount == 6):
                lap = getString(link.string)            
            elif (rowCount == 7):
                gap = getString(link.string)            
                #   print (position +":" + number +":" +driver + ":" + team + ":" + time + ":" + lap + ":" + gap )
                fastestLap = FastestLap(position, number, driver, team,time,lap,gap)
                self.fastestLaps.append(fastestLap)
                rowCount = 0
                position = "" 
                number = ""
                driver = ""
                team = ""
                time = ""
                lap = ""
                gap = ""
            rowCount = rowCount + 1
        for fL in self.fastestLaps:
            print(fL)
        print("end Fastest Laps")
    
    def parsePitStop(self):
        print("start  Pit Stops")
        # html_text: str = requests.get(self.pit_stops_url).text
        html_text: str = readFile(self.pitstops_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('td')
        print("links encontrados:" + str(len(links)))
        i:int = 1
        rowCount:int = 1
        number:str = ""
        driver:str = ""
        team:str = ""
        lap:str = ""
        stop:str = ""
        time:str = ""
        timeTotal:str = ""
        for link in links:
            if (rowCount == 1):
                number = getString(link.string)
            elif (rowCount == 2):
                driver = getString(link.string)
            elif (rowCount == 3):
                team = getString(link.string)
            elif (rowCount == 4):
                lap = getString(link.string)
            elif (rowCount == 5):
                stop = getString(link.string)            
            elif (rowCount == 6):
                time = getString(link.string)            
            elif (rowCount == 7):
                timeTotal = getString(link.string)            
                # print (number +":" +driver + ":" + team + ":" + lap + ":" + stop + ":" + time + ":" + timeTotal)
                pitStop = PitStop(number,driver,team,lap,stop,time,timeTotal)
                pitStopList = self.pitStops.get(number)
                if (pitStopList == None):
                    pitStopsListTmp = []
                    pitStopsListTmp.append(pitStop)
                    self.pitStops[number] = pitStopsListTmp
                else:
                    pitStopList.append(pitStop)
                rowCount = 0
                number = ""
                driver = ""
                team = ""
                lap = ""
                stop = ""
                time = ""
                timeTotal = ""
            rowCount = rowCount + 1
        for pitStopKey in self.pitStops.keys():
            for pitStoptmp in self.pitStops[pitStopKey]:
                print(pitStoptmp)
        print("end Pit Stops")

    def parseTeamsStandings(self):
        print("start Teams Standings")
        # html_text: str = requests.get(self.teams_standings_url).text
        html_text: str = readFile(self.team_standings_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('td')
        print("links encontrados:" + str(len(links)))
        i:int = 1
        rowCount:int = 1
        position:str = ""
        team:str = ""
        points:str = ""
        for link in links:
            if (rowCount == 1):
                position = getString(link.string)
            elif (rowCount == 2):
                team = getString(link.string)
            elif (rowCount == 3):
                points = getString(link.string)
                # print (position +":" +team + ":" + points)
                teamStanding = TeamStanding(position,team,points)
                self.teamStandings.append(teamStanding)
                rowCount = 0
                position = ""
                team = ""
                points = ""
            rowCount = rowCount + 1
        for standing in self.teamStandings:
            print(standing)
        print("end Teams Standings")

    def parseDriverStandings(self):
        print("start Driver Standings")
        # html_text: str = requests.get(self.driver_standings_url).text
        html_text: str = readFile(self.driver_standings_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('td')
        print("links encontrados:" + str(len(links)))
        i:int = 1
        rowCount:int = 1
        position:str = ""
        driver:str = ""
        points:str = ""
        driverStanding: DriverStanding
        for link in links:
            if (rowCount == 1):
                position = getString(link.string)
            elif (rowCount == 2):
                driver = getString(link.string)
            elif (rowCount == 3):
                points = getString(link.string)
                # print (position +":" +driver + ":" + points)
                driverStanding = DriverStanding(position,driver,points)
                self.driverStandings.append(driverStanding)
                rowCount = 0
                position = ""
                driver = ""
                points = ""
            rowCount = rowCount + 1
        for standing in self.driverStandings:
            print(standing)
        print("end Driver Standings")


    def parseLapTimes(self,ltx:str,ltx_path:str,ltx_result:dict):
        print("start  Lap Times "+ ltx)
        # html_text: str = requests.get(self.lap_times_url).text
        html_text: str = readFile(ltx_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        lap_links:list = soup.find_all('script')
        print("links encontrados:" + str(len(lap_links)))
        value_to_find: str = "window.App="
        data: str
        json_data: Any
        pilots: list
        for link in lap_links:
            valueStr: str = str(link.string)
            if (valueStr.find(value_to_find)==0):
                data = link.string
                data = data[len(value_to_find):]
                json_data = json.loads(data)
                pilots = json_data["state"]['session']['stats']['data']
                laps: list
                for pilot in pilots:
                    number:int=pilot['carNumber']
                    driver:str=pilot['driver']['name']
                    # print(number+"-"+driver)
                    laps = pilot['laps']
                    pilotLapTimes = []
                    lapTime:LapTime
                    for lap in laps:
                        lnumber:int = lap['lap']
                        ltime: int =lap['time']
                        lapTime = LapTime(driver, number, lnumber,ltime)
                        pilotLapTimes.append(lapTime)
                        # print(str(lnumber)+":"+str(lapTime))
                    # print(number)
                    ltx_result[number] = pilotLapTimes
        for pilot in ltx_result.keys():
            print(pilot)
            for lt in ltx_result[pilot]:
                print(lt)
        print("end  Lap Times "+ ltx)

    def parseGrid(self,qx:str,qx_path:str,qx_result:list):

        print("start  "+qx)
        html_text: str = readFile(qx_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('td')
        print("links encontrados:" + str(len(links)))
        i:int = 1
        rowCount: int = 1
        position:str = ""
        number:str = ""
        driver:str = ""
        nationality:str = ""
        scuderia:str = ""
        laps:str = ""
        time:str = ""
        gap2leader:str = ""
        interval2next:str = ""
        kph:str = ""
        besttime:str = ""
        bestlap:str = ""
        for link in links:
            if (rowCount == 1):
                position = getString(link.string)
            elif (rowCount == 2):
                number = getString(link.string)
            elif (rowCount == 3):
                driver = getString(link.string)
            elif (rowCount == 4):
                nationality = getString(link.string)
            elif (rowCount == 5):
                scuderia = getString(link.string)
            elif (rowCount == 6):
                laps = getString(link.string)
            elif (rowCount == 7):
                time = getString(link.string)            
            elif (rowCount == 8):
                gap2leader = getString(link.string)
            elif (rowCount == 9):
                interval2next = getString(link.string)
            elif (rowCount == 10):
                kph = getString(link.string)
            elif (rowCount == 11):
                besttime = getString(link.string)
            elif (rowCount == 12):
                bestlap = getString(link.string)
                # print (position +":" +number + ":" + driver + ":" + nationality + ":" +  scuderia + ":" + laps + ":" + time + ":" + gap2leader + ":" + interval2next + ":" + kph + ":" + besttime + ":" + bestlap)
                sgrid = StartingGrid(position, number, driver, nationality, scuderia, laps, time, gap2leader, interval2next, kph, besttime, bestlap)
                qx_result.append(sgrid) 
                rowCount = 0
                position = ""
                number = ""
                driver = ""
                nationality = ""
                scuderia = ""
                laps = ""
                time = ""
                gap2leader = ""
                interval2next = ""
                kph = ""
                besttime = ""
                bestlap = ""
            rowCount = rowCount + 1        
        for grid in qx_result:
            print(grid)
        print("end "+qx)

    def parseRaceClassification(self):
        print("start Race Classification")
        # html_text: str = requests.get(self.race_classification_url).text
        html_text = readFile(self.race_classification_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('td')
        print("links encontrados:" + str(len(links)))
        i:int = 1
        rowCount: int = 1
        position:str = ""
        number:str = ""
        driver:str = ""
        nationality:str = ""
        scuderia:str = ""
        laps:str = ""
        time:str = ""
        gap2leader:str = ""
        interval2next:str = ""
        kph:str = ""
        besttime:str = ""
        bestlap:str = ""
        raceResult: RaceResult
        for link in links:
            if (rowCount == 1):
                position = getString(link.string)
            elif (rowCount == 2):
                number = getString(link.string)
            elif (rowCount == 3):
                driver = getString(link.string)
            elif (rowCount == 4):
                nationality = getString(link.string)
            elif (rowCount == 5):
                scuderia = getString(link.string)
            elif (rowCount == 6):
                laps = getString(link.string)
            elif (rowCount == 7):
                time = getString(link.string)            
            elif (rowCount == 8):
                gap2leader = getString(link.string)
            elif (rowCount == 9):
                interval2next = getString(link.string)
            elif (rowCount == 10):
                kph = getString(link.string)
            elif (rowCount == 11):
                besttime = getString(link.string)
            elif (rowCount == 12):
                bestlap = getString(link.string)
                raceResult = RaceResult(position, number, driver, nationality, scuderia, laps, time, gap2leader, interval2next, kph, besttime, bestlap)
                self.raceResuts.append(raceResult)
                # print (position +":" +number + ":" + driver + ":" + nationality + ":" +  scuderia + ":" + laps + ":" + time + ":" + gap2leader + ":" + interval2next + ":" + kph + ":" + besttime + ":" + bestlap)
                rowCount = 0
                position = ""
                number = ""
                driver = ""
                nationality = ""
                scuderia = ""
                laps = ""
                time = ""
                gap2leader = ""
                interval2next = ""
                kph = ""
                besttime = ""
                bestlap = ""
            rowCount = rowCount + 1                
        print("end  Race Classification")
        for race in self.raceResuts:
            print(race)

    def parseDrivers(self):
        print("start Drivers and teams")
        # html_text: str = requests.get(self.drivers_url).text
        html_text = readFile(self.drivers_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('td')
        print("links encontrados:" + str(len(links)))
        i:int = 1
        rowCount: int = 1
        number:str = ""
        driver:str = ""
        nationality:str = ""
        scuderia:str = ""
        car:str = ""
        engine:str = ""
        driver: Driver
        for link in links:
            if (rowCount == 1):
                number = getString(link.string)
            elif (rowCount == 2):
                driver = normalize(getString(link.string))
            elif (rowCount == 3):
                nationality = getString(link.string)
            elif (rowCount == 4):
                scuderia = getString(link.string)
            elif (rowCount == 5):
                car = getString(link.string)
            elif (rowCount == 6):
                engine = getString(link.string)
                # print (number + ":" + driver + ":" + nationality + ":" + ":" + scuderia + ":" + car + ":" + engine)
                driver = Driver(number,driver,nationality,scuderia,car,engine)
                team = Team(scuderia,car,engine)
                self.drivers[driver.number]=driver
                self.teams[team.name] = team
                number = ""
                driver = ""
                nationality = ""
                scuderia = ""
                car = ""
                engine = ""
                rowCount = 0
            rowCount = rowCount + 1
        # print(self.teams)
        for key in self.teams.keys():
            team:Team = self.teams[key]
            print(team)
        print()
        for key in self.drivers.keys():
            driver:Driver = self.drivers[key]
            print(driver)            
        print("end Drivers and teams")

    def parseInfo(self):
        print("start")
        # html_text: str = requests.get(self.drivers_url).text
        html_text = readFile(self.drivers_path)
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('h1')
        print("links encontrados:" + str(len(links)))
        i:int = 1
        rowCount: int = 1
        gp:str = ""
        date:str = ""
        round:str = ""
        total:str = "" 
        circuit:str= ""
        self.gpInfo = None
        for link in links:
            if (type(link.get('class')) is not type(None)):
                if (link.get('class')[0] == 'qQR9k'):
                    gp = link.text

        linksDate:list = soup.find_all('div',class_='_3G-GS')
        print("links encontrados:" + str(len(links)))
        rowCount = 1
        for link in linksDate:
            if (type(link.get('class')) is not type(None)):
                if (link.get('class')[0] == '_3G-GS'):
                    if (rowCount == 1):
                        date = link.text
                    if (rowCount == 2):
                        round = link.text
                    if (rowCount == 3):
                        total = link.text
                    if (rowCount == 4):
                        circuit = link.text
                    rowCount = rowCount + 1
        self.gpInfo = GpInfo(gp,circuit,date,round,total)
        print(self.gpInfo)
        print("end") 
        print("-----------------")
        
    def export2Yml(self, gppath):
        print("-----------------")
        print(self.gpInfo)
        print("-----------------")
        self.gpInfo.toYml(gppath)
        print("-------FIN----------")

    def export2Json(self, gppath):
        path_gpinfo : str = "2022export/gpinfo"
        print("------GPINFO-----------")
        print(self.gpInfo)
        print("-----------------")
        json_gpinfo: str = self.gpInfo.toJson()
        file_gpinfo = open(path_gpinfo+gppath+".json", "w")
        file_gpinfo.write(json_gpinfo)
        file_gpinfo.close()

        print("------DRIVERS-----------")
        print(self.drivers)
        drivers_str: str = "{\"drivers\": ["

        for key in self.drivers.keys():
            driver: Driver = self.drivers[key]
            print(driver)
            json: str = driver.toJson(gppath)
            drivers_str += json
            drivers_str += ","
        drivers_str = drivers_str[:-1] # remove last ,
        drivers_str += "]}"
        print(drivers_str)
        path_drivers : str = "2022export/drivers"
        file_drivers = open(path_drivers+gppath+".json", "w")
        file_drivers.write(drivers_str)
        file_drivers.close()

        print("------LAP CHART-----------")
        print(self.lapCharts)

        lapchart_str: str = "{"
        for lap in self.lapCharts:
            lapchart_str += lap.toJson()
            lapchart_str += ","
        lapchart_str = lapchart_str[:-1] # remove last ,
        lapchart_str += "}"
        print(lapchart_str)

        path_lapchart : str = "2022export/lapchart"
        file_lapchart = open(path_lapchart+gppath+".json", "w")
        file_lapchart.write(lapchart_str)
        file_lapchart.close()


        print("------LAP TIME-----------")
        laptime_str: str = "{"
        for pilot in self.lapTimes.keys():
           print(pilot)
           laptime_str += "\"" + pilot + "\":["
           for lt in self.lapTimes[pilot]:
               laptime_str += str(lt.time) + ","
           laptime_str = laptime_str[:-1] # remove last ,           
           laptime_str += "],"
        laptime_str = laptime_str[:-1] # remove last ,           
        laptime_str += "}"
        print(laptime_str)

        path_laptime : str = "2022export/laptime"
        file_laptime = open(path_laptime+gppath+".json", "w")
        file_laptime.write(laptime_str)
        file_laptime.close()

        print("------Starting Grid-----------")
        starting_grid: str = "["
        for grid in self.startingGrids:
            starting_grid += grid.toJson()
            starting_grid += ","
        starting_grid = starting_grid[:-1] # remove last ,           
        starting_grid += "]"
        print(starting_grid)        
        path_starting_grid : str = "2022export/starting_grid"
        file_starting_grid = open(path_starting_grid+gppath+".json", "w")
        file_starting_grid.write(starting_grid)
        file_starting_grid.close()

        print("------Pit Stops-----------")
      
        pits_str: str = "{"
        for pit in self.pitStops.keys():
           print(pit)
           pits_str += "\"" + pit + "\":["
           for pt in self.pitStops[pit]:
               pits_str += pt.toJson()
               pits_str += ","
           pits_str = pits_str[:-1] # remove last ,           
           pits_str += "],"
        pits_str = pits_str[:-1] # remove last ,           
        pits_str += "}"
        print(pits_str)
        path_pits : str = "2022export/pit_stops"
        file_pits = open(path_pits+gppath+".json", "w")
        file_pits.write(pits_str)
        file_pits.close()        


        print("------Tyres-----------")
        
        tyres_str: str = "{"
        for tyre in self.tyres.keys(): 
           print(tyre)
           tyres_str += "\"" + tyre + "\":["
           for ty in self.tyres[tyre]:
               tyres_str += ty.toJson()
               tyres_str += ","
           tyres_str = tyres_str[:-1] # remove last ,           
           tyres_str += "],"
        tyres_str = tyres_str[:-1] # remove last ,           
        tyres_str += "}"
        print(tyres_str)
        path_tyres : str = "2022export/tyres"
        file_tyres = open(path_tyres+gppath+".json", "w")
        file_tyres.write(tyres_str)
        file_tyres.close()

        print("-------FIN----------")

