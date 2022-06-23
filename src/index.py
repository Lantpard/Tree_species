from crypt import methods
from doctest import OutputChecker
from tkinter.tix import Form
from flask import Flask, render_template, request
import folium
from static.models.map import mapl
from static.models.mapCluster import mapl2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/trees')
def trees():
    return render_template('trees.html')

@app.route('/estado')
def estado():
    return render_template('estado.html')

@app.route('/app')
def dash():
    html_string = mapl()._repr_html_()
    return render_template('app.html',folium_map=html_string)

@app.route('/app2')
def dash1():
    html_string = mapl2()._repr_html_()
    return render_template('app2.html',folium_map2=html_string)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)