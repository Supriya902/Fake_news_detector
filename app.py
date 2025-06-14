import streamlit as st
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# ----------------------
# Load and Prepare Data
# ----------------------
@st.cache_data
def load_data():
    true_df = pd.read_csv("archive/True.csv")
    fake_df = pd.read_csv("archive/Fake.csv")

    true_df['label'] = 'REAL'
    fake_df['label'] = 'FAKE'

    df = pd.concat([true_df, fake_df], ignore_index=True)
    df.dropna(subset=['title', 'text', 'subject'], inplace=True)
    df['content'] = df['title'] + " " + df['text'] + " " + df['subject']
    return df

# ----------------------
# Train and Save Model
# ----------------------
def train_model():
    df = load_data()
    X = df['content']
    y = df['label']

    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    X_vect = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    with open("vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    return model, vectorizer

# ----------------------
# Load Model and Vectorizer
# ----------------------
def load_model():
    if os.path.exists("model.pkl") and os.path.exists("vectorizer.pkl"):
        with open("vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
    else:
        model, vectorizer = train_model()
    return model, vectorizer

# ----------------------
# Streamlit UI
# ----------------------
st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 Fake News Detection App")
st.markdown("""
This AI model can help you identify whether a news article is **Real** or **Fake**.
Provide a **title**, **news content**, and **subject** of the article to get started.
""")

# Input fields
title = st.text_input("Enter News Title:")
subject = st.text_input("Enter News Subject (e.g., politics, world, etc.):")
text = st.text_area("Enter Full News Content:", height=250)

# Predict button
if st.button("Detect"):
    if not title or not text or not subject:
        st.warning("Please fill all fields.")
    else:
        full_input = title + " " + text + " " + subject
        model, vectorizer = load_model()
        vect_input = vectorizer.transform([full_input])
        prediction = model.predict(vect_input)[0]

        if prediction == 'FAKE':
            st.error("🔴 This news article is likely **FAKE**.")
        else:
            st.success("🟢 This news article is likely **REAL**.")

# Optional: Show training data
with st.expander("See Training Dataset Sample"):
    st.dataframe(load_data().sample(5))
