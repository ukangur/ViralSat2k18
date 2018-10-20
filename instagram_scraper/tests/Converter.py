import time
import datetime
import os
import json

#run setup first and when entering location (add the instagram location id)

def testquery():
    location = input('Asukoht: ')
    date = input('Kuupäev (e.g dd/mm/yyyy) : ')

    unix = time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())

    locationid = str(os.system('instagram-scraper ' + location + ' --search-location -u urmaskkk -p OssaPoiss1'))

    os.system('instagram-scraper ' + locationid + ' --location -m 60 --media-metadata -u urmaskkk -p OssaPoiss1')

    input_dict = json.loads("C:/Users/Laptop/Desktop/funtimes/folder.json")

    output_dict = [x for x in input_dict if x['timestamp'] in range(unix-43200,unix+43200)]

    output_json = json.dumps("C:/Users/Laptop/Desktop/funtimes")

testquery()

