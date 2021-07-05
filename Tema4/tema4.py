import os
import csv
import json
import requests
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup

url = 'https://www.formula1.com/en/results.html/2021/drivers.html'
columns = ['Position', 'Driver', 'Nationality', 'Car', 'Points']

standings = []
page = requests.get(url)
soup = BeautifulSoup(page.content, features='html.parser')

table = soup.find('table', {"class": "resultsarchive-table"})
table_rows = table.find_all('tr')
table_rows.pop(0)

bad_classes = ['limiter', 'hide-for-tablet', 'uppercase hide-for-desktop']

for table_row in table_rows:
    columns_list = []
    for td in table_row.find_all('td'):
        if td.find('span', class_='hide-for-mobile') is not None:
            driver = td.find('span', class_='hide-for-mobile').text
            columns_list.append(driver)

        if td.find('a', class_='grey semi-bold uppercase ArchiveLink') is not None:
            car = td.find('a', class_='grey semi-bold uppercase ArchiveLink').text
            columns_list.append(car)

        if len(td.get('class', [])) and td.get('class', [])[0] not in bad_classes:
            columns_list.append(td.text)

    dict = {
        col: data
        for col, data in zip(columns, columns_list)
    }
    standings.append(dict)

with open('standings.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(columns)
    csv_writer.writerows([team_data.values() for team_data in standings])

