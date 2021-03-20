# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/178H03NCS9ozjoYRDPd3JOUlccMhzbT3j
"""

#!pip install streamlit

import streamlit as st
import VGG16
import tensorflow as tf
#import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image,ImageOps
import numpy as np
#import tensorflow as tf
#from keras.models import load_model
import io
from tensorflow import keras

import pandas as pd
import pickle
import time
#@st.cache
VGG16=tf.keras.load_model("VGG16")
MobileNetV2=tf.keras.load_model("MobileNetV2")
class plant_diseases_detection():
  
  def page_setup():
    st.set_page_config(page_title="Plant Disease Detection App", page_icon="icon.png", layout='centered', initial_sidebar_state='auto')
    
    st.title("Plant Diseases Detection")
    st.markdown("This project is *Really Interesting*! ")
    def vgg():
      add_vgg_selecbox=st.sidebar.selectbox('select view',['graph','acc'])
  
    ######### -------------- Sidebarr--------------------->
    add_selectbox = st.sidebar.selectbox(
    'select the model for classification',
    ('MobileNetV2','VGG16',"ResNet50","InceptionV3","EfficientNet",'Demo Images','Working Demo','Contact us'))
    #options=st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))

    def classes(pred):
      
      dict_classes={'Apple___Apple_scab': 0, 'Apple___Black_rot': 1, 'Apple___Cedar_apple_rust': 2, 'Apple___healthy': 3, 
                'Blueberry___healthy': 4, 'Cherry_(including_sour)___Powdery_mildew': 5, 'Cherry_(including_sour)___healthy': 6, 
                'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 7, 'Corn_(maize)___Common_rust_': 8, 
                'Corn_(maize)___Northern_Leaf_Blight': 9, 'Corn_(maize)___healthy': 10, 'Grape___Black_rot': 11, 
                'Grape___Esca_(Black_Measles)': 12, 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 13, 'Grape___healthy': 14, 
                'Orange___Haunglongbing_(Citrus_greening)': 15, 'Peach___Bacterial_spot': 16, 'Peach___healthy': 17, 
                'Pepper,_bell___Bacterial_spot': 18, 'Pepper,_bell___healthy': 19, 'Potato___Early_blight': 20, 'Potato___Late_blight': 21, 
                'Potato___healthy': 22, 'Raspberry___healthy': 23, 'Soybean___healthy': 24, 'Squash___Powdery_mildew': 25, 
                'Strawberry___Leaf_scorch': 26, 'Strawberry___healthy': 27, 'Tomato___Bacterial_spot': 28, 'Tomato___Early_blight': 29,
                'Tomato___Late_blight': 30, 'Tomato___Leaf_Mold': 31, 'Tomato___Septoria_leaf_spot': 32, 
                'Tomato___Spider_mites Two-spotted_spider_mite': 33, 'Tomato___Target_Spot': 34, 
                'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 35, 'Tomato___Tomato_mosaic_virus': 36, 'Tomato___healthy': 37}
      predicted_class=(list (dict_classes.keys())[list (dict_classes.values()).index(pred)])
      return predicted_class


    ############# model selection ################
    if(add_selectbox=='VGG16' or add_selectbox=='MobileNetV2'):
      file_uploader=st.file_uploader('Upload cloth Image for Classification:')
      st.set_option('deprecation.showfileUploaderEncoding', False)
    if file_uploader is not None:
        image=Image.open(file_uploader)
        text_io = io.TextIOWrapper(file_uploader)
        image=image.resize((224,224))
        st.image(image,'Uploaded image:')
        
           
        def classify_image(image,model):
            st.write("classifying......")
            img = ImageOps.grayscale(image)
        
            img=img.resize((224,224))
      
            img=np.expand_dims(img,0)
          
            img=(img/255.0)
        
        
            #pred=model.predict(img)
        
            st.write("The Predicted image is:",classes(pred=10))
            st.write('Prediction probability :{:.2f}%'.format(np.max(pred)*100))
        st.write('Click for classify the image')
        if st.button('Classify Image'):
            if(add_selectbox=='VGG16'):
                st.write("You are choosen Image classification with VGG16 model")
                classify_image(image,VGG16)
                st.success('This Image successufully classified!')
                with st.spinner('Wait for it...'):
                    time.sleep(2)
                    st.success('Done!')
                    st.balloons()
                st.balloons()
            if(add_selectbox=='MobileNetV2'):
                st.write("You are choosen Image classification with MobileNetV2")
                classify_image(image,VGG16)
                st.success('This Image successufully classified!')
                with st.spinner('Wait for it...'):
                    time.sleep(2)
                    st.success('Done!')
                    st.balloons()
    else:
        st.write("Please select image:")
  
  page_setup()
plant_diseases_detection()



