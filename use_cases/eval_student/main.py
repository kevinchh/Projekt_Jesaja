from flask import Flask, request, jsonify
#import function that calls model from ml_model.py
from bb_model import predict

app = Flask("feedback_evaluation")

@app.route('/', methods=['GET'])
def ping():
    return "Get / is working"

@app.route('/predict', methods=['POST'])
def route_predict():
    unstructured_text = request.get_json()

    #with open('PATH_MODEL', 'rb') as f:
        # model = load(f)
        # f.close()

    #cal prediction function with data and model
    #
    res = predict([unstructured_text["1"]])

    response = {
        'res': res
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
