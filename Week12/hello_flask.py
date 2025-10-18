from flask import Flask
from flask import request

app = Flask(__name__)

temperature_converters = {
    'c_to_f': {
        'unit': {
            'from': 'Celsius',
            'to': 'Fahrenheit'
        },
        'func': lambda n: n * 9 / 5 + 32
    },
    'f_to_c': {
        'unit': {
            'from': 'Fahrenheit',
            'to': 'Celsius'
        },
        'func': lambda n: (n - 32) * 5 / 9
    },
    'c_to_k': {
        'unit': {
            'from': 'Celsius',
            'to': 'Kelvin'
        },
        'func': lambda n: n + 273.15
    },
    'k_to_c': {
        'unit': {
            'from': 'Kelvin',
            'to': 'Celsius'
        },
        'func': lambda n: n - 273.15
    },
    'f_to_k': {
        'unit': {
            'from': 'Fahrenheit',
            'to': 'Kelvin'
        },
        'func': lambda n: (n - 32) * 5 / 9 + 273.15
    },
    'k_to_f': {
        'unit': {
            'from': 'Kelvin',
            'to': 'Fahrenheit'
        },
        'func': lambda n: (n - 273.15) * 9 / 5 + 32
    },
}


@app.route('/')
def hello_flask():
    return '<p>Hello, Flask</>'


@app.route('/username/<name>')
def hello_user(name):
    return f'<p>{name} is learning Flask</>'


@app.route('/calc/<int:number>')
def calc(number):
    return f'<p>The squre of {number} is {number**2}</>'


@app.route('/uploadimage')
def upload_image():
    return f'<p><a href="#">Hyper Link</a></p>\n<p><input type="file" /></p>'


@app.route('/temperature/<number>')
def convert_temperature(number):
    try:
        number = float(number)
    except Exception:
        return '<h1>Input temperature value is not valid</h1>'
    from_unit = request.args.get('from') or ''
    to_unit = request.args.get('to') or ''
    if not from_unit or not to_unit:
        return '<h1>Input convertion parameter is not valid</h1>'
    converter = temperature_converters[f'{from_unit}_to_{to_unit}']
    result = converter['func'](number)
    return (
        f"<h1>"
        f"Temperature {number} {converter['unit']['from']} is converted to"
        f" {result} {converter['unit']['to']}"
        "</h1>")
