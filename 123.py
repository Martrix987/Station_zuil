import psycopg2.extras

#er moet een input zijn voor welke stad en die moet doorgeven welke voorzieningen er zijn
def voorzieningen(stad):
    connection_string = "host='localhost' dbname='station_zuil_database' user='postgres' password='128256'"
    conn = psycopg2.connect(connection_string) 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


    cursor.execute("SELECT   ov_fiets, lift, wc, laaden_lossen   FROM station_service   WHERE station_stad = %s", (stad,))


    voorzieningen = cursor.fetchall()
    conn.close()
    for berichten in voorzieningen:
        ov_fiets = berichten[berichten[0]]
        lift = berichten[berichten[1]]
        wc = berichten[berichten[2]]
        laaden_lossen = berichten[berichten[3]]
        if ov_fiets == True:
            print('hello world')
        if lift == True:
            print('hello world')
        if wc == True:
            print('hello world')
        if laaden_lossen == True:
            print('hello world')     

    return ov_fiets, lift, wc, laaden_lossen



stad = 'Amsterdam'
ov_fiets, lift, wc, laaden_lossen = voorzieningen(stad)
print(ov_fiets)
print(lift)
print(wc)
print(laaden_lossen)

