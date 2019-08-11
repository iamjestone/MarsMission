from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/marsapp"
mongo = PyMongo(app)

@app.route("/")
def home():
    marsstuff = mongo.db.marsstuff.find_one()
    return render_template("index.html", marsstuff = marsstuff)

@app.route("/scrape")
def scrape():
    marsstuff = mongo.db.marsstuff
    marsdata = scrape_mars.marsscrape1()
    marsstuff.update({}, marsdata, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)