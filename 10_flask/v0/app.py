# Team Toast: Haotian Gan, Aryaman Goenka, Sean Ging (Duckies: Cinnamon and Untitled and Friedrich)
# SoftDev
# 10-03-2021

# 0: 
#Similar syntax exists in Javascript. In Javascript, global variables can be defined by typing your variable name followed by the variable's value, though it is bad practice and not allowed in Javascript's strict mode.
#Function calls also use the function name followed by parentheses and parameter values in Javascript, Java, C, C++, and C#
#In javascript, a few global variables are defined by the browser. Just like how Python defines "__name__", Javascript defines "document". Many other languages probably also have variables that are globally defined.

#1:
#Based on how most websites use "/" to refer to the page you get if you don't specify a subdirectory when typing in the website's url, this is the page you get if you don't specify a subdirectory in your url

#2:
#This will print __name__ because we are running app.py directly, as opposed to using a module import to run it. This will print to the console

#3:
#This is a guess but if this string is related to what the page's HTML is, the string will probably appear on the screen as a <body>No hablo queso!</body>.

# 4:
# We have seen similar constructs in Javascript, C, C#, Python, and Java


from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?

app.run()  # Q4: Where have you seen similar construcs in other languages?
                
