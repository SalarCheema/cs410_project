import pandas as pd
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np


data = pd.read_csv("political_data.csv")

sentences = [text.split() for text in data['text']]
w2v_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

def get_sentence_embedding(sentence):
    words = sentence.split()
    word_vectors = [w2v_model.wv[word] for word in words if word in w2v_model.wv]
    if word_vectors:
        return np.mean(word_vectors, axis=0)
    else:
        return np.zeros(w2v_model.vector_size)

data['text_vector'] = data['text'].apply(get_sentence_embedding)

# Combine Text and Upvote Score Features
X = np.array([np.append(vec, score) for vec, score in zip(data['text_vector'], data['score'])])
y = data['expected_political_leaning']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tain a Classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Make Predictions and Evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# To make predictions on new data
def predict_paragraph(text, upvote_score):
    text_vector = get_sentence_embedding(text)
    features = np.append(text_vector, upvote_score)
    return clf.predict([features])[0]  # 0 for Democrat, 1 for Republican

# example prediction
new_text = "Test paragraph to see leaning expected near fifty"
new_upvote_score = 150
prediction = predict_paragraph(new_text, new_upvote_score)
print("Prediction:", "Republican" if prediction == 1 else "Democrat")