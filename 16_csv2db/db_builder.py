#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Dec 2020 -- The Time of the Rona

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

c.execute("Drop Table if exists Students")
command = "Create Table Students (name Text, age Integer, id Integer)"    
c.execute(command)      # test SQL stmt in sqlite3 shell, save as string
# run SQL statement

filename = "students.csv"
with open(filename) as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        name = row['name']
        age = int(row['age'])
        id = int(row['id'])
        command = f"""Insert Into Students Values("{name}", "{age}", "{id}")"""
        c.execute(command)

c.execute("Drop Table if exists Courses")
command = "Create Table Courses (code Text, mark Integer, id Integer)"    
c.execute(command)      # test SQL stmt in sqlite3 shell, save as string
# run SQL statement

filename = "courses.csv"
with open(filename) as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        code = row['code']
        mark = int(row['mark'])
        id = int(row['id'])
        command = f"""Insert Into Courses Values("{code}", "{mark}", "{id}")"""
        c.execute(command)


#==========================================================

db.commit() #save changes
db.close()  #close database


