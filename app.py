from flask import Flask, render_template, request
import pickle
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Home page
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/findcrop")
def findcrop():
    return render_template("index.html")

# Prediction page
@app.route("/predict", methods=["POST"])
def predict():

    # Get values from the form
    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    # Create DataFrame
    sample = pd.DataFrame({
        "N": [N],
        "P": [P],
        "K": [K],
        "temperature": [temperature],
        "humidity": [humidity],
        "ph": [ph],
        "rainfall": [rainfall]
    })

    # Predict crop
    prediction = model.predict(sample)[0]

    return render_template("result.html", prediction=prediction)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)