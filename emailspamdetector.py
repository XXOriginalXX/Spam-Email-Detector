import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
dataset=pd.read_csv(r"C:\Users\adith\OneDrive\Desktop\Projects\ML\emailspamdataset\spam.csv",encoding='ISO-8859-1')
x = dataset['v2']
y = dataset['v1']
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
example=input("Enter the content of the email")
example_transformed = vectorizer.transform([example])
prediction = model.predict(example_transformed)
print(f'It is a : {prediction[0]} mail')