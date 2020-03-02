from bs4 import BeautifulSoup
import requests
from datetime import date


def get_info():

    result = requests.get('https://airnow.gov/index.cfm?action=airnow.local_city&cityid=327')
    soup = BeautifulSoup(result.content, 'lxml')

    find_air_quality = soup.find(class_="AQDataLg").get_text()

    str_air_quality = str(find_air_quality)
    date_of_collection = date.today()

    with open('sac_air_data.txt', 'a') as f:
        f.write(f'{date_of_collection}: air quality: {str_air_quality}')
        f.write('\n')
        f.close()


get_info()
