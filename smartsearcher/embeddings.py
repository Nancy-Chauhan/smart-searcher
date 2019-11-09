import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras import Sequential

from tqdm import tqdm

import os
import logging

IMG_WIDTH = 224
IMG_HEIGHT = 224

logger = logging.getLogger(__name__)

# Pre-Trained Model

__model = None


def __get_model():
    global __model
    if not __model:
        base_model = InceptionResNetV2(weights='imagenet',
                                       include_top=False,
                                       input_shape=(IMG_WIDTH, IMG_HEIGHT, 3))
        base_model.trainable = False

        # Add Layer Embedding
        __model = Sequential([
            base_model,
            GlobalMaxPooling2D()
        ])

    return __model


def __calculate_embedding(img_path):

    model = __get_model()

    # Reshape
    img = image.load_img(img_path, target_size=(IMG_WIDTH, IMG_HEIGHT))
    # img to Array
    x = image.img_to_array(img)
    # Expand Dim (1, w, h)
    x = np.expand_dims(x, axis=0)
    # Pre process Input
    x = preprocess_input(x)
    return model.predict(x).reshape(-1)


def get_embedding(img_path, cached=True):

    if not cached:
        return __calculate_embedding(img_path)

    embeddings_path = img_path + '.npy'

    try:
        return np.load(embeddings_path)
    except FileNotFoundError:

        embeddings = __calculate_embedding(img_path)
        np.save(embeddings_path, embeddings)

        return embeddings
