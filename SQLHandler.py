import requests
import mysql.connector
import pandas as pd
from mysql.connector import Error
from io import StringIO

def getTable():
    tap_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    query = """
    SELECT pl_name, discoverymethod, pl_dens, pl_orbtper, pl_massj, pl_letter
    FROM ps
    """
    response = requests.post(tap_url, data={'query': query, 'format': 'csv'})

    if response.status_code == 200:
        # Convert the response to a DataFrame for easy handling
        data = pd.read_csv(StringIO(response.text))
        print(data.tail)
        return data
    else:
        print(f"Error: {response.status_code}\n{response.text}")
        return None
    
def update():
    
    new_pl = requests.pl_name
    new_method = requests.discoverymethod
    new_dens = requests.pl_dens
    new_orbtper = requests.pl_orbtper
    new_mass = requests.pl_massj
    new_letter = requests.pl_letter
        
    query = ("UPDATE ps SET pl_name = '%s', discoverymethod = '%s', pl_dens = '%s', pl_orbtper = '%s', pl_massj = '%s', pl_letter = '%s'" % (new_pl, new_method, new_dens, new_orbtper, new_mass, new_letter))
    
update()
getTable()