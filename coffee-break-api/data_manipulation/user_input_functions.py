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


# image: temporary image path
def generate_image_hash(image_path):
    with open(image_path, "rb") as file:
        image = file.read()

    hash_object = hashlib.sha256()
    hash_object.update(image)
    image_hash = hash_object.hexdigest()

    return image_hash
