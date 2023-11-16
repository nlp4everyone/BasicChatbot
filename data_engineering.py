import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import joblib
from sklearn.preprocessing import LabelEncoder
one_hot = LabelEncoder()
n_gram = CountVectorizer(ngram_range=(1,2))
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Make folder
os.makedirs("models",exist_ok=True)
def preprocess(text):
    # Lower text
    text = text.lower()

    # Remove special character
    text = re.sub("\W+"," ",text)
    # Remove stop words
    word_tokens = word_tokenize(text)
    text = [token for token in word_tokens if not token in stop_words]
    return " ".join(text)

# N-gram vectorizer
def train_ngram(text):
    # Fit method
    n_gram.fit(text)

    # Save models
    joblib.dump(n_gram,"models/ngram_vectorizer.pkl")
    return n_gram.transform(text).toarray()

def ngram_vectorize(text):
    ngram_model = joblib.load("models/ngram_vectorizer.pkl")
    return ngram_model.transform(text).toarray()

# One hot
def one_hot_encode(list_class):
    one_hot_label = one_hot.fit_transform(list_class)
    return one_hot_label,one_hot.classes_