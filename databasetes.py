import psycopg2.extras
import psycopg2


connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # DictCursor, not the default cursor!
query = """SELECT     *
           FROM       station_service
           
           ;"""



cursor.execute(query)
print(cursor.fetchall())
conn.close()

    




#SELECT TOP(5) percent
#datumtijd_bericht, naam
#FROM gebruiksers_invoer
#WHERE naam = marnix
#--ORDER BY datumtijd_bericht ASC DESC;




'''
connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("INSERT INTO gebruiksers_invoer (datumtijd_bericht, naam, bericht, station) VALUES (%s, %s, %s, %s)", (datum, naam, bericht, random_station))


conn.commit()
cursor.close()
conn.close()
'''