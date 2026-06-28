# Resume Screening System 📄🤖

An end-to-end NLP-based Resume Screening System that predicts a candidate's job category from their uploaded resume PDF. The project demonstrates the complete machine learning pipeline, from text preprocessing and feature engineering to model training and deployment using Streamlit.

## 🚀 Features

* Upload resumes in PDF format
* Extract text from resumes using PyPDF2
* Perform NLP-based text preprocessing
* Convert text into numerical features using TF-IDF
* Predict the most suitable job category using Machine Learning
* Interactive web interface built with Streamlit

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* PyPDF2
* Streamlit

---

## 🧠 Machine Learning Concepts Used

### Natural Language Processing (NLP)

* Text Cleaning using Regular Expressions
* Lowercasing
* Removing URLs, Emails, Numbers, and Punctuation
* Stopword Removal using NLTK

### Feature Engineering

* TF-IDF (Term Frequency-Inverse Document Frequency)

### Machine Learning Models Experimented With

* Multinomial Naive Bayes
* Logistic Regression
* Support Vector Machine (SVM)

### Model Performance

| Model                        | Accuracy |
| ---------------------------- | -------- |
| Multinomial Naive Bayes      | ~56%     |
| Logistic Regression          | ~65%     |
| Support Vector Machine (SVM) | ~72%     |

SVM achieved the best performance and was selected for deployment.

---

## 📊 Dataset Information

* Total Resumes: 2,484
* Total Categories: 24

Example categories:

* Information Technology
* Engineering
* Finance
* HR
* Healthcare
* Sales
* Business Development
* Banking
* Public Relations
* Designer

---

## ⚙️ Project Workflow

```text
Resume PDF
      ↓
Text Extraction
      ↓
Text Cleaning & NLP Preprocessing
      ↓
TF-IDF Vectorization
      ↓
SVM Classification
      ↓
Predicted Job Category
```

---

## 📂 Project Structure

```text
ResumeScreeningSystem/
│
├── app.py
├── Resume_Screening.ipynb
├── model.pkl
├── tfidf.pkl
├── label_encoder.pkl
├── requirements.txt
├── dataset/
└── README.md
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ResumeScreeningSystem.git
cd ResumeScreeningSystem
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Application Demo

1. Upload a resume PDF.
2. The system extracts and preprocesses the text.
3. The trained SVM model predicts the most relevant job category.

---

## ⚠️ Current Limitations

The dataset contains only broad job categories such as:

* INFORMATION-TECHNOLOGY
* ENGINEERING
* FINANCE
* HR

Because of this limitation, the model cannot yet distinguish between more specific roles such as:

* Machine Learning Engineer
* Data Scientist
* Backend Developer
* Frontend Developer
* DevOps Engineer
* Data Analyst

---

## 🔮 Future Improvements

* Use a larger and more fine-grained dataset.
* Predict specific job roles instead of broad categories.
* Add Top-3 role recommendations.
* Implement skill extraction and ATS scoring.
* Compare resumes with job descriptions.
* Add OCR support for scanned PDF resumes.
* Deploy the application online.

---

## 🎯 Learning Outcomes

This project helped me gain practical experience in:

* Natural Language Processing (NLP)
* Text Classification
* Feature Engineering
* Machine Learning Model Evaluation
* Building and Deploying End-to-End ML Applications

---

⭐ If you found this project interesting, feel free to star the repository and connect with me!
