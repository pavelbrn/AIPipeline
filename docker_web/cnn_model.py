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


def make_streamlit_prediction_colon(reshaped_numpy):
    # colon_CNN_model_main - for EC deployment or for Ubuntu testing
    # dummy_test_model - for MacOS M1(Metal) testing, other models wont work on metal
    new_mod = keras.models.load_model("colon_CNN_model_main.h5", compile=False)

    pred_test= new_mod.predict(reshaped_numpy)
    #new_mod.summary()#

    print(pred_test)
    return pred_test

def make_streamlit_prediction_skin(reshaped_numpy):
    # colon_CNN_model_main - for EC deployment or for Ubuntu testing
    # dummy_test_model - for MacOS M1(Metal) testing, other models wont work on metal
    new_mod = keras.models.load_model("alpha_model4.h5", compile=False)

    pred_test= new_mod.predict(reshaped_numpy)
    #new_mod.summary()#

    print(pred_test)
    return pred_test







