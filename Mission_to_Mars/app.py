from flask import Flask, render_template
import Mission_To_Mars2 as md

app=Flask(__name__)

@app.route("/")
def echo():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    Mars_News = md.Mars_News()
    Mars_Images = md.Mars_Images()
    Mars_Weather = md.Mars_Weather()
    Mars_Facts = md.Mars_Facts()
    Mars_Hemispheres = md.Mars_Hemispheres()
    return render_template("scrape.html",mars_news=Mars_News, mars_images=Mars_Images, mars_weather = Mars_Weather, mars_hemispheres = Mars_Hemispheres, mars_facts=Mars_Facts)

if __name__=="__main__":
    app.run(debug=True)