import warnings
warnings.filterwarnings("ignore")
from flask import Flask, request, render_template
import numpy as np
import flask
import io
import joblib
import json
from flask_lt import run_with_lt

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
run_with_lt(app)

pred=None

model =joblib.load('model.hdf5')

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("index.html")
@app.route("/index.html", methods=['GET', 'POST'])
def index1():
	return render_template("index.html")

@app.route("/mobile.html", methods=['GET', 'POST'])
def diabetes():
	return render_template("mobile.html")
@app.route("/mobile", methods=['GET', 'POST'])
def diabetes1():
	return render_template("mobile.html")

@app.route('/MOBILE', methods=["GET","POST"])

def DIABETES():
    data = {"success": False}
    if request.method == "POST":
        
        ram = request.form["ram"]
        battery_power = request.form['battery_power']
        px_height = request.form['px_height']
        px_width = request.form['px_width']
        int_memory = request.form['int_memory']
        
        
        ressdk = {"ram":ram,
               "battery_power":battery_power,
               "px_height":px_height,
               "px_width":px_width,
               "int_memory":int_memory} 
    
        json_object = json.dumps(ressdk) 

        arr = np.array([[ram, battery_power, px_height, px_width, int_memory]])
        res = model.predict(arr)
        
        global pred
        if res == 0:
            pred="Low Cost"
        elif res == 1:
            pred = "Medium Cost"
        elif res == 2:
            pred = "High Cost"
        else:
            pred = "Very High Cost"
        
        ressdk["predict"]=pred

        data["predictions"] = []
        data["predictions"].append(pred)
        data["success"] = True

    return render_template('mobile.html', pred=pred)

if __name__ == "__main__":
   
    app.run(debug=True,use_reloader=False)