import requests
from bs4 import BeautifulSoup


drivers_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix"
race_classification_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification"


def main():
    print("Parsing drivers in: " +  drivers_url)
    #parseDrivers1()
    parseDriversNumbers()


def parseDriversNumbers():
    print("start")
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
            number = link.string
        elif (rowCount == 2):
            driver = link.string
        elif (rowCount == 3):
            nationality = link.string
        elif (rowCount == 4):
            scuderia = link.string
        elif (rowCount == 5):
            car = link.string
        elif (rowCount == 6):
            engine = link.string
            print (number + ":" + driver + ":" + nationality + ":" + ":" + scuderia + ":" + car + ":" + engine)
            rowCount = 0
        rowCount = rowCount + 1        
    print("end")

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