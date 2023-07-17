import binascii
import base64
import os

from flask import Flask, request
from flask_cors import CORS
from objprint import op

from blockchain_code.blockchain import Blockchain

from data_manipulation.user_input_functions import load_image
from classifier.classifier_functions import predict_image_class


app = Flask(__name__)
CORS(app)

blockchain = Blockchain(difficulty=2)

@app.route('/classifier', methods=['POST'])

def classifier():
    if request.method == 'POST':
        data = request.get_json()

        plant_id = data['plantId']
        image_data = data["base64Image"].split(",")
        image_data = image_data[1]

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

        os.remove(file_to_save)

        previousBlock = blockchain.latest_block()
        newBlock = blockchain.new_block({'plant_id': plant_id, 'image': image_data, 'class': predicted_class})
        
        if blockchain.is_first_block_valid():
            if blockchain.is_valid_new_block(new_block=newBlock, previous_block=previousBlock):
                blockchain.add_block(block=newBlock)
            else:
                print("New block invalid")
        else:
            print("First block invalid")

        print("Is Blockchain valid?", blockchain.is_blockchain_valid())
        op(blockchain.blocks)

        return predicted_class
