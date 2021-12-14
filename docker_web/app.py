import streamlit as st
import numpy as np
import pandas as pd
from cnn_model import make_prediction
from cnn_model import make_streamlit_prediction_colon
from cnn_model import make_streamlit_prediction_skin
from PIL import Image 

# port 8501 is the default port used by streamlit applications
# reference:
# https://docs.ovh.com/gb/en/ai-training/build-use-streamlit-image/

'''
# Deep Learning Pathology Lab

'''

st.markdown('*Project Developer: Pavel Boza Zegarra*')  

add_selectbox = st.sidebar.selectbox(
    "Contents:",
    ("Colon Pathology Classifier", "Skin Cancer Classifier","About")
)

# This is the page for the Pathology classifier
if add_selectbox == "Colon Pathology Classifier":
    main_text = '''
    The following project connects this site with a backend pretrained deep learning model
    that is inside a Docker image on google cloud.

The user can upload a histopathology image of a benign or malignant colon slide.
The AI model will then classify it as being bening or malignant. My trained convolutional 
neural network classifies only images of colorectal cancer. 
The convolutional neural network uses an Inception V3 as a base model with added layers to improve the accuracy of the model.

The AI model has a cross validation a test set score of 98% - 99% respectively.
For model details, code and tests please see my Jupyter Notebook:
- https://github.com/pavelbrn/PathologyAIPipeline/blob/master/ai_trainer/colonCNN.ipynb
'''
    with st.container(): main_text
    allowed_image_types = ['png', 'jpg','jpeg']
    uploaded_file = st.file_uploader("Drag a .png, .jpg or .jpeg image here to upload, the score will be calculated:", type=allowed_image_types)

    if uploaded_file is not None:
        
        img = Image.open(uploaded_file)
        # Our model accepts images of size 120x120
        img = img.resize((120,120))

        pix = np.asarray(img)
        data = pix.reshape(1,120,120,3)/255
        prediction = make_streamlit_prediction_colon(data)
        prediction = str( int(prediction[0][0]*100))+'% chance this colon image is malignant'
        st.write(prediction)
        st.image(uploaded_file, use_column_width=True)
        
    col1, col2= st.columns(2)
    with col1:
        st.markdown(' ** Malignant sample** ')  
        st.image("streamlit_images/colonca71.jpeg")
        

    with col2:
        st.markdown(' ** Benign sample**')  
        st.image("streamlit_images/colonn72.jpeg")

# This is the page for the Skin Classifier
elif add_selectbox == "Skin Cancer Classifier":
    main_text = '''
    This skin cancer classifier is a pretrained deep learning model with a 
    prediction rate of about 80%. This mode has not been pretrained on Inception V3,
    but has been developed from scratch to learn about the general architecture of 
    a convolutional neural network. Unlike the Inception V3 model, which has over 300 
    lavers, this model has 7. 
    I will upgrade and augmented the architecture in the future. Check out my notebook here:
- https://github.com/pavelbrn/SkinCancerImageClassifier/blob/master/CNN.ipynb
'''
    with st.container(): main_text
    allowed_image_types = ['png', 'jpg','jpeg']
    uploaded_file = st.file_uploader("Drag a .png, .jpg or .jpeg image here to upload, the score will be calculated:", type=allowed_image_types)

    if uploaded_file is not None:
        
        img = Image.open(uploaded_file)
        # Our model accepts images of size 120x120
        img = img.resize((120,120))

        pix = np.asarray(img)
        data = pix.reshape(1,120,120,3)/255
        prediction = make_streamlit_prediction_skin(data)
        prediction = str( int(prediction[0][0]*100))+'% chance this skin image is malignant'
        st.write(prediction)
        st.image(uploaded_file, use_column_width=True)
        
    col1, col2= st.columns(2)
    with col1:
        st.markdown(' ** Malignant sample** ')  
        st.image("streamlit_images/skin_malignant.jpg")
        
    with col2:
        st.markdown(' ** Benign sample**')  
        st.image("streamlit_images/skin_benign.jpg")


# This is the About page    
elif add_selectbox == "About":
    main_text = '''
Berlin based Canadian. Applying data science and my programming skills in the medical field and beyond. 
I have excellent medical domain knowledge with 7 years of applied clinical experience in Anesthesia, Intensive Care Unit, Emergency Medicine and Internal Medicine. 
13 years of medical training and am fully licensed to practice medicine in the European Union. 
Certified by the United States Educational Commission for Foreign Medical Graduates.

       '''
    with st.container(): main_text   

    st.markdown('GitHub:')
    st.markdown('https://github.com/pavelbrn')

    st.markdown('https://www.linkedin.com/in/pavelbz/')
#with st.container(): main_text

