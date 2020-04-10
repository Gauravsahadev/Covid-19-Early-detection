from keras.utils import to_categorical
from keras.models import load_model
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras import backend as K


class Covid:
    def __init__(self, IMAGE_PATH, MODEL_PATH):
        self.IMAGE_PATH = IMAGE_PATH
        self.MODEL_PATH = MODEL_PATH

    def covid_predict(self):
        # Before prediction
        K.clear_session()
        model = load_model(self.MODEL_PATH)
        # Loading and preprocessing image
        img = load_img(self.IMAGE_PATH, target_size=(
            224, 224), color_mode='rgb')
        img = img_to_array(img)
        img = np.array(img) / 255.0
        # Get predictions for image
        prediction = ['Positive', 'Negative']
        return prediction[np.argmax(model.predict(np.expand_dims(img, axis=0)))]
