import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import Normalizer
import cv2
from PIL import Image
from numpy import expand_dims
from keras.models import load_model
import pickle

old_value = ""

def get_face_embedding(model,face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = ( face_pixels - mean ) / std
    sample = expand_dims(face_pixels,axis = 0)
    yhat = model.predict(sample)
    return yhat[0]

model = load_model('Model/Facenet_keras.h5')
with open('./Model/Finalized_FaceVerificationV0.1.model','rb') as file:
    svc_model = pickle.load(file)

def User_Initial_Login(img,result_face_array):

    x, y, width, height = result_face_array[0]['box']
    x1, y1, x2, y2 = abs(x), abs(y), x + width, y + height
    image_arr = np.array(img)
    face = image_arr[y1:y2, x1:x2]
    cropped_face = Image.fromarray(face)
    cropped_face_resize = cropped_face.resize(((160,160)))
    face_array = np.array(cropped_face_resize)
    
    embedding = get_face_embedding(model,face_array)
    in_encoder = Normalizer(norm ='l2')
    new_embedding = in_encoder.transform(embedding.reshape(-1,1))
    embedding_result = svc_model.predict(new_embedding.reshape(1,128))

    Facenet_result = embedding_result[0]
    print(Facenet_result)

    return Facenet_result