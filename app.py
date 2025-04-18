import streamlit as st
import pickle
import pandas as pd
import string

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required NLTK resources only if not already present
nltk_packages = ['punkt', 'stopwords']
for pkg in nltk_packages:
    try:
        nltk.data.find(f'tokenizers/{pkg}' if pkg == 'punkt' else f'corpora/{pkg}')
    except LookupError:
        nltk.download(pkg)


# import nltk
# from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# # Check if the 'punkt' resource is already downloaded
# try:
#     nltk.data.find('tokenizers/punkt')
# except LookupError:
#     nltk.download('punkt')

# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    #text = nltk.word_tokenize(text)
    text = word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    y_text = [i for i in y if i.lower() not in stopwords.words('english') and i not in string.punctuation ]  
    y_final = [ps.stem(i) for i in y_text ]
    return " ".join(y_final)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

# 1. preprocess
    transformed_sms = transform_text(input_sms)
# 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
# 3. predict
    result = model.predict(vector_input)
# 4. display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not a spam")

