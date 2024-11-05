from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

coordinates = {'x': 0, 'y': 0}

# Get coordinates
@app.route('/coordinates', methods=['GET'])
def get_coordinates():
    return jsonify(coordinates)

# Posty coordinates
@app.route('/coordinates', methods=['POST'])
def update_coordinates():
    data = request.get_json()
    if 'x' in data:
        coordinates['x'] = data['x']
    if 'y' in data:
        coordinates['y'] = data['y']
    return jsonify(coordinates)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
