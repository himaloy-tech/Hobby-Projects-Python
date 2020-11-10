import pandas as pd
import requests as re
from bs4 import BeautifulSoup
from PackageHimaloy import *


def new_york():
    page = re.get(
        'https://forecast.weather.gov/MapClick.php?lat=44.1252&lon=-84.1967#.Xs-KcTozbIU')
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(id="seven-day-forecast-body")
    items = week.find_all(class_="tombstone-container")
    # print(items)
    # print(items[0].find(class_='period-name').get_text())
    # print(items[0].find(class_='short-desc').get_text())
    # print(items[0].find(class_='temp').get_text())
    period_names = [item.find(class_='period-name').get_text()
                    for item in items]
    short = [item.find(class_='short-desc').get_text() for item in items]
    temperature = [item.find(class_='temp').get_text() for item in items]
    # print(period_names)
    # print(short)
    # print(temperature)
    weather = pd.DataFrame({
        'Period': period_names,
        'Short Description': short,
        'Temperature': temperature
    })
    createfile('Weather Report', str(weather))


def Washington():
    page = re.get(
        'https://forecast.weather.gov/MapClick.php?lat=38.8904&lon=-77.032#.Xs-R5DozbIU')
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(id="seven-day-forecast-body")
    items = week.find_all(class_="tombstone-container")
    # print(items)
    # print(items[0].find(class_='period-name').get_text())
    # print(items[0].find(class_='short-desc').get_text())
    # print(items[0].find(class_='temp').get_text())
    period_names = [item.find(class_='period-name').get_text() for item in items]
    short = [item.find(class_='short-desc').get_text() for item in items]
    temperature = [item.find(class_='short-desc').get_text() for item in items]
    # print(period_names)
    # print(short)
    # print(temperature)
    weather = pd.DataFrame({
        'Period': period_names,
        'Short Description': short,
        'Temperature': temperature
    })
    createfile('Weather Report', str(weather))


def Michigan():
    page = re.get(
        'https://forecast.weather.gov/MapClick.php?lat=44.1252&lon=-84.1967')
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(id="seven-day-forecast-body")
    items = week.find_all(class_="tombstone-container")
    # print(items)
    # print(items[0].find(class_='period-name').get_text())
    # print(items[0].find(class_='short-desc').get_text())
    # print(items[0].find(class_='temp').get_text())
    period_names = [item.find(class_='period-name').get_text()
                    for item in items]
    short = [item.find(class_='short-desc').get_text() for item in items]
    temperature = [item.find(class_='temp').get_text() for item in items]
    # print(period_names)
    # print(short)
    # print(temperature)
    weather = pd.DataFrame({
        'Period': period_names,
        'Short Description': short,
        'Temperature': temperature
    })
    createfile('Weather Report', str(weather))


def Los_angeles():
    page = re.get(
        'https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453#.Xs-S1jozbIU')
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(id="seven-day-forecast-body")
    items = week.find_all(class_="tombstone-container")
    # print(items)
    # print(items[0].find(class_='period-name').get_text())
    # print(items[0].find(class_='short-desc').get_text())
    # print(items[0].find(class_='temp').get_text())
    period_names = [item.find(class_='period-name').get_text()
                    for item in items]
    short = [item.find(class_='short-desc').get_text() for item in items]
    temperature = [item.find(class_='temp').get_text() for item in items]
    # print(period_names)
    # print(short)
    # print(temperature)
    weather = pd.DataFrame({
        'Period': period_names,
        'Short Description': short,
        'Temperature': temperature
    })
    createfile('Weather Report', str(weather))


print("Welcome")
print('I can tell the weather')
a = 'Los Angeles'
d = 'los angeles'
f = 'Michigan'
g = 'Washington'
h = 'New York'
inpt = ''
def ask():
    inpt = input("Type the city name of which you want to see the weather.")

if inpt == a or inpt == d or 'L' in inpt or 'l' in inpt:
    print('Los Angeles :')
    Los_angeles()
elif inpt == f or inpt == d or 'M' in inpt or 'm' in inpt:
    print("Michigan :")
    Michigan()
else:
    if inpt == g or 'W' in inpt or 'w' in inpt:
        print("Washington Dc :")
        Washington()
    elif inpt == h or 'N' in inpt or 'n' in inpt:
        print('New York :')
        new_york()
    else:
        print("  ")
        print('\n I can only tell the weather of Washington,')
        print('Michigan, Los Angeles, New York')
        ask()