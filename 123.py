import psycopg2.extras

connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
conn = psycopg2.connect(connection_string) 
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
query = """SELECT bericht, naam
            FROM bericht
            ORDER BY datumtijd_bericht DESC
            LIMIT 5;
        ;"""
cursor.execute(query)
non_con_bericht = cursor.fetchall()

'''
new = []
for non_con_bericht in cursor:
    new.append(non_con_bericht)
berichten = []
while new != []:
    new1 = list(new[0])
    print(new1)
    new2 = f"{new1[1]} zegt: {new1[0]}"
    print(new2)
    #if len(new2) >= 50:
    #    new2 = f"{new1[1]} zegt: {new1[0][:50]}-\n{new1[0][50: 100]}-\n{new1[0][100:]}"
    berichten.append(new2)
    new.remove(new[0])
''''







#print(non_con_bericht)
conn.close()



