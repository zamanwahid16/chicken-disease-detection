""" Web app for the project. """
import os

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin

from chickendisease.pipeline.predict import Prediction
from chickendisease.utils.common import decode_image

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    """Client App"""

    def __init__(self):
        self.filename = 'inputImage.jpg'
        self.classifier = Prediction(self.filename)


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    """Home Page"""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    """Prediction Route"""
    image = request.json['image']
    decode_image(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == '__main__':
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)
