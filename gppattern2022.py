


from crawlf1web2022 import Crawlf1web2022
from utils import *

gppath:str= "_xxxxx2022"


class xxxx2022:

    def __init__(self) -> None:
        
        print("Generating xxxx2022")
        bahrain2022 = Crawlf1web2022(gppath,
                                     "https://fiaresultsandstatistics",
                                     "https://www.racefans.net")
        
        bahrain2022.loadUrls()
        bahrain2022.loadWebPages()
        bahrain2022.parseUrls()
        bahrain2022.exportData(gppath)

