# 📰 Fake News Detection App

This is a simple AI-powered Fake News Detection web app built using **Python**, **Streamlit**, and **Scikit-learn**. It helps you determine whether a news article is **REAL** or **FAKE** based on its title, content, and subject.

---

## 🚀 Features

- Takes in **news title**, **text content**, and **subject**
- Detects whether the news is likely **REAL** or **FAKE**
- Uses the [ISOT Fake News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- Provides a sample of the training data
- Simple and interactive **Streamlit UI**

---

## 📁 Dataset Structure (ISOT)

The dataset contains two CSV files:

- `archive/True.csv` – 21,000+ real news articles
- `archive/Fake.csv` – 23,000+ fake news articles

Each CSV has the following columns:

| Column   | Description                                     |
|----------|-------------------------------------------------|
| title    | Title of the news article                       |
| text     | Full text of the news article                   |
| subject  | Topic category (e.g., politics, tech, world)    |
| date     | Date the article was published                  |

For training, a `label` column (`REAL` or `FAKE`) is added during preprocessing.

---

## 🛠 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Supriya902/Fake_news_detector.git
   cd Fake_news_detector
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Place Dataset:**
   Ensure True.csv and Fake.csv are located inside an archive/ folder like:
   ```bash
   Fake_news_detector/
   ├── archive/
   │   ├── True.csv
   │   └── Fake.csv
   ```
## ▶ Running the App

```bash
 streamlit run app.py
```
Once running, the app will:

* Load and preprocess the dataset
* Train a logistic regression model (if not already trained)
* Launch the Streamlit UI in your browser

---

## 📅 Adding More News
To improve predictions or test with newer articles (like 2020+), you can manually add rows to:

* True.csv – For real news
* Fake.csv – For fake news

Example:

```bash
"Coronavirus pandemic declared by WHO","In March 2020 WHO declared COVID-19 a global pandemic.","health","2020-03-11"
```

> ⚠ After adding new rows, **delete model.pkl and vectorizer.pkl** to retrain the model with updated data.

---

## 🧪 Example Prediction

*Input:*

* Title: Coronavirus pandemic declared by WHO
* Subject: health
* Content: In March 2020 WHO declared COVID-19 a global pandemic.

*Output:*

```bash
🟢 This news article is likely REAL.
```

---

## 📚 Requirements

* Python 3.8+
* streamlit
* pandas
* scikit-learn
* pickle

---

## 📌 Credits

* Dataset: [ISOT Fake News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
* App developed using [Streamlit](https://streamlit.io/)
