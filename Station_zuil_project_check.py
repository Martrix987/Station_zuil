import psycopg2.extras
import psycopg2


connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # DictCursor, not the default cursor!
query = """SELECT     *
           FROM       station_service
           where
           ;"""



cursor.execute(query)
print(cursor.fetchall())
conn.close()