# Haotian Gan, Aryman Goenka
# SoftDev
# K19: API Practice
# 11-23-2021


from flask import Flask, render_template
import requests
app = Flask(__name__)
api_key = open('./key_nasa.txt').readlines()[0]


@app.route("/")
def hello_world():
  payload = {'count': 1, 'api_key': api_key}
  r = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
  r_json = r.json()[0]
  templateArgs = {
    "image": r_json['url'],
    "explanation": r_json['explanation']
  }
  return render_template("main.html", **templateArgs)

if __name__ == "__main__":
    app.debug = True
    app.run()
