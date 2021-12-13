import streamlit as st
import numpy as np
import pandas as pd
from cnn_model import make_prediction
from cnn_model import make_streamlit_prediction
from PIL import Image 

#port 8501 is the default port used by streamlit applications
# reference:
#  https://docs.ovh.com/gb/en/ai-training/build-use-streamlit-image/

st.title("Histopythology Lab")
st.write("Upload an histopathology image")


uploaded_file = st.file_uploader("Choose a file")
#print(type(uploaded_file))
if uploaded_file is not None:
    st.image(uploaded_file, use_column_width=True)
    img = Image.open(uploaded_file)
    # Our model accepts images of size 120x120
    img = img.resize((120,120))

    pix = np.asarray(img)
    data = pix.reshape(1,120,120,3)/255
    prediction = make_streamlit_prediction(data)
    prediction = str( int(prediction[0][0]*100))+'% chance this is malignant'
    st.write(str(prediction))

