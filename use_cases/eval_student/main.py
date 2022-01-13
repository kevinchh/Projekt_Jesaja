from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
#import function that calls model from ml_model.py
from bb_model import predict

app = Flask("feedback_evaluation")

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def ping():
    return "Get / is working"

@app.route('/predict', methods=['POST'])
@cross_origin()
def route_predict():
    unstructured_text = request.get_json()

    #with open('PATH_MODEL', 'rb') as f:
        # model = load(f)
        # f.close()

    #cal prediction function with data and model
    #
    print(f"Request Body: {unstructured_text}")
    res = predict([unstructured_text["1"]])

    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
