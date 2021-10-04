import json
from datetime import datetime
from datetime import timedelta
from dataclasses import dataclass
import requests

## Global Variable Declaration:###
weatherDeCoded = []             ##
holidayObjectsList = []         ##
dictOfHolidays = {}             ##
deleted = 0                     ##
##################################

def deleteprint(decoratedfunc):
    def inner_fn(*args, **kwargs):
        print("Deleting the %s from the stored holidays" % str(args[1]))
        evaluated = decoratedfunc(*args, **kwargs)
        return evaluated
    return inner_fn


## Each input checker uses a try-except pair to avoid program errors due to invalid inputs.
## User-input authenticators##########################################
                                                                    ##
def inputyn(string):                                                ##
    invalidInput = True                                             ##
    while invalidInput:                                             ##
        try:                                                        ##
            userinput = str(input(string))                          ##
            if userinput == 'y' or userinput == 'n':                ##
                invalidInput = False                                ##
            else:                                                   ##
                print("Invalid input: Not in the form of y or n!")  ##
        except:                                                     ##
            print("Invalid input: Not a string")                    ##
    return userinput                                                ##
######################################################################
def inputint(string):                                               ##
    invalidInput = True                                             ##
    while invalidInput:                                             ##
        try:                                                        ##
            userinput = int(input(string))                          ##
            invalidInput = False                                    ##
        except:                                                     ##
            print("Invalid input: Not a integer")                   ##
    return userinput                                                ##
######################################################################
def inputstr(string):                                               ##
    invalidInput = True                                             ##
    while invalidInput:                                             ##
        try:                                                        ##
            userinput = str(input(string))                          ##
            invalidInput = False                                    ##
        except:                                                     ##
            print("Invalid input: Not a string")                    ##
    return userinput                                                ##
######################################################################

## Creates the class object "Holiday" that is used to store each holiday as object.
@dataclass
class Holidays:
    holidayName: str
    holidayDate: str
    @property
    def holidayname(self):
        return self.holidayName

    @property
    def holidaydate(self):
        return self.holidayDate

    def __str__(self):
        return self.holidayName + " " + str(self.holidayDate)

## Used to load in the initial holidayStarter.json file as save it as a dictionary of holidays.
def openInitialFile():
    global dictOfHolidays
    with open(r"C:\Users\Eddy Doering\PycharmProjects\Assessment7\venv\holidaysStarter.json") as infile1:
         dictOfHolidays = json.load(infile1)

## Used to load in the scrapped data from the HolidayScraper.py program and store merge it with the initial file.
def openScrapedFile():
    global dictOfHolidays
    with open(r"C:\Users\Eddy Doering\PycharmProjects\Assessment7\venv\HolidaysScraped.json") as infile2:
        jsonFile2 = json.load(infile2)
    dictOfHolidays['holidays'].extend(jsonFile2)
    # dictOfHolidays = json.dumps(dictOfHolidays, indent=4)

def initilizeholidays():
    global holidayObjectsList
    holidayObjectsList = []
    holidayObjects = dictOfHolidays["holidays"]
    for index in range(len(holidayObjects)):
        holidayObjectsList.insert(index, 'holidayItem' + str(index))
        # print(holidayObjectsList[index])
        for key in holidayObjects[index]:
            holidayObjectsList[index] = Holidays(holidayObjects[index]["name"], holidayObjects[index]["date"])
            # print (holidayObjects[index][key])
    # print(holidayObjectsList[0].holidayName)
    # print(holidayObjectsList[0].holidayDate)
    # print(holidayObjectsList)

def findobject(find):
    for index in range(len(holidayObjectsList)):
        if holidayObjectsList[index].holidaydate == find:
            found = holidayObjectsList[index].holidayname
    return found
