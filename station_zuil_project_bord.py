import psycopg2.extras
import psycopg2
import requests
import datetime as dt


base_url = "https://openweathermap.org/data/2.5/weather?" 
api_key = open('api_key', 'r').read()
stad = "Amsterdam"

url = base_url + "appid=" + api_key + "&q=" + stad

antwoord = requests.get(url).json
print(antwoord)




connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
query = """SELECT bericht
           FROM bericht
           ORDER BY datumtijd_bericht DESC
           LIMIT 5;
           ;"""
cursor.execute(query)
non_con_bericht = cursor.fetchall()
conn.close()

print(non_con_bericht)

'''
print('\n')
for berichten in non_con_bericht:
    bericht = berichten['bericht']
print(bericht)
'''










