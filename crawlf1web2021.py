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

class Crawlf1web2021:

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

    def __init__(self, drivers_html_path, race_classification_path, practice1_path, practice2_path, 
                practice3_path, q1_path, q2_path, q3_path, q1_laptimes_path, q2_laptimes_path, q3_laptimes_path,starting_grid_path, driver_standings_path, teams_standings_path,
                pit_stops_path,fastest_laps_path,lap_chart_path,lap_times_path,tyres_path):
        
        self.drivers_html_path = drivers_html_path
        self.race_classification_path = race_classification_path
        self.practice1_path = practice1_path
        self.practice2_path = practice2_path
        self.practice3_path = practice3_path
        self.q1_path = q1_path
        self.q2_path = q2_path
        self.q3_path = q3_path
        self.q1_laptimes_path = q1_laptimes_path
        self.q2_laptimes_path = q2_laptimes_path
        self.q3_laptimes_path = q3_laptimes_path
        self.starting_grid_path = starting_grid_path
        self.driver_standings_path = driver_standings_path
        self.teams_standings_path = teams_standings_path
        self.pit_stops_path = pit_stops_path
        self.fastest_laps_path = fastest_laps_path
        self.lap_chart_path = lap_chart_path
        self.lap_times_path = lap_times_path
        self.tyres_path = tyres_path

    
    def load(self):
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
        self.parseLapTimes("Race",self.lap_times_path,self.lapTimes)
        self.parseTyres()

    def exportData(self,gppath):
        print("Export data")
        self.exportInfo(gppath)

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
                            # print("piloto:"+nomDriver)
                        elif (index>0):
                            stint:Stint = Stint(None, "",0,0)
                            stint.driver = nomDriver
                            if (data):
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
                    # print(stints)
                    for stint in stints:
                        print(stint)
        print("end  Tyres")

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
        for fL in self.fastestLaps:
            print(fL)
        print("end Fastest Laps")
    
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

    def parseInfo(self):
        print("start")
        # html_text: str = requests.get(self.drivers_url).text
        html_text = readFile(self.drivers_html_path)
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

        print("-------FIN----------")