def apicall():
    global weatherDeCoded
    response = requests.get('https://api.tomorrow.io/v4/timelines?location=44.986656,-93.258133&fields=weatherCode&timesteps=1d&units=metric&apikey=iNmVrPeULGBSY7hAG8r90w9oA4lzIPEz')
    weatherDic = response.json()
    weatherCode = []
    for i in range(len(weatherDic['data']['timelines'][0]['intervals'])):
        weatherCode.append(weatherDic['data']['timelines'][0]['intervals'][i]['values']['weatherCode'])
    for i in range(len(weatherCode)):
        if weatherCode[i] == 0:
            weatherDeCoded.insert(i, "unknown")
        if weatherCode[i] == 1000:
            weatherDeCoded.insert(i, "clear")
        if weatherCode[i] == 1001:
            weatherDeCoded.insert(i, "cloudy")
        if weatherCode[i] == 1100:
            weatherDeCoded.insert(i, "mostly clear")
        if weatherCode[i] == 1101:
            weatherDeCoded.insert(i, "partially cloudy")
        if weatherCode[i] == 1102:
            weatherDeCoded.insert(i, "mostly cloudy")
        if weatherCode[i] == 2000:
            weatherDeCoded.insert(i, "fog")
        if weatherCode[i] == 2100:
            weatherDeCoded.insert(i, "light fog")
        if weatherCode[i] == 3000:
            weatherDeCoded.insert(i, "breezy")
        if weatherCode[i] == 3001:
            weatherDeCoded.insert(i, "windy")
        if weatherCode[i] == 3002:
            weatherDeCoded.insert(i, "strong wind")
        if weatherCode[i] == 4000:
            weatherDeCoded.insert(i, "drizzle")
        if weatherCode[i] == 4001:
            weatherDeCoded.insert(i, "rain")
        if weatherCode[i] == 4200:
            weatherDeCoded.insert(i, "light rain")
        if weatherCode[i] == 4201:
            weatherDeCoded.insert(i, "heavy rain")
        if weatherCode[i] == 5000:
            weatherDeCoded.insert(i, "snow")
        if weatherCode[i] == 5001:
            weatherDeCoded.insert(i, "flurries")
        if weatherCode[i] == 5100:
            weatherDeCoded.insert(i, "light snow")
        if weatherCode[i] == 5101:
            weatherDeCoded.insert(i, "heavy snow")
        if weatherCode[i] == 6000:
            weatherDeCoded.insert(i, "freezing drizzle")
        if weatherCode[i] == 6001:
            weatherDeCoded.insert(i, "freezing rain")
        if weatherCode[i] == 6200:
            weatherDeCoded.insert(i, "light freezing rain")
        if weatherCode[i] == 6201:
            weatherDeCoded.insert(i, "heavy freezing rain")
        if weatherCode[i] == 7000:
            weatherDeCoded.insert(i, "ice pellets")
        if weatherCode[i] == 7101:
            weatherDeCoded.insert(i, "heavy ice pellets")
        if weatherCode[i] == 7102:
            weatherDeCoded.insert(i, "light ice pellets")
        if weatherCode[i] == 8000:
            weatherDeCoded.insert(i, "thunderstorm")
def startup():
    print('''
--------------------------------------------------------|
HOLIDAY MANAGEMENT SYSTEM (HMS 1.1)                     |
--------------------------------------------------------|
    ''')
    print("Currently there are", len(holidayObjectsList), "holidays stored in the system")

def mainmenu():
    print('''
--------------------------------------------------------|
MAIN HOLIDAY MENU                                       |
--------------------------------------------------------|
1. add a holiday
2. remove a holiday
3. save a holiday list
4. view holidays
5. exit
    ''')
    print("Currently there are", len(holidayObjectsList), "holidays stored in the system")

def holidayadd():
    print('''
--------------------------------------------------------|
ADD HOLIDAY                                             |
--------------------------------------------------------|
        ''')
    newHolidayName = inputstr("Enter holiday name: ")
    invalidDate = True
    while invalidDate:
        newHolidayDate = inputstr("enter date in format yyyy-mm-dd: ")
        try:
            x = datetime.strptime(newHolidayDate, '%Y-%m-%d')
            invalidDate = False
        except:
            print("Invalid input: not in format yyyy-mm-dd, please try again")
    index = len(holidayObjectsList)
    newHoliday = Holidays(newHolidayName, newHolidayDate)
    newHolidayList = [newHoliday]
    holidayObjectsList.extend(newHolidayList)
    print("Success, the holiday: ", holidayObjectsList[index].holidayName, " has been added")
@deleteprint
def deleteobject(holidayObjectList,removeHoliday):
    global holidayObjectsList
    deletedObject = False
    for i in range(len(holidayObjectsList)):
        if holidayObjectsList[i].holidayName.lower() == removeHoliday:
            holidayObjectsList.pop(i)
            deletedObject = True
            print("Deletion Successful!")
            break
    if deletedObject is False:
        print(removeHoliday, " was not found, try a different input or check the list for correct spelling")
    #return holidayObjectList
def holidayremove():
    print('''
--------------------------------------------------------|
REMOVE HOLIDAY                                          |
--------------------------------------------------------|
            ''')
    removeHoliday = inputstr("Select Holiday to be removed: ").lower()
    deleteobject(holidayObjectsList,removeHoliday)

