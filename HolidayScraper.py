from bs4 import BeautifulSoup
from datetime import datetime
import json
import requests

def jsonDumperHelper():
    for i in range(len(holidays)):
        holidays[i]['date'] = str(holidays[i]['date'])
    holidaysJSON = json.dumps(holidays, indent=4)
    with open(r"C:\Users\Eddy Doering\PycharmProjects\Assessment7\venv\HolidaysScraped.json", "w") as outfile:
        outfile.write(holidaysJSON)
def getHTML(url):
    response = requests.get(url)
    return response.text
#print(getHTML("https://www.countrycode.org").status_code)

response = requests.get("https://www.timeanddate.com/holidays/us/")

print(response)
print(response.status_code)
html = getHTML("https://www.timeanddate.com/holidays/us/")

soup = BeautifulSoup(html, "html.parser")

#table = soup.find('table', attrs = {'id': 'holidays-table'})
table = soup.find('tbody')
#print(table)
holidays = []
holidayNames = []
for row in table.find_all_next('tr'):
    holiday = {}
    name = row.find_next('a').string
    holiday['name'] = name
    if name not in holidayNames and name != 'let us know':
        holidayNames.append(name)
        if row.find_next('th'):
            holiday['date'] = datetime.strptime(row.find_next('th').string + ' 2021','%b %d %Y').date()
        holidays.append(holiday)
#print(holidays)
jsonDumperHelper()
