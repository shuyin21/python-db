import sqlite3

"Create a variabe 'conn' and pass sqlite connect method to it "
"if the database file not exist it will create, otherwise use it"

conn = sqlite3.connect("c10Sqlite.db")
# cursor method iterates through database/tables
cursor = conn.cursor()
