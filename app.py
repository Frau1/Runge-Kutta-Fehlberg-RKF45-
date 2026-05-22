from flask import Flask, render_template, request
from methods.rkf45 import rkf45_solver

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/theory')
def theory():
    return render_template('theory.html')

@app.route('/examples')
def examples():
    return render_template('examples.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():

    results = None

    if request.method == 'POST':

        equation = request.form['equation']
        x0 = float(request.form['x0'])
        y0 = float(request.form['y0'])
        h = float(request.form['h'])
        xn = float(request.form['xn'])

        results = rkf45_solver(
            equation,
            x0,
            y0,
            h,
            xn
        )

    return render_template(
        'calculator.html',
        results=results
    )

if __name__ == '__main__':
    app.run(debug=True)