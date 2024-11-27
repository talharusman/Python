import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
df['message'] = df['message'].str.replace('[^\w\s]', '').str.lower()

X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.3, random_state=42)
count_vectorizer = CountVectorizer()
X_train_counts = count_vectorizer.fit_transform(X_train)
X_test_counts = count_vectorizer.transform(X_test)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)

nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_tfidf, y_train)

y_pred = nb_classifier.predict(X_test_tfidf)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

new_emails = [
    "Congratulations! You have won a $1000 gift card. Claim now!",
    "Hey, can we meet tomorrow at 3 PM?",
    "Your bank account has been compromised. Please update your details.",
    "Thanks for the update. Looking forward to our meeting next week."
]

new_emails_counts = count_vectorizer.transform(new_emails)
new_emails_tfidf = tfidf_transformer.transform(new_emails_counts)
predictions = nb_classifier.predict(new_emails_tfidf)

for email, label in zip(new_emails, predictions):
    print(f"Email: {email}\nPrediction: {'Spam' if label == 1 else 'Ham'}\n")

with open('spam_classifier.pkl', 'wb') as model_file:
    pickle.dump(nb_classifier, model_file)

with open('count_vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(count_vectorizer, vectorizer_file)

with open('spam_classifier.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

with open('count_vectorizer.pkl', 'rb') as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)

new_email = ["You have won a lottery! Call us now to claim your prize."]
new_email_counts = loaded_vectorizer.transform(new_email)
new_email_tfidf = tfidf_transformer.transform(new_email_counts)
new_prediction = loaded_model.predict(new_email_tfidf)

print(f"Email: {new_email[0]}\nPrediction: {'Spam' if new_prediction[0] == 1 else 'Ham'}")
