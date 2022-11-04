import psycopg2.extras
import psycopg2

connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
query = """SELECT naam, bericht
           FROM bericht
           ORDER BY datumtijd_bericht DESC
           LIMIT 5;
           ;"""
cursor.execute(query)
non_con_bericht = cursor.fetchall()
conn.close()

print(non_con_bericht)

print('\n')
for berichten in non_con_bericht:
    bericht = berichten['bericht']
print(bericht)