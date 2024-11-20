from flask import Flask,render_template,request,url_for,flash,redirect,session,Request
from email_service import send_mail
from werkzeug.security import check_password_hash,generate_password_hash
from weather import get_weather
import socket
app=Flask(__name__)
app.secret_key="hallelujah"

@app.route("/")
def home():
    ip=socket.gethostbyname(socket.gethostname())
    session["ip"]=ip
    print(session["ip"])
    return render_template("title.html",ip=ip)

@app.route("/contact",methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        flash("your message has been sent successfully","Success")
        send_mail(name,email,message)
        return redirect(url_for("login"))
    return render_template("login.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/events")
def events():
    return render_template("events.html")
@app.route("/event_details/<event_id>")
def event_details(event_id):
    return render_template(f"{event_id}.html")
@app.route("/team")
def team():
    return render_template("team.html")
@app.route("/map",methods=["GET","POST"])
def map():
    if request.method=="POST":
        
        latitude=request.form['latitude']
        longitude=request.form['longitude']
        flash(f"Latitude: {latitude}, Longitude: {longitude}","Success")
        global final
        final=get_weather(latitude,longitude)
        print(session["ip"])
        return render_template("homepage.html",final=final)

    return render_template("map.html")


    

if __name__=="__main__":
    app.run()