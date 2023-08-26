from flask import Flask, render_template, jsonify
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data/<int:start_year>')
def get_data(start_year):
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Filter the data based on the year
    filtered_data = [item for item in data['Values'] if item['year'] >= start_year]

    return jsonify(filtered_data)


if __name__ == '__main__':
    app.run(debug=True)
