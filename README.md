# 📄 AI Resume Screening System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Machine%20Learning-NLP-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

An AI-powered Resume Screening System that automatically analyzes and ranks resumes based on a given Job Description using **Natural Language Processing (NLP)** and **Machine Learning** techniques.

The application extracts text from PDF resumes, compares them with the job description, calculates similarity scores, identifies matching and missing skills, and ranks candidates based on their relevance.

---

## 🌐 Live Demo

🚀 **Try the application here:**

**https://resumescreeningsystemdeep.streamlit.app/**

---

## 📌 GitHub Repository

**GitHub:**  
https://github.com/Deepal008/AI-Resume-Screening-System

---

# 📖 Project Overview

Recruiters often receive hundreds of resumes for a single job opening, making manual screening slow and time-consuming.

The **AI Resume Screening System** automates this process by:

- Extracting text from uploaded PDF resumes
- Processing resumes using NLP
- Comparing resumes with a Job Description
- Calculating Resume Match Percentage
- Ranking resumes based on similarity
- Identifying matched and missing skills
- Displaying interactive analytics and visualizations

This helps recruiters shortlist the most relevant candidates quickly and efficiently.

---

# ✨ Features

✅ Upload one or multiple PDF resumes

✅ Paste Job Description

✅ Automatic PDF text extraction

✅ NLP-based preprocessing

✅ TF-IDF Vectorization

✅ Cosine Similarity Matching

✅ Resume Ranking

✅ Skill Matching

✅ Missing Skills Detection

✅ Interactive Dashboard

✅ Resume Statistics

✅ Candidate Comparison

✅ Beautiful Streamlit UI

---

# 🛠️ Tech Stack

### Programming Language

- Python

### Frontend

- Streamlit

### Machine Learning

- Scikit-learn

### Natural Language Processing

- NLTK
- spaCy

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly
- Matplotlib

### PDF Processing

- pdfplumber
- PyPDF2

### Model Serialization

- Joblib

---

# 📂 Project Structure

```text
AI-Resume-Screening-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── resumes/
│   └── sample_jd.txt
│
├── src/
│   ├── pdf_reader.py
│   ├── preprocessing.py
│   ├── skill_match.py
│   ├── ranking.py
│   └── visualization.py
│
├── assets/
│
└── screenshots/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Deepal008/AI-Resume-Screening-System.git
```

Move into the project directory

```bash
cd AI-Resume-Screening-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download required NLP resources

```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
```

Run the application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```text
streamlit
plotly
pandas
numpy
scikit-learn
nltk
spacy
pdfplumber
PyPDF2
joblib
matplotlib
```

---

# 🚀 How It Works

### Step 1

Enter or paste the Job Description.

↓

### Step 2

Upload one or multiple PDF resumes.

↓

### Step 3

The system extracts text from each resume.

↓

### Step 4

Text is cleaned and preprocessed using NLP techniques.

↓

### Step 5

TF-IDF converts text into numerical vectors.

↓

### Step 6

Cosine Similarity compares each resume with the Job Description.

↓

### Step 7

Matching score is calculated.

↓

### Step 8

Candidates are ranked based on similarity score.

↓

### Step 9

Dashboard displays:

- Resume Rankings
- Best Candidate
- Average Match Score
- Skills Found
- Missing Skills
- Visual Analytics

---

# 📊 Machine Learning Techniques Used

- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Text Preprocessing
- Tokenization
- Stopword Removal
- Skill Extraction

---

# 📸 Application Preview

## Dashboard

> Add your application screenshots inside a `screenshots` folder and update the image paths.

```md
![Dashboard](screenshots/dashboard.png)
```

---

# 💡 Future Enhancements

- Resume Recommendation System
- AI-based Resume Feedback
- ATS Score Prediction
- Keyword Suggestions
- Resume Parsing using LLMs
- Multi-language Resume Support
- Authentication System
- Recruiter Dashboard
- Candidate Database
- Export Reports (PDF/Excel)

---

# 🎯 Use Cases

- HR Recruitment
- Resume Screening
- Campus Placement
- Internship Hiring
- Job Portals
- Talent Acquisition

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 👨‍💻 Author

**Deepal Yadav**

GitHub:
https://github.com/Deepal008

LinkedIn:
https://www.linkedin.com/in/deepal-yadav-293078230/

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further improvements.

---

# 📄 License

This project is licensed under the **MIT License**.

---

<p align="center">
Made with ❤️ using Python, Streamlit, NLP and Machine Learning
</p>