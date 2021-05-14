from typing import Type
import requests
from bs4 import BeautifulSoup
from bs4.element import Script
from utils import *


drivers_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix"
race_classification_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification"
starting_grid_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/9bb465b8-a1d7-4d67-beaf-c6b7a310d65a"
driver_standings_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/drivers"
teams_standings_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/teams"
pit_stops_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=PitStop"
fastest_laps_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=FastestLap"
lap_chart_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapChart"
lap_times_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapTime"


def main():
    #parseDrivers1()
    #parseDrivers()
    #parseRaceClassification()
    #parseStartingGrid()
    #parseDriverStandings()
    #parseTeamsStandings()
    #parsePitStop()
    #parseFastestLaps()
    #parseLapChart()
    parseLapTimes()


def parseLapTimes():
    print("start  Lap Chart")
    html_text: str = requests.get(lap_times_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    print("parseado:"+ soup.title.string)
    print("---------------------")
    lap_links:list = soup.find_all('script')
    print("links encontrados:" + str(len(lap_links)))
    s: str = "This be a string"
    if s.find("is") == -1:
        print("No 'is' here!")
    else:
        print("Found 'is' in the string.")
    for link in lap_links:
        valueStr: str = str(link.string)
        if (valueStr.find("window.App")==0):
            print(link.string)

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
        print()
        for j in range(20):
            if (j==0):
                lap = getString(lap_links[lap_index].string)
                print(lap+":", end='')
            number = getString(positions[i+(j*len(lap_links))].string)
            print(number, end=',')
            if (j==20):
                print()
        lap_index= lap_index +1     
    print()
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
            print (position +":" + number +":" +driver + ":" + team + ":" + time + ":" + lap + ":" + gap )
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
            print (number +":" +driver + ":" + team + ":" + lap + ":" + stop + ":" + time + ":" + timeTotal)
            rowCount = 0
            number = ""
            driver = ""
            team = ""
            lap = ""
            stop = ""
            time = ""
            timeTotal = ""
        rowCount = rowCount + 1
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
            print (position +":" +team + ":" + points)
            rowCount = 0
            position = ""
            team = ""
            points = ""
        rowCount = rowCount + 1
    
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
    for link in links:
        if (rowCount == 1):
            position = getString(link.string)
        elif (rowCount == 2):
            driver = getString(link.string)
        elif (rowCount == 3):
            points = getString(link.string)
            print (position +":" +driver + ":" + points)
            rowCount = 0
            position = ""
            driver = ""
            points = ""
        rowCount = rowCount + 1
    
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
            print (position +":" +number + ":" + driver + ":" + nationality + ":" +  scuderia + ":" + laps + ":" + time + ":" + gap2leader + ":" + interval2next + ":" + kph + ":" + besttime + ":" + bestlap)
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
            print (position +":" +number + ":" + driver + ":" + nationality + ":" +  scuderia + ":" + laps + ":" + time + ":" + gap2leader + ":" + interval2next + ":" + kph + ":" + besttime + ":" + bestlap)
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

def parseDrivers():
    print("start Drivers")
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
            print (number + ":" + driver + ":" + nationality + ":" + ":" + scuderia + ":" + car + ":" + engine)
            number = ""
            driver = ""
            nationality = ""
            scuderia = ""
            car = ""
            engine = ""
            rowCount = 0
        rowCount = rowCount + 1        
    print("end Drivers")

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
                    rowCount = 0
                rowCount = rowCount + 1
        #print(i)
        #print(rowCount)
        i = i + 1
    print("end")   

if __name__ == "__main__":
    main()  