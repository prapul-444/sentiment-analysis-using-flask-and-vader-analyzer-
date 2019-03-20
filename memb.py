import pyrebase

import fire_send
from flask import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer= SentimentIntensityAnalyzer()

c1=0
config = {
    "apiKey": ,
    "authDomain": ,
    "databaseURL": ,
    "projectId": ,
    "storageBucket":,
    "messagingSenderId": 
    }
firebase = pyrebase.initialize_app(config)

db = firebase.database()

app=Flask(__name__)
@app.route('/',methods=['GET','POST']) 
def ne():
    if(request.method=='POST'):
       name=request.form['name']
       mem=request.form['mem']
       
       db.child(mem).push(name)
       b=analyzer.polarity_scores(name)
     
       if(b['pos']>0.5):
           c1=1
       if(b['neg']>0.5):
       	   c1=0
       if(b['neu']>0.5):
       	   c1=0
       

       j=fire_send.send(mem+"senti",c1)
       

       return render_template("index.html")
    return render_template("index.html")
if __name__=="__main__":
     app.run(debug=True)        