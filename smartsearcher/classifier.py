
import tensorflow as tf

from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_resnet_v2 import preprocess_input, decode_predictions

import numpy as np

import sys

from . import synset

model = InceptionResNetV2(weights='imagenet')


def predict(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)

    return [{
            'probability': float(p[2]),
            'name': p[1],
            'categories': synset.tree(p[0])
            } for p in decode_predictions(preds, top=2)[0]]
