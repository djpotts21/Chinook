import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select the "Name" records from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select all records from the "Artist"
# table where the artis equals "Queen"
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s',["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s',[51])

# Query 5 - select only by "ArtistId" #51 from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s',[51])

# Query 6 - select only by "ArtistId" #51 from the "Album" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close connection
connection.close()

# print results
for result in results:
    print(result)
