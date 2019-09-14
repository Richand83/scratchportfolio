import requests
from flask import Flask, redirect, session, render_template, request, flash

app = Flask(__name__)  

@app.route("/")
def landing_page():

    return render_template("index.html")

@app.route("/https://usebasin.com/f/5cbcc589d31b", methods=['POST'])
def send_simple_message():
	
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)