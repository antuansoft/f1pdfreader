
# Static module utils, functions with utils

from driver import Driver


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
        surname=nameParts[len(nameParts)-1]
        # print(surname)
        if surname in name:
            return key
    return None