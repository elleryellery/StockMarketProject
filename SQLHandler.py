import requests
import mysql.connector
import csv
import pandas as pd
from mysql.connector import Error
from io import StringIO

tap_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
query = """
SELECT pl_name, discoverymethod, pl_dens, pl_orbtper, pl_massj, pl_letter
FROM ps
"""
response = requests.post(tap_url, data={'query': query, 'format': 'csv'})
    
def retrieveRow(index):
    myRow = [row for idx, row in enumerate(reader) if idx == index]
    
    return myRow[0]

def numRows():
    global reader
    reader = csv.reader(StringIO(response.text))
    i = 0
    for row in reader:
        i = i+1
    reader = csv.reader(StringIO(response.text))
    return i
