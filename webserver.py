from flask import Flask, send_from_directory, jsonify
import threading
import time
from wetbuzz import wet_buzz
from temp import sensor_dht11
from sound import sound_serv

humidity_value = 0
temperature_value = 0
moisture_value = "not wet"

def generate_humidity_temperature():
    global humidity_value, temperature_value
    while True:
        humidity_value, temperature_value = sensor_dht11()
        time.sleep(0.2)  # Generate a new value every 0.2 seconds

def check_sound():
    while True:
        sound_serv()
        time.sleep(0.2)  # Generate a new value every 0.2 seconds

def generate_moisture():
    global moisture_value
    while True:
        moisture_value = wet_buzz()
        time.sleep(0.2)  # Generate a new value every 0.2 seconds

threading.Thread(target=generate_humidity_temperature, daemon=True).start()
threading.Thread(target=generate_moisture, daemon=True).start()
threading.Thread(target=check_sound, daemon=True).start()

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>')
def static_file(path):
    return send_from_directory('static', path)

@app.route('/update_humidity')
def update_humidity():
    return jsonify({'humidity': humidity_value})

@app.route('/update_temperature')
def update_temperature():
    return jsonify({'temperature': temperature_value})

@app.route('/update_moisture')
def update_moisture():
    return jsonify({'moisture': moisture_value})

if __name__ == '__main__':
    app.run(port = 5600)
