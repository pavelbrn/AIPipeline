import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras
import os
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt


IMAGES_PATH = "ai_trainer/data_prostate/train/train_images"
LABELS_PATH = "ai_trainer/data_prostate/labels/train.csv"

patho_labels = pd.read_csv(LABELS_PATH,index_col=0)

print(patho_labels.head())

