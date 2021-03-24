from flask_config import Config
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/route', methods=['GET', 'POST'])
def endpoint_function():
    return jsonify(User = 'Ariel Serravalle',
                    Description = 'Testing the API can receive and return JSON')
