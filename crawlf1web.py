from typing import Any, Type
import requests
import json
from bs4 import BeautifulSoup
from bs4.element import Script
from driverStanding import DriverStanding
from fastestlap import FastestLap
from lapchart import LapChart
from pitStop import PitStop
from raceresult import RaceResult
from startinggrid import StartingGrid
from teamStanding import TeamStanding
from utils import *
from driver import *
from team import *

drivers_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix"
race_classification_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification"
starting_grid_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/9bb465b8-a1d7-4d67-beaf-c6b7a310d65a"
driver_standings_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/drivers"
teams_standings_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/teams"
pit_stops_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=PitStop"
fastest_laps_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=FastestLap"
lap_chart_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapChart"
lap_times_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapTime"
tyres_url: str = "https://www.racefans.net/2021/03/29/2021-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/"

drivers:dict = dict() 
teams:dict = dict() 
raceResuts = []
startingGrids = []
driverStandings = []
teamStandings = []
pitStops:dict = dict()
fastestLaps = []
lapCharts = []
def main():
    # parseDrivers1()
    # parseDrivers()
    # parseRaceClassification()
    # parseStartingGrid()
    # parseDriverStandings()
    # parseTeamsStandings()
    # parsePitStop()
    # parseFastestLaps()
    parseLapChart()
    # parseLapTimes()
    # parseTyres()

def parseTyres():

    print("start  Tyres")
    html_text: str = requests.get(tyres_url).text
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
                for stint in stints:
                    print(stint.string,end=' ')
                print()


def parseLapTimes():
    print("start  Lap Chart")
    html_text: str = requests.get(lap_times_url).text
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
                print(pilot['carNumber']+"-"+pilot['driver']['name'])
                laps = pilot['laps']
                for lap in laps:
                    print(str(lap['lap'])+":"+str(lap['time']))


    print("end  Lap Times")

def parseLapChart():
    print("start  Lap Chart")
    html_text: str = requests.get(lap_chart_url).text
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
            print(number, end=',')
            # if (j==20):
            #    print()
        lap_index= lap_index +1
        lapCharts.append(lapChart)
    # print()
    for lc in lapCharts:
        print(lc)
    print("end  Lap Chart")
def parseFastestLaps():
    print("start  Fastest Laps")
    html_text: str = requests.get(fastest_laps_url).text
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
            fastestLaps.append(fastestLap)
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
    for fL in fastestLaps:
        print(fL)

def parsePitStop():
    print("start  Pit Stops")
    html_text: str = requests.get(pit_stops_url).text
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
            pitStopList = pitStops.get(number)
            if (pitStopList == None):
                pitStopsListTmp = []
                pitStopsListTmp.append(pitStop)
                pitStops[number] = pitStopsListTmp
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
    for pitStopKey in pitStops.keys():
        for pitStoptmp in pitStops[pitStopKey]:
          print(pitStoptmp)
    print("end Pit Stops")

def parseTeamsStandings():
    print("start Teams Standings")
    html_text: str = requests.get(teams_standings_url).text
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
            teamStandings.append(teamStanding)
            rowCount = 0
            position = ""
            team = ""
            points = ""
        rowCount = rowCount + 1
    for standing in teamStandings:
        print(standing)
    print("end Teams Standings")

def parseDriverStandings():
    print("start Driver Standings")
    html_text: str = requests.get(driver_standings_url).text
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
            driverStandings.append(driverStanding)
            rowCount = 0
            position = ""
            driver = ""
            points = ""
        rowCount = rowCount + 1
    for standing in driverStandings:
        print(standing)
    print("end Driver Standings")
def parseStartingGrid():
    print("start Starting Grid")
    html_text: str = requests.get(starting_grid_url).text
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
            startingGrids.append(startingGrid) 
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
        for grid in startingGrids:
            print(grid)

    print("End Starting Grid")
def parseRaceClassification():
    print("start Race Classification")
    html_text: str = requests.get(race_classification_url).text
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
            raceResuts.append(raceResult)
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
    for race in raceResuts:
        print(race)

def parseDrivers():
    print("start Drivers and teams")
    html_text: str = requests.get(drivers_url).text
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
            drivers[driver.number]=driver
            teams[team.name] = team
            number = ""
            driver = ""
            nationality = ""
            scuderia = ""
            car = ""
            engine = ""
            rowCount = 0
        rowCount = rowCount + 1
    print(teams)
    print("end Drivers and teams")

def parseDrivers1():
    print("start")
    html_text: str = requests.get(drivers_url).text
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
                    drivers[driver.name]=driver
                    rowCount = 0
                rowCount = rowCount + 1
        #print(i)
        #print(rowCount)
        i = i + 1
    print("end") 
    print("-----------------")
    #print(drivers)  

if __name__ == "__main__":
    main()  