def listsave():
    print("Saving holiday list to JSON file.")
    listDict = []
    for i in range(len(holidayObjectsList)):
        dict = {}
        dict["name"] = holidayObjectsList[i].holidayName
        dict["date"] = holidayObjectsList[i].holidayDate

        listDict.append(dict)
    listJSON = json.dumps(listDict, indent=4)
    #print(listJSON)
    with open(r"C:\Users\Eddy Doering\PycharmProjects\Assessment7\SavedHolidaysList.json", 'w') as outfile:
        outfile.write(listJSON)
def holidayview():
    global holidayObjectsList
    print('''
--------------------------------------------------------|
VIEW HOLIDAYS                                           |
--------------------------------------------------------|
    ''')
    invalidSelectView = True
    while invalidSelectView:
        today = datetime.today().isocalendar()[1]
        selectYear = inputint("Which year: ")
        print("todays week is: ", today+1, "enter this for weather forecast")
        selectWeek = inputint("Which week? [1-52]: ")
        if 1 <= selectWeek <= 52 and 2021 <= selectYear <= 2024:
            invalidSelectView = False
        else:
            print("Invalid input: Please select a year between 2021 and 2024 and a week between 1 and 52")
    if selectWeek == today:
        apicall()
    # holidayWeekList = []
    # holidayYearList = []
    holidayObjectsListFiltered1 = filter(lambda x: datetime.strptime(x.holidayDate, '%Y-%m-%d').year == selectYear,
                                         holidayObjectsList)
    holidayObjectsListFiltered2 = filter(
        lambda x: datetime.strptime(x.holidayDate, '%Y-%m-%d').isocalendar()[1] == selectWeek,
        holidayObjectsListFiltered1)
    holidayObjectsListFiltered2 = list(holidayObjectsListFiltered2)
    print('-------------------------------------------------------- |')
    for index in range(len(holidayObjectsListFiltered2)):
        print(holidayObjectsListFiltered2[index])
    print('-------------------------------------------------------- |')
    if selectWeek == today+1:
        apicall()
        date = datetime.today().date()
        for i in range(7):
            print(date + timedelta(days=i), "   ", weatherDeCoded[i])
    # for i in range(len(holidayObjectsList)):
    #     holidayWeekList.insert(i, datetime.strptime(holidayObjectsList[i].holidayDate, '%Y-%m-%d').isocalendar()[1])
    #     holidayYearList.insert(i, datetime.strptime(holidayObjectsList[i].holidayDate, '%Y-%m-%d').year)
    #     if holidayWeekList[i] == 53:
    #         holidayWeekList[i] = 1
    #     if holidayWeekList[i] == selectWeek and holidayYearList[i] == selectYear:
    #         print(holidayObjectsList[i].holidaydate)


def exit():
    global selectStartUp
    exityn = inputyn("Are you sure you want to exit? [y/n]: ")
    if exityn == "y":
        selectStartUp = "z"


## open and save to variable a initial .json file as a dictionary with a list of dictionaries with name, and date being keys to each holidays name and date of occurrence as values.
openInitialFile()
## open and save to variable a scraped .json file as a list of dictionaries with the same key-value pair setup as previous file.
openScrapedFile()
## Initialize the main program here by appending scrapped data to initial data and creating a class object for holidays.
initilizeholidays()

## Start user input and begin printing displays.
selectStartUp = inputyn("Do you want to start the super cool holiday management system? [y/n]: ")

## User interface print statements:
startup()
mainmenu()

## Main program while loop. This loop keeps the program cycling until the exit menu option has been chosen.
while selectStartUp == "y":
    print()
    selectMainMenu = inputint("Please select an option from the above menu: ")

    ## Main menu selection options. Refer to individual function decorations for insights into functionality.
    if selectMainMenu == 1:         ## Summarized functionality:
        holidayadd()                ## Adds a new holiday to the global variable that tracks holiday objects
    if selectMainMenu == 2:
        holidayremove()             ## Removes a existing holiday from the global variable that tracks holiday objects
    if selectMainMenu == 3:
        listsave()                  ## Saves file as a .json
    if selectMainMenu == 4:
        holidayview()               ## Lists holiday objects based on user input.
    if selectMainMenu == 5:
        exit()                      ## Exits program.
    if 1 > selectMainMenu < 5:
        print("input invalid: Please enter a number between 1 and 5")
if selectStartUp == "n":
    print("okay, smartass! Go shove it where the sun don't shine because this application is daBOMB!")
else:
    print("program exit successful")
