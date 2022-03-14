import numpy as np
from flask import Flask, request, jsonify, render_template
from tools import predcitor

# Create flask app
flask_app = Flask(__name__)

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    text = str(request.form)
    prediction = predcitor(text)
    return render_template("index.html", prediction_text = "The dialect is {}".format(prediction.upper()))

if __name__ == "__main__":
    flask_app.run(debug=True)