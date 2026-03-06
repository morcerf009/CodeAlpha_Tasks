# Language Translation Tool

A streamlined, web-based application for translating text between multiple languages. Built with Python and Streamlit, this tool leverages the Google Translate API for accurate real-time translations and includes Text-to-Speech (TTS) capabilities.

## Features

- **Real-time Translation**: Instant translation between 7+ major languages.
- **Auto-detection**: Automatically detects the source language.
- **Text-to-Speech**: Listen to the translated text with a single click.
- **Copy Functionality**: Easily copy translated text to your clipboard.
- **Responsive Design**: Clean and accessible user interface.

## Technologies Used

- **Python 3.11+**
- **Streamlit**: For the web interface.
- **deep-translator**: For Google Translate API integration.
- **gTTS (Google Text-to-Speech)**: For audio generation.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/LanguageTranslationTool.git
    cd LanguageTranslationTool
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application locally:

```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
