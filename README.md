# Email Spam Detector
## Overview
This project implements an email spam detection system using a Naive Bayes classifier. The model is trained on a dataset of labeled emails (spam and ham) and predicts whether a given email is spam or not based on its content.
## Features
* Text Processing: The email content is transformed into a numerical format using a CountVectorizer.
* Model Training: A Naive Bayes classifier is trained on the processed data.
* Prediction: The model can predict whether a new email is spam or not.
* Accuracy Measurement: The model's accuracy is evaluated on a test set.
```bash
pip install pandas scikit-learn seaborn matplotlib
