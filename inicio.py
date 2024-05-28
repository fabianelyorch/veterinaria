from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def layin():
    return render_template("layout.html")

@app.route('/gat')
def gat():
    return render_template("gat.html")

@app.route('/layout')
def layout():
    return render_template("layout.html")

@app.route('/panr')
def panr():
    return render_template("panr.html")

@app.route('/zor')
def zor():
    return render_template("zor.html")



if __name__ == "__main__":
    app.run(debug=True)
