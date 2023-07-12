# import base64
# import io
import tensorflow as tf


# def decode_base64(base64_string):
#     image_data = base64.b64decode(base64_string)
#     image = io.BytesIO(image_data)
#     return image


def load_cnn_model():
    model = tf.keras.models.load_model(r"C:\Users\ArkadeUser\Documents\projects\coffee-break\coffee-break-api\classifier\ShuffleNet.h5")
    return model


def predict_image_class(image):
    model = load_cnn_model()
    class_names = ["Cercospirose", "Saudável", "Ferrugem", "Bicho Mineiro", "Phoma"]
    prediction = model.predict(image)

    predictions_probability = {key: round(value * 100, 1) for key, value in zip(class_names, prediction[0])}
    predictions_probability = {key: predictions_probability[key] 
                               for key in sorted(predictions_probability, 
                                                 key=predictions_probability.get, 
                                                 reverse=True)}
    
    return predictions_probability