# Team Toast
# Sean Ging, Haotian Gan, Aryman Goenka, (Duckies:) Friedrich, Cinnamon, Untitled
# SoftDev
# K10: Putting Little Pieces Together / Predicting rudimentary flask apps
# 10-04-2021

# Predictions:
# We predict that the following code will create a flask object that 
# displays "No hablo queso" in its body when its index page is visited by a user.
# and prints "__name__" to the python console because when we directly run this file 
# through the python terminal, Python sets __name__ equal to '__name__'

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

