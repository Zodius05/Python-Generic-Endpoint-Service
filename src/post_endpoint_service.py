import datetime
import time
import random
import string
from flask import Flask, render_template, request, redirect, url_for

#### Flask Routes ####
app = Flask(__name__)
message_id = None
instant_message = {}

@app.route('/json', methods=('GET', 'POST'))
def json():
    global message_id
    global instant_message
    if request.method == 'POST':
        json_data = request.get_json()
        form_id = json_data['text']
        app.logger.debug(f"POST received with form_id: {str(form_id)}")
        message_id = datetime.datetime.now().strftime("%H:%M:%S")
        instant_message[message_id] = str(json_data['text'])
        app.logger.debug(f"Message receieved: {instant_message}")

        return redirect(url_for('home'))
    return render_template('json.html', instant_message = instant_message)

@app.route('/', methods=('GET', 'POST'))
def home():
    global message_id
    global instant_message
    if request.method == 'POST':
        form_id = request.form['form_id']
        app.logger.debug(f"POST received with form_id: {str(form_id)}")
        message_id = datetime.datetime.now().strftime("%H:%M:%S")
        instant_message[message_id] = str(request.form['text'])
        app.logger.debug(f"Message receieved: {instant_message}")

        return redirect(url_for('home'))
    return render_template('index.html', instant_message = instant_message)

#### Main ####
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8008', debug=True, use_reloader=False)