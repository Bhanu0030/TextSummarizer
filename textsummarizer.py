import re
import streamlit as st

# NLTK Packages
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# SPACY Packages
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# NLTK Summarizer
def nltk_summarizer(docx):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(docx)
    freqTable = dict()

    for word in words:
        word = word.lower()
        if word not in stopWords:
            freqTable[word] = freqTable.get(word, 0) + 1

    sentence_list = sent_tokenize(docx)
    max_freq = max(freqTable.values())

    for word in freqTable:
        freqTable[word] = freqTable[word] / max_freq

    sentence_scores = {}
    for sent in sentence_list:
        for word in word_tokenize(sent.lower()):
            if word in freqTable and len(sent.split(' ')) < 30:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freqTable[word]

    import heapq
    summary_sentences = heapq.nlargest(8, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)

# spaCy Summarizer
def spacy_summarizer(docx):
    stopWords = list(STOP_WORDS)
    words = word_tokenize(docx)
    freqTable = dict()

    for word in words:
        word = word.lower()
        if word not in stopWords:
            freqTable[word] = freqTable.get(word, 0) + 1

    sentence_list = sent_tokenize(docx)
    max_freq = max(freqTable.values())

    for word in freqTable:
        freqTable[word] = freqTable[word] / max_freq

    sentence_scores = {}
    for sent in sentence_list:
        for word in word_tokenize(sent.lower()):
            if word in freqTable and len(sent.split(' ')) < 30:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freqTable[word]

    import heapq
    summary_sentences = heapq.nlargest(8, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)

# Streamlit App
def main():
    st.title("Text Summarizer App")
    activities = ["Summarize Via Text"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == 'Summarize Via Text':
        st.subheader("Summary using NLP")
        article_text = st.text_area("Enter Text Here", "Type here")

        # Clean input text
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub('[^a-zA-Z.,]', ' ', article_text)
        article_text = re.sub(r'\b[a-zA-Z]\b', '', article_text)
        article_text = re.sub("[A-Z]\Z", '', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)

        summary_choice = st.selectbox("Summary Choice", ["NLTK", "SPACY"])

        if st.button("Summarize Via Text"):
            if summary_choice == 'NLTK':
                summary_result = nltk_summarizer(article_text)
            else:
                summary_result = spacy_summarizer(article_text)

            st.success("Summary:")
            st.write(summary_result)

if __name__ == '__main__':
    main()
