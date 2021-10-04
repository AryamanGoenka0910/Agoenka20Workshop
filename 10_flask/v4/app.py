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
# since debug mode has been toggled on with app.debug = True, the app will reload when the code changes
# This code will only run if __name__ is equal to '__name__'--in other words, if this file is run directly, as opposed to an import.

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
