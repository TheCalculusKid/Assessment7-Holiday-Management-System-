--------------------------------------------------------|
Welcome to the super cool holiday management system 1.1 |
--------------------------------------------------------|

INTRODUCTION:

This project comes in two parts.

1)  The Holiday Scraper (HolidayScraper.py) that scrapes holiday dates off of the website
    https://www.timeanddate.com/holidays/us/ and stores it in a .json file, called HolidaysScraped.json. This
    scraper can easily be repurposed to scrape data for other years, for a proof of form the year 2021 has been scraped
    but a simple change of the https and a couple small modifications to the code.

2)  The second part is holiday management system itself or HMS. This program stores an initial dictionary of holidays
    called holidayStarter.json and merges the scraped data with this json dictionary. It stores this data in as an
    object using classes in python. The HMS has four main functionalities:

            1. Adding a new holiday object
            2. Remove an existing holiday object
            3. Save the current holiday objects to a .json file
            4. View the holiday objects based on year and week of year [1-52]

USE:
1) Load all files into a python IDE. I recommend using pycharm.
2) Run the program.
3) Follow input instructions.