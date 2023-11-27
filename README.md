# Project_jobEasy
Prerequisites:

Python installed on your system.
Flask, a Python web framework. Install it using - pip install flask.
NLTK for natural language processing. Install it using - pip install nltk.
Joblib for loading the model. Install it using -  pip install joblib.
Steps to Run the Website
Clone the Repository: First, clone the repository to your local machine using Git:

bash
Copy code
git clone https://github.com/sai-harsha-k/Project_jobEasy.git
Navigate to the website-slice directory:

bash
Copy code
cd Project_jobEasy/website-slice
Set Up the Environment: Make sure you have Python installed. You can check this by running python --version in your terminal. If Python is not installed, download and install it from the official website.

Install Dependencies: Install the required Python packages:

Copy code
pip install flask nltk joblib
Run the Flask Application: In the website-slice directory, there is a file named app.py. This is the main file that runs the Flask application. Start the server by running:

Copy code
python app.py
Access the Website: Once the Flask server is running, open a web browser and go to http://127.0.0.1:5000/. This should load the MBTI Predictor web application.

Using the Application: Enter text in the provided input field and click "Predict" to see the MBTI type prediction.

Notes
The application uses pre-trained models (model_cat.pkl, target_encoder.pkl, and vector.pkl) for predictions. These models are loaded in app.py.
The web interface is defined in the HTML templates index.html and result.html located in the templates folder.
Troubleshooting
If you encounter any issues, make sure all dependencies are correctly installed and that you are running the app.py script from the correct directory.
