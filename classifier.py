import dataloader,data_engineering
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,f1_score,confusion_matrix
import joblib
svm = SVC(probability=True)
# Prepare data
sentences,labels = dataloader.load_from_path("Data/data.json")
# Preprocess text
sentences = [data_engineering.preprocess(sentence) for sentence in sentences]
# N-gram vectorize
sentences_vector = data_engineering.train_ngram(sentences)

# Onehot
labels,class_name = data_engineering.one_hot_encode(labels)

def train(sentences,labels):
    # Train classifier
    svm.fit(sentences_vector,labels)
    # Dump classifier
    joblib.dump(svm,"models/svm_classifier.pkl")

train(sentences,labels)
def load_model(path="models/svm_classifier.pkl"):
    return joblib.load(path)


# Eval
def evaluate(sentences,labels):
    if isinstance(sentences,str): sentences = [sentences]

    svm_classifier = load_model()
    # Load svm model
    prediction = svm_classifier.predict(sentences)

    # Check len
    if not len(prediction) == len(sentences_vector):
        raise Exception("Sentences and labels has no similar dimensions")
    # Accuracy
    print(f"Accuracy: {accuracy_score(labels,prediction)*100}%")
    # F1-score

def predict(sentence):
    if isinstance(sentence,str): sentence = [sentence]
    # Preprocessing
    sentence = [data_engineering.preprocess(sent) for sent in sentence]
    # Convert text to vector
    sentence_vector = data_engineering.ngram_vectorize(sentence)

    # Load classfier model
    svm_classifier = load_model()
    predictions = svm_classifier.predict(sentence_vector)
    prob = svm_classifier.predict_proba(sentence_vector)
    print(prob)
    print(predictions)


    # Class name
    class_predictions = [class_name[index] for index in predictions]
    return predictions,class_predictions