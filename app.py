import streamlit as st
import pickle
from PyPDF2 import PdfReader
import re
import nltk 
import string
from nltk.corpus import stopwords
# loading pickle files of model and other 
model = pickle.load(
    open('svm.pkl','rb')
)

tfidf = pickle.load(
    open('tfidf.pkl','rb')
)

le = pickle.load(
    open('label_encoder.pkl' , 'rb')
)


st.title("RESUME SCREENING SYSTEM BY MURLI MISHRA")

def extract_text_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + " "

    return text

uploaded_file = st.file_uploader(
    "Upload the file or resume",
    type = ['pdf']
)
if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.write(resume_text)

# Text Cleaning function using NLP library re (Regular Expressiom)

    def clean_text(text):
       text = text.lower()
       text = re.sub(r'http\S+|www\S+','',text)
       text = re.sub(r'\S+@+\S+','',text)
       text = re.sub(r'\d+','',text)
       text = text.translate(str.maketrans('','',string.punctuation))
       text = re.sub(r'\s+',' ',text)
       return text

    resume_text = clean_text(resume_text)

    words = resume_text.split()
    stop_words = set(stopwords.words('english'))
    stop_words.discard('not')
    stop_words.discard('no')
    stop_words.discard('without')

    filtered = lambda x:" ".join(
    word for word in x.split()
    if word not in stop_words
    )
    resume_text = filtered(resume_text)

    vector = tfidf.transform([resume_text])
    prediction = model.predict(vector)
    category = prediction

    st.success(
        f"Predicted Role according to the Resume : {category[0]}"
    )
    st.subheader("Extracted Resume")
    st.write(resume_text[:1000])
    st.balloons()





