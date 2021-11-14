from typing import Any, Type
import requests
import json
from bs4 import BeautifulSoup
from bs4.element import Script
from driverStanding import DriverStanding
from fastestlap import FastestLap
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

class Crawlf1web2021:

    drivers:dict = dict() 
    teams:dict = dict() 
    raceResuts = []
    startingGrids = []
    driverStandings = []
    teamStandings = []
    pitStops:dict = dict()
    fastestLaps = []
    lapCharts = []
    lapTimes:dict = dict()
    tyres:dict = dict()

    def __init__(self, drivers_html_path, race_classification_path, starting_grid_path, driver_standings_path, teams_standings_path,
                pit_stops_path,fastest_laps_path,lap_chart_path,lap_times_path,tyres_path):
        
        self.drivers_html_path = drivers_html_path
        self.race_classification_path = race_classification_path
        self.starting_grid_path = starting_grid_path
        self.driver_standings_path = driver_standings_path
        self.teams_standings_path = teams_standings_path
        self.pit_stops_path = pit_stops_path
        self.fastest_laps_path = fastest_laps_path
        self.lap_chart_path = lap_chart_path
        self.lap_times_path = lap_times_path
        self.tyres_path = tyres_path

    
    def load(self):
        # self.parseDrivers1()
        self.parseDrivers()
        self.parseRaceClassification()
        self.parseStartingGrid()
        self.parseDriverStandings()
        self.parseTeamsStandings()
        self.parsePitStop()
        self.parseFastestLaps()
        self.parseLapChart()
        self.parseLapTimes()
        self.parseTyres()

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
                            # print(key)
                        elif (index>0):
                            stint:Stint = Stint(None, None, None,None)
                            stint.driver = nomDriver
                            tyre = data.split()
                            stint.tyre = tyre[0]
                            stint.laps = tyre[1]
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
                    for stint in stints:
                        print(stint)


    def parseLapTimes(self):
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
        html_text: str = readFile(self.lap_chart_path)
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
        print("end Fastest Laps")
        for fL in self.fastestLaps:
            print(fL)

    def parsePitStop(self):
        print("start  Pit Stops")
        # html_text: str = requests.get(self.pit_stops_url).text
        html_text: str = readFile(self.pit_stops_path)
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
        html_text: str = readFile(self.teams_standings_path)
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

    def parseStartingGrid(self):
        print("start Starting Grid")
        # html_text: str = requests.get(self.starting_grid_url).text
        html_text = readFile(self.starting_grid_path)
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
        startingGrid: StartingGrid
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
                startingGrid = StartingGrid(position, number, driver, nationality, scuderia, laps, time, gap2leader, interval2next, kph, besttime, bestlap)
                self.startingGrids.append(startingGrid) 
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
            for grid in self.startingGrids:
                print(grid)

        print("End Starting Grid")
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
        html_text = readFile(self.drivers_html_path)
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
                driver = getString(link.string)
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

    def parseDrivers1(self):
        print("start")
        html_text: str = requests.get(self.drivers_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        print("parseado:"+ soup.title.string)
        print("---------------------")
        links:list = soup.find_all('a')
        print("links encontrados:" + str(len(links)))
        i:int = 1
        rowCount: int = 1
        name:str = ""
        country:str = ""
        scuderia:str = ""
        driver:Driver    
        for link in links:        
            if (type(link.get('class')) is not type(None)):
                if (link.get('class')[0] == '_1TRrV'):
                    if (rowCount == 1):
                        name = link.string
                    elif (rowCount == 2):
                        country = link.string
                    elif (rowCount == 3):
                        scuderia = link.string
                        print (name + ":" + country + ":" + scuderia)
                        driver = Driver(name,country,None,scuderia,None,None)
                        #print(driver)
                        self.drivers[driver.name]=driver
                        rowCount = 0
                    rowCount = rowCount + 1
            #print(i)
            #print(rowCount)
            i = i + 1
        print("end") 
        print("-----------------")
        #print(drivers)  
