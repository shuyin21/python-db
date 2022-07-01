from sqliteConnect import *
import time
import readData


def deleteSongs():
    # songId to be deleted
    idField = input("Enter the songId of the song to be deleted: ")
    # Method 1
    cursor.execute(f"DELETE FROM songs WHERE SongID = {idField} ")

    # Method 2
    # cursor.execute("DELETE FROM songs WHERE SongID =" + idField)

    conn.commit()

    print(f"Record {idField} deleted from Songs table ")

    time.sleep(3)

    readData.readSongs()


# deleteSongs()
