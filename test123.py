import psycopg2
import psycopg2.extras

'''import psycopg2

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
'''





print('\n')
connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
query = """SELECT     bericht
           FROM       bericht   g, 
                      moderatie           m
           where      g.bericht_id = m.bericht_id
           and      (  goedkeuring = 0 or goedkeuring is NULL )
           ;"""
cursor.execute(query)
print(cursor.fetchall())
conn.close()

