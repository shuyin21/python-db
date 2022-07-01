from sqliteConnect import *
import time


# create a subroutine to add songs to table songs in c10Sqlite.db

def addSongs():

    # create an empty list

    songs = []

    # capture data inputted by the user

    title = input("Enter song title: ")

    artist = input("Enter Artist: ")

    genre = input("Enter song  Genre")

    # append captured data from the user to the song lis []

    "songs.songID is set to auto increment and would be added automatically"

    # listNmae.append(variableName)

    songs.append(title)

    songs.append(artist)

    songs.append(genre)

    # insert data from the list into the songs table

    cursor.execute("INSERT INTO songs VALUES(NULL, ?,?,?)", songs)

    conn.commit()  # commit/write changes to the songs table in the databse

    # display the name of the song that was added
    print(f"{title} added to Songs table")

    time.sleep(3)  # delay for 3 seconds then execute the code that follows

    cursor.execute("SELECT * FROM songs")  # select all songs records

    # fetch all songs that was retrieved and pas it to the row variable
    row = cursor.fetchall()

    for record in row:  # ierate through the records(held in the row variable)

        print(record)


# addSongs()
