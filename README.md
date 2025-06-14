# 📰 Fake News Detection App

This is a simple AI-powered Fake News Detection web app built using **Python**, **Streamlit**, and **Scikit-learn**. It helps you determine whether a news article is **REAL** or **FAKE** based on its title, content, and subject.

---

## 🚀 Features

- Takes in **news title**, **text content**, and **subject**
- Detects whether the news is likely **REAL** or **FAKE**
- Uses the [ISOT Fake News Dataset](https://www.uvic.ca/engineering/ece/isot/datasets/fake-news/index.php)
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
   git clone https://github.com/yourusername/fake-news-detector.git
   cd fake-news-detector
