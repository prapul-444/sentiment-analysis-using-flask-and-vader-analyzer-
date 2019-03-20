import pyrebase
from flask import *
config = {
    "apiKey": ,
    "authDomain": ,
    "databaseURL": ,
    "projectId": ,
    "storageBucket": ,
    "messagingSenderId": 
    }
firebase = pyrebase.initialize_app(config)

db = firebase.database()
app=Flask(__name__)
@app.route('/',methods=['GET','POST']) 
def  basic():
	if(request.method=='POST'):
	 	name=request.form['mem']
	 	v=db.child(name+"senti").get()
	 	b=v.val()
	 	k=b.values()
	 	l=list(k)
	 	avg=l.count(1)/len(l)
	    
	    
	 	return render_template("calc.html",t=int(avg*100))

	return render_template("calc.html") 	
if __name__=="__main__":
     app.run(debug=True)        	
