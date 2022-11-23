import io
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, jsonify, request, Blueprint, render_template, flash
from tensorflow import keras 
import json

application = Blueprint('application', __name__) # lien avec la route mise sur __init__ sinon la route ne fonctionne pas 

model = tf.keras.models.load_model('website/static/retinal-oct_final.h5')

app = Flask(__name__)

diseases = {
    0 : 'Maladie CNV',
    1 : 'Maladie DME',
    2 : 'Maladie DRUSEN',
    3 : 'Aucune maladie'
}

@application.route('/application', methods=['GET','POST'])
def application_panel():
    if request.method == 'POST':
        form_data = request.files
        prediction_result = bulk_infer_image(form_data)
        #json_result = json.dumps(prediction_result)
        predicted_disease_number = prediction_result[0]['prediction']
        predicted_disease_str = diseases[predicted_disease_number]
        return render_template('base.html', json_result = prediction_result, predicted_disease = predicted_disease_str)


    return 'PREDICTION MALADIE DE LA RETINE'

def prepare_image(img):
    img = Image.open(io.BytesIO(img))
    img = img.resize((150, 150))
    img = np.expand_dims(img, 0)
    img = np.stack((img,)*3, axis=-1)
    
    return img


def predict_result(img):
    Y_pred = model.predict(img)
    print('Prédiction du modèle: ', Y_pred)
    return np.argmax(Y_pred, axis=1) #argmax permet de trouver la valeur maximale donc la meilleure prédiction possible de la bonne pathologie


def bulk_infer_image(form_data):

    files = form_data.getlist('images')
    application_data = []

    if not files:
        print("coucou je suis pas là")
        return

    
    for file in files:
        img_bytes = file.read()
        img = prepare_image(img_bytes)
        application_data.append(dict(file=file.filename, prediction=int(predict_result(img))))
    return application_data



# REMPLACE PAR LE CODE CI DESSUS

# @app.route('/predict', methods=['POST'])
# def infer_image():
#     if 'file' not in request.files:
#         return "Please try again. The Image doesn't exist"
    
#     file = request.files.get('file')

#     if not file:
#         return

#     img_bytes = file.read()
#     img = prepare_image(img_bytes)
#     return jsonify(prediction=int(predict_result(img)))
    

# DEVENU INUTILE, REMPLACE PAR LE PAGE HTML

# @app.route('/', methods=['GET'])
# def index():
#     return 'Machine Learning Inference'

# SE TROUVE DANS LE MAIN

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')