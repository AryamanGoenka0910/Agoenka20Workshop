# Team Toast
# Sean Ging, Haotian Gan, Aryman Goenka, (Duckies:) Friedrich, Cinnamon, Untitled
# SoftDev
# K10: Putting Little Pieces Together / Predicting rudimentary flask apps
# 10-04-2021

# Predictions:
# We predict that the following code will create a flask object that 
# displays "No hablo queso" in its body when its index page is visited by a user.

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

