from flask import Flask, render_template, request
import json
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Ensure NLTK data is downloaded
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')

# Load the knowledge base
def load_faq_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

# Clean and prepare user input
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    
    # Filter out stopwords and apply stemming for better matching
    tokens = [stemmer.stem(word) for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(tokens)

# Find the most relevant answer using similarity scores
def find_best_match(user_query, faq_list, vectorizer, tfidf_matrix):
    preprocessed_query = preprocess_text(user_query)
    query_vector = vectorizer.transform([preprocessed_query])
    
    # Use cosine similarity to find the closest match
    similarities = cosine_similarity(query_vector, tfidf_matrix)
    best_match_index = similarities.argmax()
    best_match_score = similarities[0][best_match_index]
    
    # Return answer if it's over the confidence threshold
    if best_match_score > 0.3:
        return faq_list[best_match_index]['answer']
    else:
        return "I'm sorry, I don't have an answer for that. Please try rephrasing your question."

# Initializing data and tools
faq_data = load_faq_data('faq_data.json')
questions = [item['question'] for item in faq_data]
preprocessed_questions = [preprocess_text(q) for q in questions]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_questions)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return find_best_match(userText, faq_data, vectorizer, tfidf_matrix)

if __name__ == "__main__":
    app.run(debug=True)
