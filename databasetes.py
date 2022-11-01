import psycopg2.extras
import psycopg2 # import changed!


connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # DictCursor, not the default cursor!
query = """SELECT     klantnr, plaats, adres
           FROM       Klant
           WHERE      plaats = 'Amersfoort';"""



cursor.execute(query)
records = cursor.fetchall()
conn.close()


for record in records:
    print(record['klantnr'])



#pw