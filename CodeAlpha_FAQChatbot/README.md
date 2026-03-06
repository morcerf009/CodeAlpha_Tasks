# FAQ Smart Assistant - NLP Chatbot

A simple and effective FAQ Chatbot built with Python and NLP techniques. This bot understands user queries and matches them with the most relevant answers from a predefined knowledge base.

## 🚀 Features
- **Intelligent Processing**: Uses NLTK for text cleaning and stemming.
- **Accuracy**: Employs TF-IDF and Cosine Similarity for precise question matching.
- **Web Interface**: Easy-to-use chat UI built with Flask.
- **Comprehensive FAQ Dataset**: Pre-loaded with categories including shipping, returns, payments, account management, and more.
- **Auto-Suggestions**: Includes clickable chips for common questions to improve user experience.

## 🛠️ Technological Stack
- **Backend**: Python, Flask
- **Machine Learning/NLP**: Scikit-learn, NLTK
- **Frontend**: HTML5, CSS3, JavaScript (jQuery)
- **Data Format**: JSON

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd CodeAlpha_FAQChatbot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK Data**:
   The application automatically handles NLTK downloads on the first run, but ensure you have an active internet connection.

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the Chatbot**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

## 📂 Project Structure
- `app.py`: Flask server and NLP logic core.
- `faq_data.json`: The knowledge base containing questions and answers.
- `templates/index.html`: The web interface.
- `requirements.txt`: List of Python dependencies.

## 📝 Usage
Type your question in the chat box or click one of the suggestion chips. The bot will analyze your query and provide the matching answer from the knowledge base. If no high-confidence match is found, it will provide a helpful fallback response.
