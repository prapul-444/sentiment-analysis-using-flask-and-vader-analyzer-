import pyrebase

config = {
    "apiKey": "AIzaSyCrOTV20lHEL1bRkdtRVOI77n1dY_6FmJk",
    "authDomain": "test-17b0c.firebaseapp.com",
    "databaseURL": "https://test-17b0c.firebaseio.com",
    "projectId": "test-17b0c",
    "storageBucket": "test-17b0c.appspot.com",
    "messagingSenderId": "143952724398"
    }
firebase = pyrebase.initialize_app(config)

db = firebase.database()
def send(k,l):
	
	db.child(k).push(l)
	