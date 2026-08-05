from flask import Flask,render_template,request
import numpy as np
import joblib

model=joblib.load("maternal_risk_rfrmodel.pkl")

app=Flask(__name__)

@app.route('/predict',methods=['GET','POST'])
def predict():
    age=int(request.form['age'])
    sbp=int(request.form['sbp'])
    dbp=int(request.form['dbp'])
    bs=int(request.form['bs'])
    temp=int(request.form['temp'])
    heartrate=int(request.form['heartrate'])

    test_data=np.array([[age,sbp,dbp,bs,temp,heartrate]])

    pred=model.predict(test_data)
    if pred[0]==0:
        label="low risk"
    elif pred[0]==1:
        label="mid risk"
    else:
        label="high risk"
        
        

    result=f"Predict Risk is : {label}"

    return render_template('home.html',msg=result)
    
@app.route('/login',methods=['GET','POST'])
def chklogin():

    username=request.form['username']
    password=request.form['password']

    if username=="admin" and password=="1234":
        return render_template('home.html')
    else:
        return render_template('index.html',msg="Login failed, relogin")
    
    if username=="admin" and password=="1234":
        return "Login is Successful"
    else:
        return "Sorry login failed"
@app.route('/')  #this is default route
def index():
    return render_template('index.html')

app.run(debug=True,host="0.0.0.0")  #it truns on server