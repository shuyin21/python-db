from sqliteConnect import *


def readSongs():
    cursor.execute("SELECT * FROM songs")  # select all songs records

    # fetch all songs that was retrieved and pas it to the row variable
    row = cursor.fetchall()

    for record in row:  # ierate through the records(held in the row variable)

        print(record)


# readSongs()
