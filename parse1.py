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
    for link in links:
        print(link.get('class'))
        print(link.string)
        

if __name__ == "__main__":
    main()  