import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image


model = tf.keras.models.load_model("F:\\.FINAL YEAR PROJECT\\LFR EFFICIENTNET.h5",custom_objects={'KerasLayer':hub.KerasLayer})

def predict():
	class_names=['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Potato___Early_blight',
 'Potato___Late_blight', 'Potato___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
	img_path ="input.jpg"
	img = image.load_img(img_path, target_size=(224, 224))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	predictions = model.predict(x)
	predicted_class = class_names[np.argmax(predictions[0])]
	confidence = round(100 * (np.max(predictions[0])), 2)
	return predicted_class,confidence