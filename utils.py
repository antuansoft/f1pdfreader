
# Static module utils, functions with utils

from driver import Driver
from os.path import exists
import requests
from os import makedirs
from posixpath import dirname

# read a String excluding null value
def getString(value: str) -> str:
    if (value == None):
        return "---"
    else:
        return value

# get the driver number based on driver name and the dict of drivers
def getdriverId(driver: str, drivers:dict)->int:
    for key in drivers.keys():
        name:str=drivers[key].name
        nameParts = driver.split()
        surname=nameParts[1]
        if surname in name:
            return key
    return None

# read file and return text
def readFile(filePath:str)->str:
    f = open(filePath, "r")
    return f.read()

# Downlad Url and return html string
def downloadUrl(url:str)->str:
    if (url != ""):
        print("download:"+url)
        html_text: str = requests.get(url).text
        print("downloaded")
        return html_text
    else:
        print("No existe")
        return ""

def saveWeb(webHtml:str,pathToFile:str):
    
    if (webHtml!=""):
        file_exists = exists(pathToFile)
        if (not file_exists):
            makedirs(dirname(pathToFile),0o777,True)
            f = open(pathToFile,"w")
            f.write(webHtml)
            f.close()
            print(pathToFile + " saved")
        else:
            print(pathToFile + " already exits.")

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ä", "a"),
        ("ë", "e"),
        ("ï", "i"),
        ("ö", "o"),
        ("ü", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def normalize_number(s):
    replacements = (
        ("(", ""),
        (")", ""),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s