# Email Spam Detector
## Overview
This project implements an email spam detection system using a Naive Bayes classifier. The model is trained on a dataset of labeled emails (spam and ham) and predicts whether a given email is spam or not based on its content.
## Features
* Text Processing: The email content is transformed into a numerical format using a CountVectorizer.
* Model Training: A Naive Bayes classifier is trained on the processed data.
* Prediction: The model can predict whether a new email is spam or not.
* Accuracy Measurement: The model's accuracy is evaluated on a test set.
## Usage
* Run the script:
```bash
python emailspamdetector.py
```
* Input the content of the email you want to classify when prompted.
* The model will output whether the email is "spam" or "ham" (not spam).

## Dataset
The dataset used for training and testing the model is derived from publicly available data. It contains labeled emails with their corresponding classifications as either spam or ham.

### Note: The dataset was obtained from Kaggle, and its accuracy and completeness are not guaranteed.

## Results
The model's performance is evaluated using accuracy and a confusion matrix. The accuracy score and confusion matrix are displayed after the model is tested.
## License
This project is for educational purposes and does not have a specific license. The dataset's original source should be credited if used in other projects.

