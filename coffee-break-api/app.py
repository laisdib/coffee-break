import binascii
from flask import Flask, request
from flask_cors import CORS

from blockchain_code.blockchain import Blockchain

from data_manipulation.user_input_functions import load_image
from classifier.classifier_functions import predict_image_class

import base64

app = Flask(__name__)
CORS(app)

blockchain = Blockchain(difficulty=4)

@app.route('/classifier', methods=['POST'])

def classifier():
    if request.method == 'POST':
        data = request.get_json()

        plant_id = data['plantId']
        image_data = data["base64Image"].split(",")
        image_data = image_data[1]

        newBlock = blockchain.new_block({'plant_id': plant_id})
        blockchain.add_block(block=newBlock)

        print(blockchain.blocks)

        try:
            decoded_data = base64.b64decode(image_data)
            file_to_save = "./assets/images/process.jpg"
            with open(file_to_save, "wb") as f:
                f.write(decoded_data)
                f.close()
        except binascii.Error as e:
            print(e)

        processed_image = load_image(file_to_save)

        predicted_class = predict_image_class(processed_image)

        print(predicted_class)

        return predicted_class
