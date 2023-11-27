# Project JobEasy - Website Slice Guide

## Prerequisites
- **Python**: Ensure Python is installed on your system.
- **Flask**: A Python web framework. Install with `pip install flask`.
- **NLTK**: For natural language processing. Install with `pip install nltk`.
- **Joblib**: For loading the model. Install with `pip install joblib`.

## Steps to Run the Website

### 1. Clone the Repository
Clone the repository to your local machine using Git:
git clone https://github.com/sai-harsha-k/Project_jobEasy.git
cd Project_jobEasy/website-slice

### 2. Set Up the Environment
Ensure Python is installed (`python --version`). If not, download it from [Python's official website](https://www.python.org/).

### 3. Install Dependencies
Install the required Python packages:

pip install flask nltk joblib

### 4. Run the Flask Application
In the `website-slice` directory, run:


### 5. Access the Website
Open `http://127.0.0.1:5000/` in a web browser.

### 6. Using the Application
Enter text in the input field and click "Predict" for the MBTI type prediction.

## Notes
- The application uses `model_cat.pkl`, `target_encoder.pkl`, and `vector.pkl` for predictions.
- The web interface is in `index.html` and `result.html` in the `templates` folder.

## Troubleshooting
Ensure all dependencies are installed and `app.py` is run from the correct directory.
