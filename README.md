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

## Streamlit App Deployment on Render

To deploy your Streamlit app as a web service on Render, follow these steps:

## 1. Create a Render Account
   - Go to [Render](https://render.com/) and sign up for an account if you don't already have one.

## 2. Prepare Your Project
   - Ensure your project is ready with the following files:
     - `app.py`: Your Streamlit app.
     - `requirements.txt`: List of dependencies (if not already created).
     - `Procfile`: For deployment instructions.

## 3. Create a `Procfile`
   - A `Procfile` tells Render how to run your app. Create a `Procfile` in your project root directory and add the following content:
     ```
     web: streamlit run app.py --server.enableCORS false
     ```
     This tells Render to start your Streamlit app using the `streamlit run` command.

## 4. Set Up `requirements.txt`
   - If you don’t have a `requirements.txt` file yet, create one by running:
     ```bash
     pip freeze > requirements.txt
     ```
   - The `requirements.txt` file should include all the necessary Python libraries for your app, such as:
     ```
     streamlit
     scikit-learn
     xgboost
     nltk
     pandas
     pickle
     ```

## 5. Push Your Code to GitHub (or any Git repository)
   - If your project isn’t already in a Git repository, initialize one and push your project to GitHub (or another Git provider).
   - If it's already on GitHub, make sure the latest changes are pushed.

   Example:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/your-username/your-repository.git
   git push -u origin main

## 6. Deploy on Render
   - Go to [Render](https://render.com/) and click **New** > **Web Service**.
   - Choose **GitHub** as the source and authorize Render to access your GitHub account.
   - Select the repository with your Streamlit app.
   - Set the branch (usually `main`) to deploy and select **Python 3.x** as the environment.
   - Leave the **Build Command** empty.
   - In **Start Command**, enter:
     ```
     streamlit run app.py --server.enableCORS false
     ```
   - Click **Create Web Service**.

## 7. Wait for Deployment
   - Render will install dependencies from `requirements.txt` and deploy your app.
   - Once deployed, you'll get a live URL.

## 8. Access Your App
   - After deployment, access your app at:
     ```
     https://your-app-name.onrender.com
     ```

## 9. Continuous Deployment (Optional)
   - Any new changes pushed to the connected GitHub repository will automatically redeploy your app on Render.


```

---

## 🧾 License

MIT License – use freely and customize!
