#  Team Toast
# Sean Ging, Haotian Gan, Aryman Goenka, Tomas Acuna (Duckies:) Friedrich, Cinnamon, Untitled, Llamy
# SoftDev
# K10: Putting Little Pieces Together / Predicting rudimentary flask apps
# 10-04-2021

import csv, random

#Function to read csv file and transfer it to an approriate dictionary
def readfile(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    header = next(csvreader)
    occupations = {}
    for row in csvreader:
        if header[1] != row[1]:
            if row[0] != "Total":
                occupations[row[0]] = row[1]
    file.close()
    return occupations

#Using the weights provided in percentages, generate a randomly selected occupation
def generateRandom(occupations):
    ran = random.random() * 100
    for row in occupations:
        holder = occupations.get(row)
        ran -= float(holder)
        if ran <= 0:
            return row
    return "Unemployed" #if user never reaches 0, they are unemployed   


from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    choice = generateRandom(readfile("occupations.csv"))
    return render_template('index.html', choice=choice)

app.run(debug=True)