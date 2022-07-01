from sqliteConnect import *
import time
import readData


def updateSongs():
    idField = input("Enter the songID of the song to be updated: ")

    fieldName = input(
        "Which field would you like to be updated: (Title, Artist, Genre)? ").title()
    newfieldValue = input(f"Enter the new field value for {fieldName}: ")
    print(f"the new value entered is {newfieldValue} ")

    # add single quotes around the new field value entered by the user

    newfieldValue = "'" + newfieldValue + "'"
    print(f"The new value entered is {newfieldValue} ")
    cursor.execute(
        f"UPDATE songs SET {fieldName} = {newfieldValue} WHERE songID = {idField} ")
    conn.commit()
    print(f"Record {idField} Updated from Songs table ")

    time.sleep(3)
    readData.readSongs()


# updateSongs()
