import flask
from flask import Flask, render_template, request
import random


app=Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/submits",methods=['POST'])
def submit():
    fname=str(request.form['fname'])
    lname=str(request.form['lname'])
    dob=request.form['dob']
    sc=['!','@','#','$','%','^','&','*','<','>','?','.','/','~','`']
    dobnum=dob.split('-') #YYYY-MM-DD
    fname=fname.capitalize()
    lname=lname.capitalize()
    names=[fname,lname]
    passlist=[random.choice(names),random.choice(sc),random.choice(dobnum)]
    random.shuffle(passlist)
    password=""
    for i in passlist:
        password+=str(i)
    if len(password)<12:
        x=12-len(password)
        addatend=[]
        while len(addatend)<=x:
            addatend.append(random.choice(sc))
            addatend.append(random.randint(0,9))
        random.shuffle(addatend)
        for j in addatend:
            password+=str(j)
    return render_template("submits.html",passwords=password)
if __name__=="__main__":
    app.run(debug=True)