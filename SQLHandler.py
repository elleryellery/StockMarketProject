import requests
import mysql.connector
import pandas as pd
from mysql.connector import Error
from io import StringIO

tap_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
query = """
SELECT pl_name, discoverymethod, pl_dens, pl_orbtper, pl_massj, pl_letter
FROM ps
"""
response = requests.post(tap_url, data={'query': query, 'format': 'csv'})

data = pd.read_csv(StringIO(response.text))
print(data.tail)

    
def update():
    
    new_pl = data.pl_name
    new_method = data.discoverymethod
    new_dens = data.pl_dens
    new_orbtper = data.pl_orbtper
    new_mass = data.pl_massj
    new_letter = data.pl_letter
    
    if(new_pl == data.pl_name): #condition that determines whether the table has been updated
        return 0
    else:
        query = ("UPDATE ps SET pl_name = '%s', discoverymethod = '%s', pl_dens = '%s', pl_orbtper = '%s', pl_massj = '%s', pl_letter = '%s'" % (new_pl, new_method, new_dens, new_orbtper, new_mass, new_letter))
        return 1
            

def latest():
    data2 = data.get(-1)
    #remove any null values and organize correctly
    return data2

update()