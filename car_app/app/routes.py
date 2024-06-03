from flask import Flask, render_template, request, redirect, url_for
from .models import Car

app = Flask(__name__)

# List of cars (simulating a database)
cars = []

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

@app.route('/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        new_car = Car(make, model, year)
        cars.append(new_car)
        return redirect(url_for('index'))
    return render_template('add_car.html')
