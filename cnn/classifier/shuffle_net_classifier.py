import tensorflow as tf
import numpy as np
from PIL import Image


model = tf.keras.models.load_model("ShuffleNet.h5")

image_dir = "test_images/test.jpg"
image = Image.open(image_dir)
image = image.resize((128, 128))
image = np.array(image) / 255.
image = np.expand_dims(image, axis=0)

prediction = model.predict(image)
class_index = np.argmax(prediction)
class_probability = prediction[0][class_index] * 100

class_names = ["Cercospirose", "Saudável", "Ferrugem", "Bicho Mineiro", "Phoma"]

print("Prediction")
print(f"{class_names[class_index]}: {class_probability}")
