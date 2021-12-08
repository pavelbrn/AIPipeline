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



new_mod = keras.models.load_model("flask_main/neptune_ai.h5")
new_mod.summary()







