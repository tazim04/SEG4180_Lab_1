from flask import Flask, request, jsonify
from transformers import pipeline

# init flask app
app = Flask(__name__)

# load pretrained model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

@app.route("/")
def home():
    return "Flask app is running"

# prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    if "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    result = classifier(text) # perform sentiment analysis

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)