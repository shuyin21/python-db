import readData
import updateData
import deleteData
import insertData


def menuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5"]:
        print("Songs Menu Options:\nEnter \n1. To print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. To Exit")
        options = input("\nEnter one of the options above : ")
        if options not in ["1", "2", "3", "4", "5"]:
            print(f" {options} is not a valid choice!")
        return options


mainProgram = True

while mainProgram:
    mainMenu = menuOptions()
    if mainMenu == "1":
        readData.readSongs()
    elif mainMenu == "2":
        insertData.addSongs()
    elif mainMenu == "3":
        updateData.updateSongs()
    elif mainMenu == "4":
        deleteData.deleteSongs()
    elif mainMenu == "5":
        break
