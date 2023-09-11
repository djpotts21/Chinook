from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost chinook db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create varuabke for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
    )

# create varuabke for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId")),
    )

# create varuabke for "Album" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer, primary_key=False),
    Column("Bytes", Integer, primary_key=False),
    Column("UnitPrice", Float)
    )

# making the connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select the "Name" records from the "Artist" table
    # select_query = artist_table.select().with_only_columns(
    #    [artist_table.c.Name])

    # Query 3 - select all records from the "Artist"
    # table where the artis equals "Queen"
    # select_query = artist_table.select().where(
    #    artist_table.c.Name == "Queen"
    #    )

    # Query 4 - select only by "ArtistId" #51 from the "Artist" table
    # select_query = artist_table.select().where(
    #     artist_table.c.ArtistId == 51
    #     )

    # Query 5 - select only by "ArtistId" #51 from the "Album" table
    # select_query = album_table.select().where(
    #     album_table.c.ArtistId == 51
    #     )

    # Query 6 - select only by "Composer" == "Queen" from the "Track" table
    select_query = track_table.select().where(
        track_table.c.Composer == "Queen"
        )

    results = connection.execute(select_query)
    for result in results:
        print(result)
