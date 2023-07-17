import tensorflow as tf
import os


os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
LOCAL_PATH = os.getcwd()


def load_cnn_model():
    model = tf.keras.models.load_model(r"{}".format(LOCAL_PATH + "\classifier\ShuffleNet.h5"))
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
