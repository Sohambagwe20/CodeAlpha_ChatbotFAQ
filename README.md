# 🤖 AI FAQ Chatbot — CodeAlpha Internship Task 2

A conversational FAQ chatbot built from scratch using **Python** and **Natural Language Processing (NLP)** techniques. The chatbot answers questions related to **Artificial Intelligence**, Machine Learning, Deep Learning, and more — with a clean browser-based chat UI powered by Streamlit.

---

## 🎯 Project Overview

This project was built as part of the **CodeAlpha AI Internship — Task 2: Chatbot for FAQs**.

The chatbot takes a user's question, preprocesses it using NLP, compares it against a set of predefined FAQs using **TF-IDF vectorization** and **Cosine Similarity**, and returns the most relevant answer.

---

## 🖥️ Demo

> Type a question like *"What is machine learning?"* or *"What is a neural network?"* and the chatbot finds the best matching answer instantly.

![Chatbot UI](https://img.shields.io/badge/Built%20With-Streamlit-red?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![NLP](https://img.shields.io/badge/NLP-NLTK-green?style=for-the-badge)

---

## 🧠 How It Works

```
User types a question
        ↓
Preprocess input (lowercase → remove punctuation → tokenize → remove stopwords → stem)
        ↓
Convert to TF-IDF vector
        ↓
Compare against all FAQ questions using Cosine Similarity
        ↓
Return the answer with the highest similarity score
```

---

## 📁 Project Structure

```
CodeAlpha_ChatbotFAQ/
│
├── faq_data.py          # 20 FAQ questions & answers about AI
├── preprocessor.py      # NLP text cleaning using NLTK
├── matcher.py           # TF-IDF + Cosine Similarity matching logic
├── chatbot.py           # Chatbot class with greeting, farewell & respond logic
├── app.py               # Streamlit web UI (chat interface)
└── requirements.txt     # Project dependencies
```

---

## 🔧 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NLTK | Tokenization, stopword removal, stemming |
| Scikit-learn | TF-IDF Vectorizer + Cosine Similarity |
| Streamlit | Browser-based chat UI |

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Sohambagwe20/CodeAlpha_ChatbotFAQ.git
cd CodeAlpha_ChatbotFAQ
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the chatbot (browser UI)
```bash
python -m streamlit run app.py
```

### 4. Or run in terminal only
```bash
python chatbot.py
```

---

## 💬 Sample Questions to Try

- What is artificial intelligence?
- What is machine learning?
- What is deep learning?
- What is a neural network?
- What is NLP?
- What is reinforcement learning?
- What is TensorFlow?
- What is a large language model?
- What are real world applications of AI?
- What is overfitting?

---

## 📸 Features

- ✅ Clean chat bubble UI in the browser
- ✅ Sidebar with suggested questions
- ✅ Handles greetings and farewells naturally
- ✅ Fallback message for unrecognized questions
- ✅ Clear chat / reset button
- ✅ NLP preprocessing pipeline (tokenize, stem, stopword removal)
- ✅ TF-IDF + Cosine Similarity for accurate FAQ matching

---

## 📚 Concepts Used

**TF-IDF (Term Frequency - Inverse Document Frequency)**
Converts text into numerical vectors where important words get higher scores.

**Cosine Similarity**
Measures the similarity between two text vectors. Score ranges from 0 (no match) to 1 (perfect match). The FAQ with the highest score is returned.

**Porter Stemmer**
Reduces words to their root form — e.g. "learning" → "learn", "running" → "run" — so variations of the same word are treated equally.

---

## 👨‍💻 Author

**Soham Bagwe**
AI Intern @ CodeAlpha
GitHub: [@Sohambagwe20](https://github.com/Sohambagwe20)

---

## 🏢 About CodeAlpha

CodeAlpha is a leading software development company dedicated to driving innovation across emerging technologies. This project was built as part of their AI Internship program.

🌐 [www.codealpha.tech](https://www.codealpha.tech)