# TextSummarizer
This project is a NLP-based text summarization tool built with Streamlit, supporting both NLTK and spaCy summarization techniques. It allows users to input raw text and receive a condensed version using frequency-based sentence scoring methods.
🔍 Features
Summarizes input text using:

NLTK (Natural Language Toolkit)

spaCy

Real-time summarization through a simple web interface

Removes stopwords and uses normalized word frequencies

Uses heapq for selecting top-ranked sentences

🧠 Technologies
Python 3.x

Streamlit

NLTK (punkt, stopwords)

spaCy (en_core_web_sm)

🚀 How to Run
Install dependencies:

bash
Copy
Edit
pip install streamlit nltk spacy
python -m nltk.downloader punkt stopwords
python -m spacy download en_core_web_sm
Start the app:

bash
Copy
Edit
streamlit run textsummarizer.py
📚 Use Case
Ideal for academic researchers, students, and anyone looking to extract key information from long text documents using rule-based extractive summarization.

