# 🎬 Movie Recommender System

> A Machine Learning based Movie Recommendation System that suggests similar movies using Content-Based Filtering and Cosine Similarity.

---

## 🚀 Live Demo : https://movie-recommendation-npeecu6gbjeklvvsxcrovz.streamlit.app/

🌐 Deployed on:

- 🤗 Hugging Face Spaces
- ☁️ Streamlit Community Cloud

---

## 📌 Features

✨ Movie Recommendation based on content similarity

🎭 Uses:
- Genres
- Keywords
- Cast
- Crew
- Overview

🎨 Modern Streamlit UI

🌙 Dark Theme

❄️ Snow Animation

🎬 Netflix-Inspired Layout

🔍 Movie Search Dropdown

⚡ Fast Recommendations

---

## 🛠️ Tech Stack

### 👨‍💻 Programming Language

- Python

### 📚 Libraries

- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Requests
- Pickle

### 🤖 Machine Learning

- CountVectorizer
- Cosine Similarity

## 📂 Dataset

This project uses the **TMDB 5000 Movie Dataset**.

📁 Files Used:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

## ⚙️ Project Workflow

### 1️⃣ Data Collection

📥 Loaded movie and credits datasets.

---

### 2️⃣ Data Preprocessing

✔️ Merged datasets

✔️ Removed unnecessary columns

✔️ Handled missing values

✔️ Extracted:
- Genres
- Keywords
- Top 3 Cast Members
- Director
- Overview

---

### 3️⃣ Feature Engineering

Created a new **tags** column by combining:

- 📝 Overview
- 🎭 Genres
- 🔑 Keywords
- 👨‍🎤 Cast
- 🎬 Crew

---

### 4️⃣ Text Vectorization

Used:

```python
CountVectorizer()
```

to convert movie tags into numerical vectors.

---

### 5️⃣ Similarity Calculation

Calculated similarity using:

```python
cosine_similarity()
```

---

### 6️⃣ Recommendation Engine

🎯 Returns the Top 5 most similar movies.

---

### 7️⃣ Web Application

Built an interactive web application using Streamlit.

---

## 🗂️ Project Structure

```text
Movie-Recommender-System/
│
├── app.py
├── movie_list.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
│-- 1_movie_recommender_system.ipynb
├── tmdb_5000_movies.csv
└── tmdb_5000_credits.csv
```

---

## 💻 Installation

### 📥 Clone Repository

```bash
git clone https://github.com/your-username/movie-recommender-system.git
```

### 📂 Move into Project Folder

```bash
cd movie-recommender-system
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🌍 Deployment

### ☁️ Streamlit Community Cloud

Used for easy online deployment and sharing.

### 🤗 Hugging Face Spaces

Used to host and deploy the application publicly.

---

## 🔮 Future Improvements

- 🎞️ Trailer Support
- 🎭 Genre-Based Recommendations
- ❤️ User Favorites
- 🤝 Collaborative Filtering
- 🧠 Hybrid Recommendation System

---

## 📚 What I Learned

✅ Data Preprocessing

✅ Feature Engineering

✅ Natural Language Processing Basics

✅ Count Vectorization

✅ Cosine Similarity

✅ Streamlit Development

✅ Git & GitHub

✅ Model Deployment

✅ Hugging Face Spaces

---

## 👨‍💻 Author

### Shashank Kumar Jha

🎓 Data Science Student

🤖 Machine Learning Enthusiast

📊 Aspiring Data Scientist

---

## ⭐ Support

If you liked this project, consider giving it a ⭐ on GitHub!

It motivates me to build more Machine Learning projects 🚀
