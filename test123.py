import psycopg2

#verbind met de database 
con = psycopg2.connect(
            host = 'localhost',
            database = 'station_zuil_database',
            user = 'postgres',
            password = 'postgres')

#cursor
cur = con.cursor()

#het uitvoeren van de query
cur.execute('select id, name frome employes')


rows = cur.fetchall()

for r in rows:
    print(f'id {r[0]} name {r[1]}')

#sluit de verbindig en de cursor
cur.close
con.close





