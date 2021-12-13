import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras
import os
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from tensorflow.keras import Model

from tensorflow.keras.applications.inception_v3 import InceptionV3

# flask_main/imagetest.png
def make_prediction(img_path):
    # colon_CNN_model_dummy - for EC deployment or for Ubuntu testing
    # neptune_ai - for MacOS M1(Metal) testing, other models wont work on metal
    new_mod = keras.models.load_model("colon_CNN_model_dummy.h5", compile=False)
    # Image.open("flask_main/imagetest.png")
    ext_img = image.load_img(img_path, target_size=(120, 120))

    data_img = np.asarray( ext_img )
    data = data_img.reshape(1, 120, 120, 3)/255.0
    print(data.shape)
    pred_test= new_mod.predict(data)
    #new_mod.summary()#

    print(pred_test)
    return pred_test

#make_prediction("uploads/imagetest.png")







