import requests
from bs4 import BeautifulSoup


web_url: str = "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix"
def main():
    print("Hello Word")
    print("Empezando function")
    parse1()


def parse1():
    print("parseando")
    html_text: str = requests.get(web_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    print("parseado:"+ soup.title.string)
    print("---------------------")
    links:list = soup.find_all('a')
    print("links encontrados:" + str(len(links)))
    i:int = 1
    rowCount: int = 1
    maxRowElements: int = 3
    name:str = ""
    country:str = ""
    scuderia:str = ""
    for link in links:
        if (type(link.get('class')) is not type(None)):
            if (link.get('class')[0] == '_1TRrV'):
                if rowCount == 1:
                    name = print(link.string)
                elif rowCount == 2:
                    country = print(link.string)
                elif rowCount == 3:
                    scuderia = print(link.string)
                    print (name + ":" + country + ":" + scuderia)
                    rowCount = 0
        print(i)
        print(rowCount)
        i = i + 1
        rowCount = rowCount + 1

if __name__ == "__main__":
    main()  