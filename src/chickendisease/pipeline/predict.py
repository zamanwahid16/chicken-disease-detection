""" Prediction pipeline for chicken disease detection. """
import os

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class Prediction:
    """Prediction Class"""

    def __init__(self, file_name):
        self.file_name = file_name

    def predict(self):
        """Predict the class of the image."""
        model = load_model(os.path.join('artifacts', 'model_training', 'model.h5'))
        img = image.load_img(self.file_name, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        prediction = np.argmax(model.predict(img), axis=-1)
        if prediction[0] == 1:
            prediction = 'Healthy'
            return [{'Prediction': prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{'Prediction': prediction}]
