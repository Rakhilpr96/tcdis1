from flask import Flask, render_template,url_for,request
import pyrebase




config = {
	"apiKey": "AIzaSyDUB5SEN8eszLEGGg31fv36V4fq5IdpRUY",
   	"authDomain": "tcdis-fd5cd.firebaseapp.com",
   	"databaseURL": "https://tcdis-fd5cd.firebaseio.com",
    	"projectId": "tcdis-fd5cd",
    	"storageBucket": "tcdis-fd5cd.appspot.com",
    	"messagingSenderId": "462180862749",
	"appId": "1:462180862749:web:587913ee41259b7a772ff4",
    	"measurementId": "G-JQMMLZH9LS"
}




app = Flask(__name__)

@app.route('/')
def hello_world(): 
    return render_template('tcd.html')

@app.route('/crowd_status', methods = ['GET'])
def result():
	no = request.args.get('trainnumber')
	firebase = pyrebase.initialize_app(config)
	db = firebase.database()
	result = db.child("VENAD EXPRESS").child("Coach Number : 1").get().val()
	per_from_db = int(result["Percentage of crowd"])
	count = per_from_db
	#print("count" , x)
	return render_template('crowd.html',n=no,x=count)
  

if __name__ == '__main__':
    app.run() 
