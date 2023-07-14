import hashlib
import numpy as np
from PIL import Image


def get_image_id(image_id):
    return image_id


# image: temporary image path
def load_image(image_path):
    image = Image.open(image_path)
    image = image.resize((128, 128))
    image = np.array(image) / 255.
    image = np.expand_dims(image, axis=0)

    return image
