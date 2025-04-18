# 📩 SMS/Email Spam Classifier

This is a simple yet powerful web app built with **Streamlit** that uses machine learning (ML) to classify SMS or email messages as **Spam** or **Not Spam**.

---

## 🚀 Features

- Built with `Streamlit` for an interactive front-end  
- Uses Natural Language Processing (NLP) for text preprocessing  
- Trained on a dataset using TF-IDF vectorization and an ML classifier  
- Supports multiple ML models (currently loaded via `model.pkl`)

---

## 🛠️ Technologies Used

- Python 🐍  
- Scikit-learn  
- XGBoost  
- NLTK  
- Streamlit

---

## 📂 Project Structure

```
├── app.py                       # Streamlit app
├── spam.csv                     # Dataset (used during model training)
├── model.pkl                    # Trained ML model
├── vectorizer.pkl               # Fitted TF-IDF vectorizer
├── requirements.txt             # Python dependencies
├── Procfile                     # For deploying to Heroku (optional)
└── README.md                    # You're here!
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone <your-repo-url>
   cd SMS_Spam_Classifier
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 📦 Required NLTK Downloads

The app automatically checks for and downloads:
- `punkt` (for tokenization)
- `stopwords` (for filtering common English words)

But you can also download them manually if needed:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 🧠 How It Works

- Input message is converted to lowercase  
- Tokenized into words  
- Stopwords and punctuation are removed  
- Words are stemmed (e.g., "running" → "run")  
- Transformed into a TF-IDF vector  
- Classified using a pre-trained ML model

---

## 📸 Sample UI

```
+------------------------------+
| Email/SMS Spam Classifier    |
+------------------------------+
| Enter the message:           |
| [ This is a free prize! ]    |
|                              |
| [ Predict ]                  |
+------------------------------+
| Result:                      |
|     Spam                   |
+------------------------------+
```

---

## 🐳 Optional Deployment (Render)

Make sure you have:
- `Procfile`
- `requirements.txt`


```

---

## 🧾 License

MIT License – use freely and customize!
