from flask import Flask, render_template, request
import joblib
from nltk.stem import WordNetLemmatizer

# Include the custom Lemmatizer class definition here
class Lemmatizer(object):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
    def __call__(self, sentence):
        return [self.lemmatizer.lemmatize(word) for word in sentence.split() if len(word) > 2]

app = Flask(__name__)

# Load the pre-trained model and the vectorizer
with open('model_cat.pkl', 'rb') as model_file:
    model = joblib.load(model_file)

with open('vector.pkl', 'rb') as vector_file:
    vectorizer = joblib.load(vector_file)

with open('target_encoder.pkl', 'rb') as encoder_file:
    target_encoder = joblib.load(encoder_file)


@app.route('/')
def index():
    # Render the main page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['user_input']
    transformed_input = vectorizer.transform([input_text])
    prediction = model.predict(transformed_input)

    # Convert prediction to label name
    label_names = target_encoder.inverse_transform(prediction)
    if label_names:
        selected_label = label_names[0]  # Assuming it's a single prediction
        prediction_result = selected_label
    else:
        prediction_result = "Invalid label number"

    return render_template('result.html', prediction=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
