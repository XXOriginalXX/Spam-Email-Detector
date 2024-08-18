# Email Spam Detector
## Overview
This project implements an email spam detection system using a Naive Bayes classifier. The model is trained on a dataset of labeled emails (spam and ham) and predicts whether a given email is spam or not based on its content.
## Features
* Text Processing: The email content is transformed into a numerical format using a CountVectorizer.
* Model Training: A Naive Bayes classifier is trained on the processed data.
* Prediction: The model can predict whether a new email is spam or not.
* Accuracy Measurement: The model's accuracy is evaluated on a test set.
## Usage
** 1. Run the script:**
```bash
python emailspamdetector.py
```
** 2. Input the content of the email you want to classify when prompted.**
** 3.The model will output whether the email is "spam" or "ham" (not spam).**

