import time
import datetime
import os
import json
import sys


# run setup first and when entering location (add the instagram location id)

def testquery():

    postnum = input("How many posts do you want to download?: ")

    os.system('instagram-scraper ' + locationgetter() + ' --location -m' + postnum + ' -u urmaskkk -p OssaPoiss1')

def locationgetter():

    location = input('Location: ')

    os.system('instagram-scraper ' + location + ' --search-location -u urmaskkk -p OssaPoiss1')

    return input('Location code (enter one from above): ')


testquery()
